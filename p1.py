import sys

# Function to read the file and extract race data
def read_race_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

    # First line is the race location
    race_location = lines[0].strip()

    # Remaining lines are lap data
    lap_data = {}
    for line in lines[1:]:
        code = line[:3]
        time = float(line[4:].strip())
        if code not in lap_data:
            lap_data[code] = []
        lap_data[code].append(time)
    
    return race_location, lap_data

# Function to find the fastest lap and driver
def find_fastest_driver(lap_data):
    fastest_time = float('inf')
    fastest_driver = None
    for driver, times in lap_data.items():
        best_time = min(times)
        if best_time < fastest_time:
            fastest_time = best_time
            fastest_driver = driver
    return fastest_driver, fastest_time

# Function to calculate average times for all drivers
def calculate_averages(lap_data):
    averages = {}
    for driver, times in lap_data.items():
        averages[driver] = sum(times) / len(times)
    return averages

# Main function
def main():
    # Check if file name is provided
    if len(sys.argv) < 2:
        print("Usage: python timings_board.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]

    # Read the race data
    race_location, lap_data = read_race_file(file_name)

    # Find the fastest driver
    fastest_driver, fastest_time = find_fastest_driver(lap_data)

    # Calculate averages
    averages = calculate_averages(lap_data)
    overall_avg = sum([sum(times) for times in lap_data.values()]) / sum([len(times) for times in lap_data.values()])

    # Print results
    print(f"Race Location: {race_location}")
    print(f"Fastest Driver: {fastest_driver} with a time of {fastest_time:.3f}")
    print("\nDriver Times:")
    for driver, times in lap_data.items():
        print(f"{driver}: Fastest = {min(times):.3f}, Average = {averages[driver]:.3f}")
    print(f"\nOverall Average Time: {overall_avg:.3f}")

if __name__ == "__main__":
    main()
