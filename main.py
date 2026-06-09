import os
import sys
import time
import random
import sqlite3

# تشخیص سیستم‌عامل برای شبیه‌سازی سخت‌افزار
try:
    import RPi.GPIO as GPIO
    IS_RASPBERRY_PI = True
except ImportError:
    IS_RASPBERRY_PI = False
    print("[INFO] Running on Non-Raspberry Pi system. Hardware simulation enabled.")

# تنظیمات پروژه
ALERT_THRESHOLD = 35.0  # دمای بحرانی برای هشدار
SAMPLING_RATE = 2       # فاصله زمانی خواندن سنسور (ثانیه)
DB_NAME = "system_logs.db"

def init_database():
    """
    ایجاد دیتابیس و جدول لوکال در صورت عدم وجود
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS temp_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            temperature REAL NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("[INFO] Database initialized successfully.")

def log_to_database(timestamp, temperature, status):
    """
    ذخیره یک رکورد جدید در دیتابیس SQLite
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO temp_logs (timestamp, temperature, status)
            VALUES (?, ?, ?)
        """, (timestamp, temperature, status))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"[❌ DB ERROR] Failed to write to database: {e}")

def read_temperature():
    """
    شبیه‌سازی خواندن دما از سنسور
    """
    if IS_RASPBERRY_PI:
        # کدهای سنسور واقعی اینجا قرار می‌گیرد
        return 25.0
    else:
        return round(random.uniform(20.0, 45.0), 2)

def trigger_alert(current_temp):
    """
    فعال کردن سیستم هشدار سخت‌افزاری/نرم‌افزاری
    """
    print(f"[🔥 ALERT] SYSTEM OVERHEATING! Temperature reached: {current_temp}°C")

def main():
    print("=" * 50)
    print("IoT Smart Temperature Monitoring System with SQLite")
    print("=" * 50)
    
    # راه‌اندازی اولیه دیتابیس
    init_database()
    
    try:
        while True:
            temp = read_temperature()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            
            # تعیین وضعیت برای دیتابیس
            if temp > ALERT_THRESHOLD:
                status = "ALERT"
                trigger_alert(temp)
            else:
                status = "NORMAL"
                
            print(f"[{current_time}] Temp: {temp}°C | Status: {status} -> Saving to DB...")
            
            # ذخیره در دیتابیس
            log_to_database(current_time, temp, status)
                
            time.sleep(SAMPLING_RATE)
            
    except KeyboardInterrupt:
        print("\n[INFO] Monitoring stopped by user.")
    finally:
        if IS_RASPBERRY_PI:
            GPIO.cleanup()
        print("[INFO] Cleanup complete. Goodbye!")

if __name__ == "__main__":
    main()