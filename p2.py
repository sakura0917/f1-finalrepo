def load_driver_data():
    """Load driver data from the first file."""
    drivers = {}
    try:
        with open("f1_drivers.txt", 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    code = parts[1].strip()
                    name = parts[2].strip()
                    team = parts[3].strip()
                    drivers[code] = {'name': name, 'team': team}
    except FileNotFoundError:
        print("Driver file not found.")
    return drivers


def process_lap_data():
    """Process lap data from the second file."""
    lap_data = {}
    track_name = None
    try:
        with open("lap_times_1.txt", 'r') as file:
            lines = file.readlines()
            track_name = lines[0].strip()  # Track name is the first line
            for line in lines[1:]:
                driver_code = line[:3]  # Extract the driver code
                lap_time = float(line[3:].strip())  # Extract the lap time
                if driver_code not in lap_data:
                    lap_data[driver_code] = []
                lap_data[driver_code].append(lap_time)
    except FileNotFoundError:
        print("Lap data file not found.")
    return track_name, lap_data


def display_results(drivers, track_name, lap_data):
    """Display the fastest lap and summary for each driver."""
    print(f"Track: {track_name}")
    print("-" * 40)

    for code, times in lap_data.items():
        fastest_lap = min(times)
        average_time = sum(times) / len(times)
        total_laps = len(times)
        driver_info = drivers.get(code, {'name': 'Unknown', 'team': 'Unknown'})

        print(f"Driver: {driver_info['name']} ({code}) from {driver_info['team']}")
        print(f"- Fastest Lap: {fastest_lap:.3f} seconds")
        print(f"- Average Lap: {average_time:.3f} seconds")
        print(f"- Total Laps: {total_laps}")
        print()


# Main execution
if __name__ == "__main__":
    driver_file = "drivers.txt"  # Replace with the actual driver file name
    lap_data_file = "lap_times.txt"  # Replace with the actual lap data file name

    drivers = load_driver_data()
    track_name, lap_data = process_lap_data()

    display_results(drivers, track_name, lap_data) 