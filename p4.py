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

filenames=["lap_times_1.txt","lap_times_2.txt","lap_times_3.txt"]
def process_lap_data(filenames):
    """Process lap data from multiple lap times files."""
    lap_data = {}
    track_name = None
    for filename in filenames:
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if track_name is None:
                    track_name = lines[0].strip()  # Track name is the first line of the first file

                for line in lines[1:]:
                    driver_code = line[:3]  # Extract the driver code
                    lap_time = float(line[3:].strip())  # Extract the lap time
                    if driver_code not in lap_data:
                        lap_data[driver_code] = []
                    lap_data[driver_code].append(lap_time)
        except FileNotFoundError:
            print(f"Lap data file '{filename}' not found.")
    
    return track_name, lap_data


'''def display_results(drivers, track_name, lap_data):
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
        print()'''
def display_results(drivers, track_name, lap_data):
    """Display the fastest lap and summary for each driver in a manual table format."""
    print(f"\nTrack: {track_name}")
    print("-" * 92)

    # Print table headers
    headers = f"{'Driver Name':<20}{'Code':<8}{'Team':<20}{'Fastest Lap (s)':<17}{'Average Lap (s)':<17}{'Total Laps':<10}"
    print(headers)
    print("-" * 92)

    # Print driver data
    for code, times in lap_data.items():
        fastest_lap = min(times)
        average_time = sum(times) / len(times)
        total_laps = len(times)
        driver_info = drivers.get(code, {'name': 'Unknown', 'team': 'Unknown'})

        print(f"{driver_info['name']:<20}{code:<8}{driver_info['team']:<20}{fastest_lap:<17.3f}{average_time:<17.3f}{total_laps:<10}")

    print("-" * 92)



# Main execution
if __name__ == "__main__":
    driver_file = "f1_drivers.txt"  # Replace with the actual driver file name
    lap_data_files = ["lap_times_1.txt", "lap_times_2.txt", "lap_times_3.txt"]  # List of lap time files

    # Load driver data
    drivers = load_driver_data()

    # Process lap data from all files
    track_name, lap_data = process_lap_data(lap_data_files)

    # Display the results
    display_results(drivers, track_name, lap_data)
