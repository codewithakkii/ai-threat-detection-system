WINDOWS_SYSTEM_PROCESSES = [
    "system", "system idle process", "smss.exe", "csrss.exe",
    "wininit.exe", "services.exe", "lsass.exe", "svchost.exe",
    "explorer.exe", "dwm.exe", "winlogon.exe",
    "runtimebroker.exe", "conhost.exe", "dllhost.exe",
    "taskhostw.exe", "fontdrvhost.exe", "sihost.exe",
    "searchhost.exe", "searchindexer.exe",
    "msmpeng.exe", "securityhealthservice.exe",
    "ctfmon.exe", "applicationframehost.exe"
]

def analyze_process(process):
    alerts = []

    name = normalize_process_name(process["name"])

    if not name:
        return []

    cpu = process["cpu"]
    memory = process["memory"]

    # Ignore core system processes
    if name in WINDOWS_SYSTEM_PROCESSES:
        return alerts

    # Rule 1: High CPU abuse
    if cpu > 60:
        alerts.append({
            "type": "High CPU Usage",
            "severity": "High",
            "process": name,
            "message": f"{name} consuming excessive CPU ({cpu}%)"
        })

    # Rule 2: Suspicious memory usage
    elif memory > 35:
        alerts.append({
            "type": "High Memory Usage",
            "severity": "Medium",
            "process": name,
            "message": f"{name} consuming high memory ({memory}%)"
        })

    # Rule 3: Unknown non-system process
    else:
        alerts.append({
            "type": "Unknown Process",
            "severity": "Low",
            "process": name,
            "message": f"Unrecognized non-system process detected: {name}"
        })

    return alerts

def normalize_process_name(name):
    return (name or "").lower().strip()

