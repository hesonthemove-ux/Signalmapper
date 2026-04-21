import math
import subprocess

class SatNavEngine:
    def __init__(self):
        # Decision points: (Lat, Lon) : {Instruction, Lanes}
        self.decision_points = {
            (55.8645, -4.2705): {
                "msg": "M8 M77 Interchange. Use Lanes 1 and 2 for Kilmarnock.",
                "lanes": "|| [1] [2] | 3 4 5",
                "audit_note": "Glasgow Edge Zone."
            },
            (55.8450, -4.4300): {
                "msg": "M8 Junction 29. Keep left for A737 Irvine.",
                "lanes": "[1] | 2 3",
                "audit_note": "Paisley 10C Primary."
            }
        }
        self.last_announced = None

    def speak(self, text):
        try:
            subprocess.Popen(['espeak', '-v', 'en-scottish', text])
        except:
            pass

    def check_position(self, current_lat, current_lon):
        for point, data in self.decision_points.items():
            dist = math.sqrt((current_lat-point[0])**2 + (current_lon-point[1])**2) * 69
            if dist < 0.15: # ~250 meters
                if self.last_announced != point:
                    self.speak(data['msg'])
                    self.last_announced = point
                    return data
        return None
