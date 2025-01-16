import sys
from tabulate import tabulate
def load_driver_data():
    #function to extract data from first file
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

def process_lap_data(files):
    lap_data = {}
    track_name = None
    for filename in files:
        a=1
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                track_name = lines[0].strip() 
                print ("The track of Grand Prix",a," is: ",track_name)
                a=a+1
                for line in lines[1:]:
                    driver_code = line[:3]  
                    lap_time = float(line[3:].strip())  
                    if driver_code not in lap_data:
                        lap_data[driver_code] = []
                    lap_data[driver_code].append(lap_time)
        except FileNotFoundError:
            print(f"Lap data file '{filename}' not found.")
    
    return  lap_data


def display_results(drivers, lap_data):

    print("\n")
    #function to display the fastest lap and summary for each driver in a table format
    table_data=[]

    #printing data of each driver
    for code, times in lap_data.items():
        fastest_lap = min(times)
        average_time = sum(times) / len(times)
        total_laps = len(times)
        driver_info = drivers.get(code, {'name': 'Unknown', 'team': 'Unknown'})

        # Add each row of data to the table
        table_data.append([driver_info['name'], code, driver_info['team'], fastest_lap, average_time, total_laps])

    #printing the table with headers using tabulate
    headers = ['Driver Name', 'Code', 'Team', 'Fastest Lap (s)', 'Average Lap (s)', 'Total Laps']
    print(tabulate(table_data, headers=headers, tablefmt='fancy_grid', floatfmt=".3f")) #printing table with fancy grid style border and 3 digits float
    


if __name__ == "__main__":
    print("\n\n\n\n\t\t\t\t|=======================================================================|")
    print("\t\t\t\t|=================FORMULA 1 PRACTICE SESSION LAP========================|")
    print("\t\t\t\t|=======================================================================|\n\n")
    lap_files = ["lap_times_1.txt", "lap_times_2.txt", "lap_times_3.txt"]  # List of lap time files

    # Load driver data
    drivers = load_driver_data()

    # Process lap data from all files
    lap_data = process_lap_data(lap_files)

    # Display the results
    display_results(drivers, lap_data)
