import sqlite3
import pandas as pd

def generate_compliance_report():
    conn = sqlite3.connect('data/devices.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM devices')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['Device ID', 'User Name', 'OS Version', 'Manufacturer', 'Model', 'Last Seen'])
    conn.close()

    # Example compliance check: devices with unknown OS version
    non_compliant_devices = df[df['OS Version'] == 'Unknown']

    report = f"Compliance Report:\n\nTotal Devices: {len(df)}\nNon-Compliant Devices: {len(non_compliant_devices)}\n\n"
    report += non_compliant_devices.to_string(index=False)

    return report
