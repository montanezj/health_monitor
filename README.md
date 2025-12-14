# 🏥 Real-Time Server Health Monitoring System

![CI Status](https://github.com/montanezj/health_monitor/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-orange)
![Kafka](https://img.shields.io/badge/Apache-Kafka-black)

## 📖 Project Overview
This project is a full-stack **Event-Driven Architecture** designed to simulate, ingest, store, and visualize real-time server metrics (CPU usage and Temperature).

It demonstrates a complete **DevOps lifecycle**:
1.  **Ingestion:** Python producers generate synthetic data.
2.  **Streaming:** Apache Kafka acts as the message broker to decouple services.
3.  **Processing:** A consumer service ingests data and writes to PostgreSQL.
4.  **Visualization:** Grafana dashboards provide real-time observability.
5.  **Automation:** GitHub Actions handles CI testing on every push.

---

## 🏗 Architecture
**Producer** (Python) ➡️ **Kafka** (Zookeeper) ➡️ **Consumer** (Python) ➡️ **PostgreSQL** ➡️ **Grafana**

* **Producer:** Simulates IoT sensors/server agents.
* **Kafka:** Handles high-throughput message streaming.
* **PostgreSQL:** Persists historical data for trend analysis.
* **Grafana:** Visualizes metrics with SQL-based time-series queries.
* **Docker Compose:** Orchestrates the entire multi-container environment.

---

## 📸 Dashboard Preview
*(Replace this line with your screenshot: `![Dashboard](dashboard.png)`)*

---

## 🛠 Tech Stack
* **Languages:** Python 3.12
* **Containerization:** Docker, Docker Compose
* **Message Broker:** Apache Kafka, Zookeeper
* **Database:** PostgreSQL 15
* **Visualization:** Grafana
* **CI/CD:** GitHub Actions (Flake8 Linting, Docker Config Validation)

---

## 🚀 How to Run locally

### Prerequisites
* Docker Desktop installed
* Git installed

### 1. Clone the Repository
```bash
git clone [https://github.com/montanezj/health_monitor.git](https://github.com/montanezj/health_monitor.git)
cd health_monitor