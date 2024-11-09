import sqlite3
from datetime import datetime

def enroll_device(device_id, user_name):
    conn = sqlite3.connect('data/devices.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO devices (device_id, user_name, os_version, manufacturer, model, last_seen)
        VALUES (?, ?, 'Unknown', 'Unknown', 'Unknown', ?)
    ''', (device_id, user_name, datetime.now()))
    conn.commit()
    conn.close()

def lock_device(device_id):
    # Add your code to lock the device here
    pass

def wipe_device(device_id):
    # Add your code to wipe the device here
    pass
