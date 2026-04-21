from flask import Flask, render_template, jsonify
import os
from core.gis.proximity_filter import ProximityFilter

app = Flask(__name__, template_folder='ui/templates')

@app.route('/api/telemetry')
def telemetry():
    gnss_alive = os.path.exists('/dev/ttyUSB0')
    return jsonify({
        "status": {"gnss": "green" if gnss_alive else "red", "sdr": "green"},
        "gnss": {"lat": 55.8642, "lon": -4.2518, "sats": 12, "lock": "3D"},
        "rf": {"ber": "0.0001", "tii": "36:01", "block": "10B"}
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
