from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from monitors.system_monitor import get_running_processes, get_system_usage
from detectors.threat_detector import analyze_process
from monitors.system_monitor import get_running_processes
from database.db import conn, cursor

app = FastAPI(title="AI Cyber Security Monitoring Tool")

@app.get("/")
def home():
    return {"status": "Cyber Security Monitor is Running"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#API Route
@app.get("/system/usage")
def system_usage():
    return get_system_usage()

@app.get("/system/processes")
def system_processes():
    return get_running_processes()
@app.get("/detect/threats")

#Detection API Route

@app.get("/detect/threats")
def detect_threats():
    processes = get_running_processes()
    detected = []

    for process in processes:
        alerts = analyze_process(process)

        for alert in alerts:
            process_name = alert["process"]

            cursor.execute(
                "SELECT count FROM threats WHERE process=?",
                (process_name,)
            )
            row = cursor.fetchone()

            if row:
                cursor.execute(
                    "UPDATE threats SET count = count + 1, last_seen=CURRENT_TIMESTAMP WHERE process=?",
                    (process_name,)
                )
            else:
                cursor.execute(
                    "INSERT INTO threats (type, severity, process, message) VALUES (?, ?, ?, ?)",
                    (alert["type"], alert["severity"], process_name, alert["message"])
                )

            conn.commit()
            detected.append(alert)

    return {
        "current_scan_threats": len(detected),
        "message": "Threat scan completed"
    }

#eat History API (Dashboard Ready)

@app.get("/threats/history")
def threat_history():
    cursor.execute("""
        SELECT process, type, severity, count, last_seen
        FROM threats
        ORDER BY last_seen DESC
    """)
    rows = cursor.fetchall()

    return [
        {
            "process": r[0],
            "type": r[1],
            "severity": r[2],
            "frequency": r[3],
            "last_seen": r[4]
        }
        for r in rows
    ]

#Severity Distribution API

@app.get("/analytics/severity")
def severity_analytics():
    cursor.execute("""
        SELECT severity, COUNT(*) 
        FROM threats
        GROUP BY severity
    """)
    rows = cursor.fetchall()

    return {
        row[0]: row[1] for row in rows
    }

#Top Risky Processes API

@app.get("/analytics/top-risky")
def top_risky_processes():
    cursor.execute("""
        SELECT process, severity, count
        FROM threats
        ORDER BY count DESC
        LIMIT 5
    """)
    rows = cursor.fetchall()

    return [
        {
            "process": r[0],
            "severity": r[1],
            "frequency": r[2]
        }
        for r in rows
    ]

#High Severity Incident Summary

@app.get("/analytics/incidents")
def incident_summary():
    cursor.execute("""
        SELECT process, message, last_seen
        FROM threats
        WHERE severity = 'High'
        ORDER BY last_seen DESC
    """)
    rows = cursor.fetchall()

    return [
        {
            "process": r[0],
            "incident": r[1],
            "last_seen": r[2]
        }
        for r in rows
    ]

#Alerts Feed API

@app.get("/alerts/live")
def live_alerts():
    cursor.execute("""
        SELECT process, severity, message, last_seen
        FROM threats
        WHERE severity IN ('Medium', 'High')
        ORDER BY last_seen DESC
        LIMIT 5
    """)
    rows = cursor.fetchall()

    return [
        {
            "process": r[0],
            "severity": r[1],
            "message": r[2],
            "time": r[3]
        }
        for r in rows
    ]


