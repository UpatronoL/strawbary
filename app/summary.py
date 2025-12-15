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
                # Humidity
                'Max Humidity': group['Humidity'].max(),
                'Min Humidity': group['Humidity'].min(),
                'Daily Avg Humidity': group['Humidity'].mean(),
                'Daytime Avg Humidity': daytime['Humidity'].mean() if not daytime.empty else 0,
                'Nighttime Avg Humidity': nighttime['Humidity'].mean() if not nighttime.empty else 0,
                # Light Intensity
                'Max Light Intensity': group['Light Intensity'].max(),
                'Daily Avg Light Intensity': group['Light Intensity'].mean(),
                # Ground Temperature
                'Max Ground Temp': group['Ground Temperature'].max(),
                'Min Ground Temp': group['Ground Temperature'].min(),
                'Daily Avg Ground Temp': group['Ground Temperature'].mean(),
                'Daytime Avg Ground Temp': daytime['Ground Temperature'].mean() if not daytime.empty else 0,
                'Nighttime Avg Ground Temp': nighttime['Ground Temperature'].mean() if not nighttime.empty else 0,
                # Ground Humidity
                'Max Ground Humidity': group['Ground Humidity'].max(),
                'Min Ground Humidity': group['Ground Humidity'].min(),
                'Daily Avg Ground Humidity': group['Ground Humidity'].mean(),
                'Daytime Avg Ground Humidity': daytime['Ground Humidity'].mean() if not daytime.empty else 0,
                'Nighttime Avg Ground Humidity': nighttime['Ground Humidity'].mean() if not nighttime.empty else 0,
                }
        summary.append(stats)

    return render_template('summary/summary.html', summary=summary)
