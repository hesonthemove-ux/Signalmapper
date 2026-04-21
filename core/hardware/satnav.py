import math
import subprocess

class SatNavEngine:
    def __init__(self):
        self.decision_points = {
            (55.8645, -4.2705): {"msg": "M8 M77 Interchange. Use Lanes 1 and 2.", "lanes": "|| [1] [2] | 3 4 5"},
            (55.8450, -4.4300): {"msg": "M8 Junction 29. Keep left for A737 Irvine.", "lanes": "[1] | 2 3"}
        }
        self.last_announced = None
        self.last_signal_alert = 0 # Timestamp or state

    def speak(self, text):
        try:
            # -p 40 makes it slightly faster for driving
            subprocess.Popen(['espeak', '-v', 'en-scottish', '-p', '40', text])
        except:
            pass

    def monitor_signal(self, ber, block):
        """Announces if signal quality drops below audit thresholds."""
        # BER > 0.02 is usually where audio starts to bubble/cut
        if ber > 0.02:
            self.speak(f"Alert. Signal degradation detected on Block {block}. Check alignment.")
            return True
        return False

    def check_position(self, current_lat, current_lon):
        for point, data in self.decision_points.items():
            dist = math.sqrt((current_lat-point[0])**2 + (current_lon-point[1])**2) * 69
            if dist < 0.15:
                if self.last_announced != point:
                    self.speak(data['msg'])
                    self.last_announced = point
                    return data
        return None
