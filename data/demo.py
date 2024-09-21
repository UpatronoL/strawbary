import csv
from random import uniform, randint
from datetime import datetime, timedelta

csv_filename = "measurements.csv"

num_days = 200

start_date = datetime.today()

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["Date", "Temperature", "Humidity", "Light Intensity"])

    for i in range(num_days):
        current_date = start_date - timedelta(days=i)

        temperature = round(uniform(20.0, 30.0), 1)
        humidity = round(uniform(40.0, 70.0), 1)
        light_intensity = randint(200, 800)

        writer.writerow([current_date.strftime('%Y-%m-%d'), temperature, humidity, light_intensity])

print(f"CSV file '{csv_filename}' created with {num_days} days of simulated data.")
