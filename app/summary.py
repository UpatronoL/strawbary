from flask import Blueprint, render_template, current_app, flash
import pandas as pd
import os

bp = Blueprint('summary', __name__)  # Define Blueprint


@bp.route('/summary', methods=('GET',))
def summary_table():
    csv_file = os.path.join(current_app.root_path, 'data', 'measurements.csv')

    if not os.path.exists(csv_file):
        flash("Data file not found. Please upload data or generate measurements.", "danger")
        return render_template('summary/summary.html', summary=[])

    # Read and process the data
    df = pd.read_csv(csv_file)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M').dt.time

    grouped = df.groupby('Date')
    summary = []

    for date, group in grouped:
        # Define day and night time ranges
        daytime = group[(group['Time'] >= pd.to_datetime("06:00", format="%H:%M").time()) &
                        (group['Time'] < pd.to_datetime("18:00", format="%H:%M").time())]
        nighttime = group[(group['Time'] < pd.to_datetime("06:00", format="%H:%M").time()) |
                          (group['Time'] >= pd.to_datetime("18:00", format="%H:%M").time())]

        # Calculate statistics
        stats = {
                'Date': date,
                # Temperature
                'Max Temp': group['Temperature'].max(),
                'Min Temp': group['Temperature'].min(),
                'Daily Avg Temp': group['Temperature'].mean(),
                'Daytime Avg Temp': daytime['Temperature'].mean() if not daytime.empty else 0,
                'Nighttime Avg Temp': nighttime['Temperature'].mean() if not nighttime.empty else 0,
                # Soil Temp
                'Max Soil Temp': group['Soil Temp'].max(),
                'Min Soil Temp': group['Soil Temp'].min(),
                'Daily Avg Soil Temp': group['Soil Temp'].mean(),
                'Daytime Avg Soil Temp': daytime['Soil Temp'].mean() if not daytime.empty else 0,
                'Nighttime Avg Soil Temp': nighttime['Soil Temp'].mean() if not nighttime.empty else 0,
                # Humidity
                'Max Humidity': group['Humidity'].max(),
                'Min Humidity': group['Humidity'].min(),
                'Daily Avg Humidity': group['Humidity'].mean(),
                'Daytime Avg Humidity': daytime['Humidity'].mean() if not daytime.empty else 0,
                'Nighttime Avg Humidity': nighttime['Humidity'].mean() if not nighttime.empty else 0,
                # Soil Humidity
                'Max Soil Humidity': group['Soil Humidity'].max(),
                'Min Soil Humidity': group['Soil Humidity'].min(),
                'Daily Avg Soil Humidity': group['Soil Humidity'].mean(),
                'Daytime Avg Soil Humidity': daytime['Soil Humidity'].mean() if not daytime.empty else 0,
                'Nighttime Avg Soil Humidity': nighttime['Soil Humidity'].mean() if not nighttime.empty else 0,
                # Light Intensity
                'Max Light Intensity': group['Light Intensity'].max(),
                'Daily Avg Light Intensity': group['Light Intensity'].mean(),
                }
        summary.append(stats)

    return render_template('summary/summary.html', summary=summary)
