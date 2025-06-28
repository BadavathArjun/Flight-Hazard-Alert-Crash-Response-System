import random
from datetime import datetime

class AlertSystem:
    def __init__(self):
        self.alert_history = []
    
    def send_cockpit_warning(self, hazard_msg, severity="WARNING"):
        """Simulate cockpit warning display"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"🛩️  COCKPIT {severity} [{timestamp}]: {hazard_msg}")
        self.alert_history.append({
            "type": "cockpit",
            "severity": severity,
            "message": hazard_msg,
            "timestamp": timestamp
        })
    
    def send_ground_alert(self, data, hazard_msg, severity="ALERT"):
        """Simulate ground control alert"""
        lat = random.uniform(0, 90)
        lon = random.uniform(0, 180)
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"🏢 GROUND {severity} [{timestamp}]: Aircraft {data.get('registration', 'N12345')}")
        print(f"   Location: {lat:.4f}°N, {lon:.4f}°E")
        print(f"   Issue: {hazard_msg}")
        self.alert_history.append({
            "type": "ground",
            "severity": severity,
            "message": hazard_msg,
            "location": (lat, lon),
            "timestamp": timestamp
        })
    
    def send_emergency_alert(self, data):
        """Simulate emergency crash alert"""
        lat = random.uniform(0, 90)
        lon = random.uniform(0, 180)
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"🚨 EMERGENCY CRASH ALERT [{timestamp}]!")
        print(f"   Aircraft: {data.get('registration', 'N12345')}")
        print(f"   Location: {lat:.4f}°N, {lon:.4f}°E")
        print(f"   Altitude: {data['altitude']} ft")
        print(f"   Speed: {data['speed']} knots")
        print(f"   G-Force: {data['g_force']}")
        print("   🚁 Search & Rescue teams dispatched!")
        print("   📞 Emergency contacts notified!")
        
        self.alert_history.append({
            "type": "emergency",
            "severity": "CRITICAL",
            "message": "CRASH DETECTED",
            "location": (lat, lon),
            "data": data,
            "timestamp": timestamp
        })
    
    def get_alert_summary(self):
        """Return summary of all alerts"""
        print(f"\n📊 Alert Summary:")
        print(f"   Total alerts: {len(self.alert_history)}")
        cockpit_alerts = len([a for a in self.alert_history if a["type"] == "cockpit"])
        ground_alerts = len([a for a in self.alert_history if a["type"] == "ground"])
        emergency_alerts = len([a for a in self.alert_history if a["type"] == "emergency"])
        print(f"   Cockpit warnings: {cockpit_alerts}")
        print(f"   Ground alerts: {ground_alerts}")
        print(f"   Emergency alerts: {emergency_alerts}")

if __name__ == "__main__":
    # Test the alert system
    alert_sys = AlertSystem()
    
    # Simulate some alerts
    alert_sys.send_cockpit_warning("Turbulence detected", "WARNING")
    alert_sys.send_ground_alert({"registration": "N12345"}, "High G-force detected", "ALERT")
    alert_sys.send_emergency_alert({
        "registration": "N12345",
        "altitude": 500,
        "speed": 400,
        "g_force": 6.0
    })
    
    alert_sys.get_alert_summary() 