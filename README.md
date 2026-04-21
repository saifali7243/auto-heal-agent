# 🚀 Auto-Healing Infrastructure Agent

## 📌 Overview

The **Auto-Healing Infrastructure Agent** is a lightweight DevOps tool that monitors system health and automatically takes corrective actions when anomalies are detected.

It simulates real-world **Site Reliability Engineering (SRE)** practices by enabling systems to recover from failures without manual intervention.

---

## 🎯 Problem Statement

In production environments, system issues such as:

* High CPU usage
* Memory exhaustion
* Rogue processes

require manual debugging and intervention, leading to:

* Increased downtime
* Operational overhead
* Slower incident response

---

## 💡 Solution

This project implements a **self-healing agent** that:

1. Monitors system metrics in real time
2. Detects anomalies using rule-based logic
3. Identifies the root cause (top CPU-consuming process)
4. Applies safe remediation policies
5. Logs all actions for auditing
6. (Optional) Sends real-time alerts

---

## ⚙️ Features

* 📊 Real-time system monitoring (CPU, RAM, Disk)
* 🧠 Rule-based anomaly detection
* 🔍 Intelligent process identification
* 🔐 Safe auto-remediation (whitelist/blacklist)
* ⏳ Cooldown mechanism to prevent repeated actions
* 📝 Persistent logging
* 📲 Alerting support (Telegram-ready)

---

## 🧱 Architecture

```text
Monitor → Rules Engine → Decision Engine → Action Engine → Logging + Alerts
```

---

## 🛠️ Tech Stack

* Python
* psutil (system monitoring)
* YAML (config-driven rules)
* Logging module
* Requests (for alerts)

---

## 🚀 How to Run

### 1. Clone repo

```bash
git clone https://github.com/<your-username>/auto-heal-agent.git
cd auto-heal-agent
```

---

### 2. Setup virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure rules

Edit `config.yaml`:

```yaml
cpu_threshold: 85

safe_processes:
  - "ssh"
  - "systemd"
  - "python"

killable_processes:
  - "yes"
```

---

### 5. Run the agent

```bash
python main.py
```

---

## 🧪 Testing

Simulate high CPU usage:

```bash
yes > /dev/null &
yes > /dev/null &
```

The agent will:

* detect high CPU
* identify the process
* safely terminate it (if allowed)

---

## 📂 Logs

All actions are recorded in:

```bash
logs/system.log
```

---

## 🔐 Safety Features

* Whitelisted processes are never terminated
* Only explicitly allowed processes are killed
* Cooldown prevents repeated actions
* Config-driven behavior (no hardcoding)

---

## 📈 Future Improvements

* AI-based anomaly detection
* REST API (FastAPI)
* Dashboard (React)
* Docker support
* Kubernetes integration

---

## 💼 Use Case

This project demonstrates:

* DevOps automation
* Infrastructure monitoring
* Incident response systems
* SRE best practices

---

## 🧠 Author

Built as a hands-on DevOps + SRE project to simulate real-world infrastructure automation.

---
