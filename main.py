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
    # Simulation: Near Paisley with a failing signal
    cur_lat, cur_lon = 55.8450, -4.4305
    cur_ber = 0.05 
    cur_block = "10C"
    
    # 1. Check for Motorway Lane Guidance
    guidance = nav.check_position(cur_lat, cur_lon)
    
    # 2. Check for Signal Strength Alerts
    nav.monitor_signal(cur_ber, cur_block)
    
    return jsonify({
        "status": {"gnss": "green", "sdr": "green"},
        "pos": {"lat": cur_lat, "lon": cur_lon},
        "guidance": guidance,
        "rf": {"ber": cur_ber, "block": cur_block, "tii": "36:01"}
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
