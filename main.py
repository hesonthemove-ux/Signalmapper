from flask import Flask, jsonify, render_template
import os
from core.hardware.satnav import SatNavEngine

app = Flask(__name__, template_folder='ui/templates')
nav = SatNavEngine()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/telemetry')
def telemetry():
    # Simulated position for testing Paisley Junction
    cur_lat, cur_lon = 55.8450, -4.4305 
    
    guidance = nav.check_position(cur_lat, cur_lon)
    
    return jsonify({
        "status": {"gnss": "green", "sdr": "green"},
        "pos": {"lat": cur_lat, "lon": cur_lon},
        "guidance": guidance,
        "rf": {"ber": "0.0001", "tii": "36:01"}
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
