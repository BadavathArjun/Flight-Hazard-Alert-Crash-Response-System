import time
import random
from flight_sim import generate_flight_data
from hazard_detection import detect_hazards, check_crash
from visualization import plot_flight
from alert_system import AlertSystem

def main():
    print("🛩️  Flight Hazard Alert and Crash Response System")
    print("=" * 60)
    print("Real-Time Flight Hazard Detection and Automated Emergency Response")
    print("=" * 60)
    
    # Initialize alert system
    alert_sys = AlertSystem()
    
    # Simulation parameters
    flight_duration = 25  # time steps
    flight_data = []
    hazard_indices = []
    hazard_msgs = []
    
    print(f"Starting flight simulation for {flight_duration} time steps...")
    print("Monitoring: Altitude, Speed, G-Force, Turbulence")
    print("-" * 60)
    
    for t in range(flight_duration):
        # Generate flight data with aircraft registration
        data = generate_flight_data()
        data['registration'] = f"N{random.randint(10000, 99999)}"
        flight_data.append(data)
        
        # Detect hazards
        hazards = detect_hazards(data)
        if hazards:
            hazard_indices.append(t)
            hazard_msgs.append('; '.join(hazards))
            
            # Send appropriate alerts based on hazard severity
            for hazard in hazards:
                if "High G-Force" in hazard:
                    alert_sys.send_cockpit_warning(hazard, "WARNING")
                    alert_sys.send_ground_alert(data, hazard, "ALERT")
                elif "Low Altitude" in hazard:
                    alert_sys.send_cockpit_warning(hazard, "CAUTION")
                    alert_sys.send_ground_alert(data, hazard, "WARNING")
                elif "Turbulence" in hazard:
                    alert_sys.send_cockpit_warning(hazard, "ADVISORY")
        
        # Check for crash
        if check_crash(data):
            print(f"\n💥 CRASH DETECTED at time {t}!")
            alert_sys.send_emergency_alert(data)
            break
        
        # Print status every 5 time steps
        if t % 5 == 0:
            print(f"⏰ Time {t:2d}: Alt={data['altitude']:5d}ft, Speed={data['speed']:3d}kts, G={data['g_force']:3.1f}")
        
        time.sleep(0.2)  # Simulate real-time data
    
    print("-" * 60)
    print("Flight simulation completed!")
    print(f"Total hazards detected: {len(hazard_indices)}")
    
    # Show alert summary
    alert_sys.get_alert_summary()
    
    # Generate visualization
    print("\n📊 Generating flight monitoring visualization...")
    plot_flight(flight_data, hazard_indices, hazard_msgs)
    print("✅ System demonstration complete!")
    print("\n🎯 Key Features Demonstrated:")
    print("   • Real-time flight data monitoring")
    print("   • Automated hazard detection")
    print("   • Multi-level alert system (Cockpit, Ground, Emergency)")
    print("   • Crash detection with GPS coordinates")
    print("   • Visual flight monitoring dashboard")
    print("   • Integration with real FAA accident data")

if __name__ == "__main__":
    main() 