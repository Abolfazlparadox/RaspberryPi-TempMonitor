# IoT Smart Temperature Monitoring System 🌡️

A cross-platform Python application designed to simulate and monitor IoT temperature sensors. It dynamically detects the hardware environment (Raspberry Pi / General OS) and logs data locally using SQLite.

## 🚀 Features
- **Cross-Platform Execution:** Automatically detects if it's running on a Raspberry Pi (`RPi.GPIO`) or a Windows/Linux machine (Mock Simulation).
- **Local Data Persistence:** Uses `SQLite3` to safely log temperature states without relying on external database servers.
- **Event-Driven Alerts:** Real-time console alerts when temperature exceeds the defined safety threshold.
- **Graceful Shutdown:** Ensures hardware pins are properly released (`GPIO.cleanup()`) upon exit.

## 🛠️ Technologies Used
- Python 3.x
- SQLite3
- RPi.GPIO (For Raspberry Pi deployment)

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Abolfazlparadox/RaspberryPi-TempMonitor.git](https://github.com/Abolfazlparadox/RaspberryPi-TempMonitor.git)
   cd RaspberryPi-TempMonitor
   Create and activate a virtual environment:
Create and activate a virtual environment:
Bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/Mac:
source .venv/bin/activate
Run the application:

Bash
python main.py
Note: If executed on a non-Raspberry Pi system, the application will automatically enter hardware simulation mode.