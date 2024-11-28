from flask import (
        Blueprint, flash, render_template, current_app, send_from_directory
        )
import pandas as pd
from datetime import datetime, timedelta
import os

bp = Blueprint('table', __name__)

@bp.route('/', methods=('GET', 'POST'))
def table():
    csv_file = os.path.join(current_app.root_path, 'data', 'measurements.csv')

    if not os.path.exists(csv_file):
        flash("Data file not found. Please upload data or generate measurements.", "danger")
        return render_template('table/table.html', measurements=[])

    df = pd.read_csv(csv_file)

    # Filter for yesterday's data
    yesterday = datetime.today().date()
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    yesterday_data = df[df['Date'].dt.date == yesterday]

    # Check if there is any data for yesterday
    if yesterday_data.empty:
        flash("No data available for yesterday's date.", "warning")
        return render_template('table/table.html', measurements=[], max_temp=None, min_temp=None, mean_temp=None)

    # Get temperature statistics
    day_start = '06:00:00'
    day_end = '18:00:00'
    daytime = yesterday_data[(pd.to_datetime((yesterday_data['Time'])).dt.time >= pd.to_datetime(day_start).time()) &
                             (pd.to_datetime((yesterday_data['Time'])).dt.time < pd.to_datetime(day_end).time())]
    nighttime = yesterday_data[(pd.to_datetime((yesterday_data['Time'])).dt.time < pd.to_datetime(day_start).time()) |
                               (pd.to_datetime((yesterday_data['Time'])).dt.time >= pd.to_datetime(day_end).time())]

    max_temp = yesterday_data['Temperature'].max()
    min_temp = yesterday_data['Temperature'].min()
    mean_temp = yesterday_data['Temperature'].mean()
    daytime_avg = daytime['Temperature'].mean()
    nighttime_avg = nighttime['Temperature'].mean()

    # Convert to dict for table display
    data = yesterday_data.to_dict(orient='records')

    return render_template('table/table.html', measurements=data,
                           max_temp=max_temp, min_temp=min_temp,
                           mean_temp=mean_temp, daytime_avg=daytime_avg,
                           nighttime_avg=nighttime_avg)


@bp.route('/download', methods=['GET'])
def download_csv():
    csv_file = os.path.join(current_app.root_path, 'data', 'measurements.csv')
    return send_from_directory(
        directory=os.path.dirname(csv_file),
        path=os.path.basename(csv_file),
        as_attachment=True,
        mimetype='text/csv',
        download_name='measurements.csv'
    )

