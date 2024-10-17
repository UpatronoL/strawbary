
import csv
from random import uniform, randint
from datetime import datetime, timedelta

csv_filename = "measurements.csv"

# Number of readings
num_readings = 10000

# Interval of 5 minutes
interval_minutes = 5

# Start date and time
start_datetime = datetime.today()

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["Date", "Time", "Temperature", "Humidity", "Light Intensity", "Ground Temperature", "Ground Humidity"])

    for i in range(num_readings):
        current_datetime = start_datetime - timedelta(minutes=i*interval_minutes)

        temperature = round(uniform(20.0, 30.0), 1)
        humidity = round(uniform(40.0, 70.0), 1)
        light_intensity = randint(200, 800)
        ground_temperature = round(uniform(0.0, 20.0), 1)
        ground_humidity = round(uniform(20.0, 60.0), 1)

        writer.writerow([current_datetime.strftime('%Y-%m-%d'), 
                         current_datetime.strftime('%H:%M'), 
                         temperature, humidity, light_intensity, ground_temperature, ground_humidity])

print(f"CSV file '{csv_filename}' created with {num_readings} readings every {interval_minutes} minutes.")
