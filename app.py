from flask import Flask, render_template, jsonify
import os, csv

app = Flask(__name__)

def load_ofcom():
    sites = []
    path = os.path.expanduser('~/Signalmapper_Project/data/ofcom_tx.csv')
    if os.path.exists(path):
        with open(path, 'r', encoding='latin-1') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Filter for DAB/SSDAB in the Ensemble or Site name
                if 'DAB' in str(row).upper():
                    try:
                        sites.append({
                            "name": row.get('Site Name', 'Unknown'),
                            "lat": float(row.get('Latitude', 0)),
                            "lon": float(row.get('Longitude', 0)),
                            "block": row.get('Block', 'N/A'),
                            "ensemble": row.get('Ensemble', 'N/A')
                        })
                    except: continue
    return sites

@app.route('/api/telemetry')
def telemetry():
    gnss_path = '/dev/ttyUSB0'
    # Check for GNSS connection
    gnss_status = "green" if os.path.exists(gnss_path) else "red"
    return jsonify({
        "status": {"gnss": gnss_status, "sdr": "green"},
        "pos": {"lat": 55.8642, "lon": -4.2518}, # Hardware logic for NMEA goes here
        "tx_data": load_ofcom()
    })

@app.route('/')
def index():
    return "SignalMapper Pro: Backend Active. Use Mission Control UI."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
