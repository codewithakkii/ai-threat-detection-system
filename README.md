🛡️ CyberSentinel – AI Cyber Security Monitoring Tool

A SOC-style AI-powered cybersecurity monitoring system that analyzes real-time system processes, detects suspicious activity, aggregates threats by severity, and visualizes insights through a live interactive dashboard.

🚀 Overview

CyberSentinel is a full-stack security monitoring tool built to simulate real-world SOC (Security Operations Center) behavior.
It monitors system processes, detects abnormal activity using rule-based logic, reduces alert noise through aggregation, and presents security insights in a live dashboard.

This project demonstrates practical cybersecurity monitoring concepts combined with modern web technologies.

✨ Features

🔍 Real-time system process monitoring

🚨 Suspicious activity detection

⚠️ Severity-based threat classification (Low / Medium / High)

📊 SOC-style live dashboard

🔄 Auto-refresh monitoring

🔔 Live alerts panel

📈 Threat frequency aggregation

📥 CSV report export

📦 Clean GitHub-ready project structure

🧠 How It Works
System Monitor
      ↓
Threat Detection Engine
      ↓
SQLite Threat Database
      ↓
FastAPI Analytics APIs
      ↓
React SOC Dashboard


The backend collects system process data using Python.

Suspicious behavior is detected via rule-based logic.

Threats are stored and aggregated in a SQLite database.

Severity analytics APIs provide structured insights.

A React dashboard visualizes security metrics in real time.

🛠 Tech Stack
Backend

Python

FastAPI

SQLite

psutil (System Monitoring)

Frontend

React.js

Axios

Recharts (Data Visualization)

📂 Project Structure
ai-threat-detection-system/
│
├── backend/
│   ├── main.py
│   ├── detectors/
│   ├── monitors/
│   └── database/
│
├── frontend/
│   ├── src/
│   ├── components/
│   └── api.js
│
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/ai-threat-detection-system.git
cd ai-threat-detection-system

2️⃣ Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000

3️⃣ Frontend Setup
cd frontend
npm install
npm start


Dashboard runs at:

http://localhost:3000

📊 Dashboard Capabilities

Severity distribution analytics

Top risky processes tracking

Live security alerts

Automated periodic refresh

Downloadable threat reports

🎯 Use Cases

Learning SOC monitoring concepts

Demonstrating cybersecurity skills

Resume & portfolio project

Security analytics practice

🔐 Security Design Notes

False positives reduced using whitelist logic

Threats aggregated by process frequency

Real-time refresh simulates SOC monitoring

Local backend ensures system-level access

📈 Future Improvements

Machine learning anomaly detection

Authentication & role-based access

Docker deployment

Cloud-hosted monitoring agent

Historical trend analytics

💼 Resume Highlight

Built an AI-powered cybersecurity monitoring system that analyzes real-time system processes, detects suspicious activities, aggregates threats by severity, and visualizes insights through a live SOC-style dashboard.

📄 License

This project is built for educational and demonstration purposes.

👨‍💻 Author

Developed by CodeWithAkki
Cybersecurity & AI Enthusiast 🚀

If you want to contribute, suggest improvements, or provide feedback — feel free to open an issue.
