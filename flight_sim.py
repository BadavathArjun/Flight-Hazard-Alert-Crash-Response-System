import random

def generate_flight_data():
    """
    Simulate a single set of flight data readings.
    Returns a dictionary with altitude (ft), speed (knots), g_force, and turbulence (bool).
    """
    return {
        "altitude": random.randint(5000, 35000),      # in feet
        "speed": random.randint(200, 600),            # in knots
        "g_force": round(random.uniform(0.8, 3.0), 1),# normal flight: ~1G
        "turbulence": random.choice([True, False])
    }

if __name__ == "__main__":
    # Print 5 sample data points
    for _ in range(5):
        print(generate_flight_data()) 