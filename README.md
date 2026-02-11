# 🛡️ CyberSentinel – AI Cyber Security Monitoring Tool

An AI-powered SOC-style cybersecurity monitoring system that analyzes real-time system processes, detects suspicious activities, aggregates threats by severity, and visualizes insights through a live interactive dashboard.

---

## 🚀 Overview

CyberSentinel is a full-stack security monitoring tool designed to simulate real-world Security Operations Center (SOC) behavior.

It:
- Monitors system processes in real time
- Detects suspicious behavior using rule-based logic
- Reduces alert noise via aggregation
- Displays insights in a live dashboard

This project demonstrates practical cybersecurity + full-stack development skills.

---

## ✨ Key Features

- 🔍 Real-time system monitoring  
- 🚨 Suspicious process detection  
- ⚠️ Severity classification (Low / Medium / High)  
- 📊 Live SOC-style dashboard  
- 🔄 Auto-refresh monitoring  
- 🔔 Live alerts panel  
- 📈 Threat frequency tracking  
- 📥 CSV threat report export  

---

## 🧠 System Architecture

System Monitor  
→ Threat Detection Engine  
→ SQLite Database  
→ FastAPI Analytics APIs  
→ React Dashboard  

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- SQLite
- psutil (System Monitoring)

### Frontend
- React.js
- Axios
- Recharts (Charts & Visualization)

---

## ⚙️ Installation & Setup

### 1. Clone Repository

git clone https://github.com/codewithakkii/ai-threat-detection-system.git  
cd ai-threat-detection-system  

---

### 2. Backend Setup

cd backend  
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
uvicorn main:app --reload  

Backend runs at:
http://127.0.0.1:8000  

---

### 3. Frontend Setup

cd frontend  
npm install  
npm start  

Dashboard runs at:
http://localhost:3000  

---

## 📊 Dashboard Capabilities

- Severity distribution analytics  
- Top risky processes tracking  
- Live security alerts  
- Auto refresh every 5 seconds  
- CSV report generation  

---

## 🎯 Use Case

- SOC monitoring simulation  
- Cybersecurity learning project  
- Resume / portfolio showcase  
- Security analytics demonstration  

---

## 🔐 Security Design Highlights

- False positives reduced via whitelist logic  
- Duplicate alert aggregation using frequency tracking  
- Severity-based threat grouping  
- Clean structured APIs for analytics  

---

## 📈 Future Improvements

- ML-based anomaly detection  
- Authentication & role-based access  
- Docker deployment  
- Cloud agent integration  
- Historical analytics charts  

---

## 💼 Resume Summary Line

Built an AI-powered cybersecurity monitoring tool that analyzes real-time system processes, detects suspicious behavior, aggregates threats by severity, and visualizes insights through a live SOC-style dashboard.

---

## 👨‍💻 Author

Developed by CodeWithAkki  
Cybersecurity & AI Enthusiast 🚀


