import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend for Flask

import matplotlib.pyplot as plt
from flask import Blueprint, render_template, current_app
import pandas as pd
import os
import io
import base64
from datetime import datetime

bp = Blueprint('analysis', __name__, url_prefix='/analysis')

@bp.route('/', methods=['GET'])
def analysis():
    # Load CSV file
    csv_file = os.path.join(current_app.root_path, 'data', 'measurements.csv')

    # Initialize graphs as an empty dictionary
    graphs = {}

    if not os.path.exists(csv_file):
        return render_template('analysis/analysis.html', error="Data file not found.", graphs=graphs)

    # Read and process the data
    data = pd.read_csv(csv_file)
    data['datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%Y-%m-%d %H:%M')
    data.set_index('datetime', inplace=True)

    # Ensure numeric columns are properly converted
    for col in ['Temperature', 'Humidity', 'Light Intensity', 'Ground Temperature', 'Ground Humidity']:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    # Drop rows with missing values
    data = data.dropna()

    # Filter data for today only
    today = datetime.today().date()
    data = data[data.index.date == today]

    # If no data for today, display an error
    if data.empty:
        return render_template('analysis/analysis.html', error="No data available for today.", graphs=graphs)

    # Generate temperature graph (includes ground temperature)
    plt.figure(figsize=(6, 4))
    plt.plot(data.index, data['Temperature'], label='Air Temperature (°C)', color='red')
    plt.plot(data.index, data['Ground Temperature'], label='Ground Temperature (°C)', color='orange')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Throughout the Day')
    plt.legend()
    plt.grid(True)
    temp_buffer = io.BytesIO()
    plt.savefig(temp_buffer, format='png')
    temp_buffer.seek(0)
    graphs['temperature'] = base64.b64encode(temp_buffer.getvalue()).decode()

    # Generate humidity graph (includes ground humidity)
    plt.figure(figsize=(6, 4))
    plt.plot(data.index, data['Humidity'], label='Air Humidity (%)', color='blue')
    plt.plot(data.index, data['Ground Humidity'], label='Ground Humidity (%)', color='green')
    plt.xlabel('Time')
    plt.ylabel('Humidity (%)')
    plt.title('Humidity Throughout the Day')
    plt.legend()
    plt.grid(True)
    hum_buffer = io.BytesIO()
    plt.savefig(hum_buffer, format='png')
    hum_buffer.seek(0)
    graphs['humidity'] = base64.b64encode(hum_buffer.getvalue()).decode()

    # Generate light intensity graph
    plt.figure(figsize=(6, 4))
    plt.plot(data.index, data['Light Intensity'], label='Light Intensity (Lux)', color='purple')
    plt.xlabel('Time')
    plt.ylabel('Light Intensity (Lux)')
    plt.title('Light Intensity Throughout the Day')
    plt.legend()
    plt.grid(True)
    lux_buffer = io.BytesIO()
    plt.savefig(lux_buffer, format='png')
    lux_buffer.seek(0)
    graphs['lux'] = base64.b64encode(lux_buffer.getvalue()).decode()

    return render_template('analysis/analysis.html', graphs=graphs)

