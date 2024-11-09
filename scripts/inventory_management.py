import sqlite3
import pandas as pd

def get_device_inventory():
    conn = sqlite3.connect('data/devices.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM devices')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Device ID', 'User Name', 'OS Version', 'Manufacturer', 'Model', 'Last Seen'])
    conn.close()
    return df
