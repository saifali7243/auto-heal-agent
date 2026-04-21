# 🚀 Auto-Heal Agent — Self-Healing Infrastructure Tool

## 📌 Overview

**Auto-Heal Agent** is a lightweight, policy-driven DevOps tool that monitors system health and automatically remediates issues in real time.

It simulates real-world **Site Reliability Engineering (SRE)** practices by enabling systems to detect anomalies and take corrective actions without manual intervention.

---

## 🎯 Problem

In production systems, issues like:

* High CPU usage
* Memory pressure
* Rogue or runaway processes

often require manual debugging and intervention, leading to:

* Increased downtime
* Slow incident response
* Operational overhead

---

## 💡 Solution

This project implements a **self-healing agent** that:

1. Continuously monitors system metrics
2. Detects anomalies using rule-based logic
3. Identifies the root cause (top CPU-consuming process)
4. Applies **safe, policy-based remediation**
5. Logs all actions for observability
6. Runs as a containerized service

---

## ⚙️ Features

* 📊 Real-time monitoring (CPU, RAM, Disk)
* 🧠 Rule-based anomaly detection
* 🔍 Intelligent process identification
* 🔐 Safe remediation with:

  * `critical_processes` (never touched)
  * `safe_processes` (protected)
  * `killable_processes` (allowed)
* ⏳ Cooldown mechanism (prevents repeated kills)
* 📝 Persistent logging (`logs/system.log`)
* 🔄 Dynamic config reload (no restart required)
* 🐳 Dockerized deployment
* ⚙️ systemd service support

---

## 🧱 Architecture

```text
Monitor → Rules Engine → Decision Engine → Action Engine → Logging
```

---

## 🛠️ Tech Stack

* Python
* psutil
* YAML (config-driven rules)
* Docker
* systemd

---

## 🚀 Getting Started

### 1. Clone repository

```bash
git clone git@github.com:saifali7243/auto-heal-agent.git
cd auto-heal-agent
```

---

### 2. Setup environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Configure rules

Edit `config.yaml`:

```yaml
cpu_threshold: 85

safe_processes:
  - "ssh"
  - "systemd"
  - "python"

killable_processes:
  - "yes"

critical_processes:
  - "nginx"
  - "postgres"
  - "docker"
```

---

### 4. Run locally

```bash
python main.py
```

---

## 🐳 Run with Docker

```bash
docker build -t auto-heal-agent .
docker run -it --pid=host --privileged auto-heal-agent
```

---

## ⚙️ Run as systemd service

```bash
sudo systemctl enable auto-heal
sudo systemctl start auto-heal
```

---

## 🧪 Testing

Simulate high CPU load:

```bash
yes > /dev/null &
yes > /dev/null &
```

The agent will:

* detect spike
* identify process
* apply safe action

---

## 📂 Logs

```bash
logs/system.log
```

Tracks:

* detected issues
* actions taken
* skipped processes

---

## 🔐 Safety Design

The system follows strict safety policies:

* Never kills critical system services
* Only terminates explicitly allowed processes
* Uses cooldown to prevent instability
* Fully configurable via YAML

---

## 📈 Future Improvements

* Prometheus metrics endpoint
* Grafana dashboard
* AI-based anomaly detection
* Kubernetes integration
* REST API (FastAPI)

---

## 💼 What This Project Demonstrates

* DevOps automation
* Infrastructure monitoring
* Incident response systems
* Safe remediation design
* Containerized deployment
* SRE thinking

---

## 🧠 Author

Built as a practical DevOps + SRE project to simulate real-world infrastructure automation.

---
