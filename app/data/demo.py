import csv
from random import uniform, randint
from datetime import datetime, timedelta
import pytz  
import os  

# Time zone: Japan Standard Time (UTC+9)
jst = pytz.timezone('Asia/Tokyo')

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)


csv_filename = os.path.join(data_dir, "measurements.csv")

# Number of readings for 8 days
num_readings = 7 * 24 * 12  

interval_minutes = 5

start_datetime = (datetime.now(jst) - timedelta(days=6)).replace(hour=0, minute=0, second=0, microsecond=0)

# Generate CSV
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    
    writer.writerow(["Date", "Time", "Temperature", "Soil Temp", "Humidity", "Soil Humidity", "Light Intensity"])

    for i in range(num_readings):
        current_datetime = start_datetime + timedelta(minutes=i * interval_minutes)

        # Generate data
        temperature = round(uniform(20.0, 30.0), 1)  # Air temperature in °C
        humidity = round(uniform(40.0, 70.0), 1)     # Air humidity in %
        light_intensity = randint(200, 800)          # Light intensity in lux
        ground_temperature = round(uniform(0.0, 20.0), 1)  # Ground temperature in °C
        ground_humidity = round(uniform(20.0, 60.0), 1)     # Ground humidity in %

        #  row to the CSV
        writer.writerow([current_datetime.strftime('%Y-%m-%d'),
                         current_datetime.strftime('%H:%M'),
                         temperature, ground_temperature, humidity, ground_humidity, light_intensity])

print(f"CSV file '{csv_filename}' created with {num_readings} readings every {interval_minutes} minutes.")
