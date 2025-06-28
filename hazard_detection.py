def detect_hazards(data):
    """
    Analyze flight data and return a list of detected hazards.
    """
    hazards = []
    if data["g_force"] > 2.5:
        hazards.append("High G-Force! Possible collision risk.")
    if data["altitude"] < 3000 and data["speed"] > 250:
        hazards.append("Low Altitude & High Speed! Terrain risk.")
    if data["turbulence"]:
        hazards.append("Turbulence detected! Advise altitude change.")
    return hazards

def check_crash(data):
    """
    Return True if crash conditions are detected, else False.
    """
    return data["g_force"] > 5.0 or data["altitude"] < 1000

if __name__ == "__main__":
    # Example usage with sample data
    sample_data = {
        "altitude": 900,
        "speed": 300,
        "g_force": 5.5,
        "turbulence": True
    }
    print("Sample Data:", sample_data)
    print("Hazards Detected:", detect_hazards(sample_data))
    print("Crash Detected:", check_crash(sample_data)) 