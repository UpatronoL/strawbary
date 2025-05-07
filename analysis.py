import matplotlib.pyplot as plt
from flask import Blueprint, render_template, current_app
import pandas as pd
import os
import io
import base64
from datetime import datetime
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend for Flask

bp = Blueprint('analysis', __name__, url_prefix='/analysis')


@bp.route('/', methods=['GET'])
def analysis():
    # Load CSV file
    csv_file = os.path.join(current_app.root_path, 'data', 'measurements.csv')
    graphs = {}
    if not os.path.exists(csv_file):
        return render_template('analysis/analysis.html', error="Data file not found.", graphs=graphs)
    data = pd.read_csv(csv_file)

    # Ensure numeric columns are properly converted
    numeric_cols = ['Temperature', 'Humidity', 'Light Intensity', 'Ground Temperature', 'Ground Humidity']
    data[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # Drop rows with missing values in numeric columns
    data = data.dropna(subset=numeric_cols)

    # Combine 'Date' and 'Time' into a datetime column
    data['datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%Y-%m-%d %H:%M')
    data = data.set_index('datetime')

    # Add 'Date' column for grouping
    data['Date'] = data.index.date

    # Filter daytime and nighttime data
    daytime_data = data.between_time('07:00', '19:00').copy()
    nighttime_data = data.between_time('19:00', '07:00').copy()

    # Group data by 'Date' and calculate averages
    last_week_avg = (
        daytime_data.groupby('Date')[numeric_cols]
        .mean()
        .tail(7)
    )
    last_week_night_avg = (
        nighttime_data.groupby('Date')[numeric_cols]
        .mean()
        .tail(7)
    )
    whole_day_avg = (
        data.groupby('Date')[numeric_cols]
        .mean()
        .tail(7)  # Get the last 7 days
    )

    # Ensure there is data for the day
    if data.empty:
        return render_template('analysis/analysis.html', error="No data available for today.", graphs=graphs)
    # Extract the hour from the index and calculate hourly averages
    data['Hour'] = data.index.hour
    hourly_data = data.groupby('Hour')[numeric_cols].mean()

    # ----------- Hourly measurement graphs ----------- #

    # Generate temperature graph (includes ground temperature)
    plt.figure(figsize=(6, 4))
    plt.plot(hourly_data.index, hourly_data['Temperature'], label='Air Temperature (°C)', color='red')
    plt.plot(hourly_data.index, hourly_data['Ground Temperature'], label='Ground Temperature (°C)', color='orange')
    plt.xlabel('Hour')
    plt.ylabel('Temperature (°C)')
    plt.title('Hourly Average Temperature')
    plt.legend()
    plt.grid(True)
    temp_buffer = io.BytesIO()
    plt.savefig(temp_buffer, format='png')
    temp_buffer.seek(0)
    graphs['temperature'] = base64.b64encode(temp_buffer.getvalue()).decode()

    # Generate humidity graph (includes ground humidity)
    plt.figure(figsize=(6, 4))
    plt.plot(hourly_data.index, hourly_data['Humidity'], label='Air Humidity (%)', color='blue')
    plt.plot(hourly_data.index, hourly_data['Ground Humidity'], label='Ground Humidity (%)', color='green')
    plt.xlabel('Hour')
    plt.ylabel('Humidity (%)')
    plt.title('Hourly Average Humidity')
    plt.legend()
    plt.grid(True)
    hum_buffer = io.BytesIO()
    plt.savefig(hum_buffer, format='png')
    hum_buffer.seek(0)
    graphs['humidity'] = base64.b64encode(hum_buffer.getvalue()).decode()

    # Generate light intensity graph
    plt.figure(figsize=(6, 4))
    plt.plot(hourly_data.index, hourly_data['Light Intensity'], label='Light Intensity (Lux)', color='purple')
    plt.xlabel('Hour')
    plt.ylabel('Light Intensity (Lux)')
    plt.title('Hourly Average Light Intensity')
    plt.legend()
    plt.grid(True)
    lux_buffer = io.BytesIO()
    plt.savefig(lux_buffer, format='png')
    lux_buffer.seek(0)
    graphs['lux'] = base64.b64encode(lux_buffer.getvalue()).decode()

    # ----------- Daytime average measurement graphs ----------- #

    plt.figure(figsize=(6, 4))
    plt.plot(last_week_avg.index, last_week_avg['Temperature'], label='Air Temperature (°C)', color='red', marker='o')
    plt.plot(last_week_avg.index, last_week_avg['Ground Temperature'], label='Ground Temperature (°C)', color='orange', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Average Temperature for the Past Week')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    day_avg_buffer = io.BytesIO()
    plt.savefig(day_avg_buffer, format='png')
    day_avg_buffer.seek(0)
    graphs['daily_avg_temperature'] = base64.b64encode(day_avg_buffer.getvalue()).decode()

    plt.figure(figsize=(6, 4))
    plt.plot(last_week_avg.index, last_week_avg['Humidity'], label='Air Humidity (%)', color='blue', marker='o')
    plt.plot(last_week_avg.index, last_week_avg['Ground Humidity'], label='Ground Humidity (%)', color='green', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Humidity (%)')
    plt.title('Daily Average Humidity for the Past Week')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    humidity_avg_buffer = io.BytesIO()
    plt.savefig(humidity_avg_buffer, format='png')
    humidity_avg_buffer.seek(0)
    graphs['daily_avg_humidity'] = base64.b64encode(humidity_avg_buffer.getvalue()).decode()

    plt.figure(figsize=(6, 4))
    plt.plot(last_week_avg.index, last_week_avg['Light Intensity'], label='Light Intensity (Lux)', color='purple', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Light Intensity (Lux)')
    plt.title('Daily Average Light Intensity for the Past Week')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    light_intensity_avg_buffer = io.BytesIO()
    plt.savefig(light_intensity_avg_buffer, format='png')
    light_intensity_avg_buffer.seek(0)
    graphs['daily_avg_light_intensity'] = base64.b64encode(light_intensity_avg_buffer.getvalue()).decode()

    # ----------- Nighttime average measurement graphs ----------- #

    plt.figure(figsize=(6, 4))
    plt.plot(last_week_night_avg.index, last_week_night_avg['Temperature'], label='Air Temperature (°C)', color='red', marker='o')
    plt.plot(last_week_night_avg.index, last_week_night_avg['Ground Temperature'], label='Ground Temperature (°C)', color='orange', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Nighttime Average Temperature for the Past Week')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    night_temp_avg_buffer = io.BytesIO()
    plt.savefig(night_temp_avg_buffer, format='png')
    night_temp_avg_buffer.seek(0)
    graphs['night_avg_temperature'] = base64.b64encode(night_temp_avg_buffer.getvalue()).decode()

    plt.figure(figsize=(6, 4))
    plt.plot(last_week_night_avg.index, last_week_night_avg['Humidity'], label='Air Humidity (%)', color='blue', marker='o')
    plt.plot(last_week_night_avg.index, last_week_night_avg['Ground Humidity'], label='Ground Humidity (%)', color='green', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Humidity (%)')
    plt.title('Nighttime Average Humidity for the Past Week')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    night_humidity_avg_buffer = io.BytesIO()
    plt.savefig(night_humidity_avg_buffer, format='png')
    night_humidity_avg_buffer.seek(0)
    graphs['night_avg_humidity'] = base64.b64encode(night_humidity_avg_buffer.getvalue()).decode()

    plt.figure(figsize=(6, 4))
    plt.plot(last_week_night_avg.index, last_week_night_avg['Light Intensity'], label='Light Intensity (Lux)', color='purple', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Light Intensity (Lux)')
    plt.title('Nighttime Average Light Intensity for the Past Week')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    night_light_intensity_avg_buffer = io.BytesIO()
    plt.savefig(night_light_intensity_avg_buffer, format='png')
    night_light_intensity_avg_buffer.seek(0)
    graphs['night_avg_light_intensity'] = base64.b64encode(night_light_intensity_avg_buffer.getvalue()).decode()

    # ----------- Allday average measurement graphs ----------- #

    plt.figure(figsize=(6, 4))
    plt.plot(whole_day_avg.index, whole_day_avg['Temperature'], label='Air Temperature (°C)', color='red', marker='o')
    plt.plot(whole_day_avg.index, whole_day_avg['Ground Temperature'], label='Ground Temperature (°C)', color='orange', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Whole-Day Average Temperature for the Past Week')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    whole_temp_avg_buffer = io.BytesIO()
    plt.savefig(whole_temp_avg_buffer, format='png')
    whole_temp_avg_buffer.seek(0)
    graphs['whole_avg_temperature'] = base64.b64encode(whole_temp_avg_buffer.getvalue()).decode()

    plt.figure(figsize=(6, 4))
    plt.plot(whole_day_avg.index, whole_day_avg['Humidity'], label='Air Humidity (%)', color='blue', marker='o')
    plt.plot(whole_day_avg.index, whole_day_avg['Ground Humidity'], label='Ground Humidity (%)', color='green', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Humidity (%)')
    plt.title('Whole-Day Average Humidity for the Past Week')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    whole_humidity_avg_buffer = io.BytesIO()
    plt.savefig(whole_humidity_avg_buffer, format='png')
    whole_humidity_avg_buffer.seek(0)
    graphs['whole_avg_humidity'] = base64.b64encode(whole_humidity_avg_buffer.getvalue()).decode()

    plt.figure(figsize=(6, 4))
    plt.plot(whole_day_avg.index, whole_day_avg['Light Intensity'], label='Light Intensity (Lux)', color='purple', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Light Intensity (Lux)')
    plt.title('Whole-Day Average Light Intensity for the Past Week')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    whole_light_avg_buffer = io.BytesIO()
    plt.savefig(whole_light_avg_buffer, format='png')
    whole_light_avg_buffer.seek(0)
    graphs['whole_avg_light_intensity'] = base64.b64encode(whole_light_avg_buffer.getvalue()).decode()

    return render_template('analysis/analysis.html', graphs=graphs)

