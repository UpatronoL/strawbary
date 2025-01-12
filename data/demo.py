import csv
from random import uniform, randint
from datetime import datetime, timedelta
import pytz  # For time zone handling

# Time zone: Japan Standard Time (UTC+9)
jst = pytz.timezone('Asia/Tokyo')

# CSV file name
csv_filename = "measurements.csv"

# Number of readings for 8 days
num_readings = 20 * 24 * 12  # 8 days * 24 hours * 12 readings per hour (every 5 minutes)

# Interval of 5 minutes
interval_minutes = 5

# Start date and time (tomorrow at midnight in JST)
start_datetime = (datetime.now(jst) + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)

# Generate CSV
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write header
    writer.writerow(["Date", "Time", "Temperature", "Humidity", "Light Intensity", "Ground Temperature", "Ground Humidity"])

    # Generate data for each interval
    for i in range(num_readings):
        # Current timestamp (subtract intervals from the start time)
        current_datetime = start_datetime - timedelta(minutes=i * interval_minutes)

        # Generate random data
        temperature = round(uniform(20.0, 30.0), 1)  # Air temperature in °C
        humidity = round(uniform(40.0, 70.0), 1)     # Air humidity in %
        light_intensity = randint(200, 800)          # Light intensity in lux
        ground_temperature = round(uniform(0.0, 20.0), 1)  # Ground temperature in °C
        ground_humidity = round(uniform(20.0, 60.0), 1)     # Ground humidity in %

        # Write the row to the CSV
        writer.writerow([current_datetime.strftime('%Y-%m-%d'),
                         current_datetime.strftime('%H:%M'),
                         temperature, humidity, light_intensity, ground_temperature, ground_humidity])

print(f"CSV file '{csv_filename}' created with {num_readings} readings every {interval_minutes} minutes.")
