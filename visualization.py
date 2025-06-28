import matplotlib.pyplot as plt
from flight_sim import generate_flight_data
from hazard_detection import detect_hazards


def plot_flight(flight_data, hazard_indices, hazard_msgs):
    """
    Plot altitude, speed, and g-force over time. Annotate detected hazards.
    """
    times = list(range(len(flight_data)))
    altitudes = [d['altitude'] for d in flight_data]
    speeds = [d['speed'] for d in flight_data]
    g_forces = [d['g_force'] for d in flight_data]

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(times, altitudes, label='Altitude (ft)')
    plt.ylabel('Altitude (ft)')
    for idx, msg in zip(hazard_indices, hazard_msgs):
        plt.annotate('⚠ ' + msg, (idx, altitudes[idx]), color='red', fontsize=8, rotation=15)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(times, speeds, label='Speed (knots)', color='orange')
    plt.ylabel('Speed (knots)')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(times, g_forces, label='G-Force', color='green')
    plt.ylabel('G-Force')
    plt.xlabel('Time Step')
    plt.legend()

    plt.tight_layout()
    plt.suptitle('Flight Monitoring System', fontsize=16, y=1.02)
    plt.savefig('flight_monitoring.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Flight monitoring plot saved as 'flight_monitoring.png'")


if __name__ == "__main__":
    # Simulate a flight with 30 time steps
    flight_data = []
    hazard_indices = []
    hazard_msgs = []
    for t in range(30):
        data = generate_flight_data()
        flight_data.append(data)
        hazards = detect_hazards(data)
        if hazards:
            hazard_indices.append(t)
            hazard_msgs.append('; '.join(hazards))
    plot_flight(flight_data, hazard_indices, hazard_msgs) 