from flask import (
    Blueprint, flash, render_template, current_app, send_from_directory, request
)
import pandas as pd
from datetime import datetime, timedelta
import os
import numpy as np

bp = Blueprint('table', __name__, url_prefix='/table')

@bp.route('/')
def table():
    csv_file = os.path.join(current_app.root_path, 'data', 'measurements.csv')

    # Initialize all variables with default values
    template_vars = {
        'measurements': [],
        'max_temp': None,
        'min_temp': None,
        'mean_temp': None,
        'daytime_avg': None,
        'nighttime_avg': None
    }

    if not os.path.exists(csv_file):
        flash("Data file not found. Please upload data or generate measurements.", "danger")
        return render_template('table/table.html', **template_vars)

    try:
        df = pd.read_csv(csv_file)
        # Convert Date and Time columns to proper datetime objects
        df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
        df['Date'] = pd.to_datetime(df['Date']).dt.date  # Store as date object
    except Exception as e:
        flash(f"Error reading data file: {str(e)}", "danger")
        return render_template('table/table.html', **template_vars)

    # Get the selected date from the form (if any)
    selected_date = request.args.get('date')
    if selected_date:
        try:
            selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            filtered_data = df[df['Date'] == selected_date]
        except Exception as e:
            flash(f"Invalid date format: {str(e)}", "danger")
            return render_template('table/table.html', **template_vars)
    else:
        # Default to showing data from yesterday
        yesterday = datetime.today().date() - timedelta(days=1)
        filtered_data = df[df['Date'] == yesterday]

    # Check if the filtered data is empty
    if filtered_data.empty:
        flash("No data available for the selected date.", "warning")
        return render_template('table/table.html', **template_vars)

    try:
        # Get temperature statistics
        day_start = '06:00:00'
        day_end = '18:00:00'

        # Convert time strings to datetime.time objects for comparison
        filtered_data['Time'] = pd.to_datetime(filtered_data['Time']).dt.time
        day_start_time = pd.to_datetime(day_start).time()
        day_end_time = pd.to_datetime(day_end).time()

        daytime = filtered_data[(filtered_data['Time'] >= day_start_time) & 
                                (filtered_data['Time'] < day_end_time)]
        nighttime = filtered_data[(filtered_data['Time'] < day_start_time) | 
                                  (filtered_data['Time'] >= day_end_time)]

        # Calculate stats, handling potential NaN values
        template_vars['max_temp'] = np.nanmax(filtered_data['Temperature'])
        template_vars['min_temp'] = np.nanmin(filtered_data['Temperature'])
        template_vars['mean_temp'] = np.nanmean(filtered_data['Temperature'])
        template_vars['daytime_avg'] = np.nanmean(daytime['Temperature']) if not daytime.empty else None
        template_vars['nighttime_avg'] = np.nanmean(nighttime['Temperature']) if not nighttime.empty else None
        
        # Convert to list of dictionaries with proper date formatting
        template_vars['measurements'] = filtered_data.to_dict(orient='records')
        
    except Exception as e:
        flash(f"Error calculating statistics: {str(e)}", "danger")
        return render_template('table/table.html', **template_vars)

    return render_template('table/table.html', **template_vars)

@bp.route('/download')
def download_csv():
    csv_file = os.path.join(current_app.root_path, 'data', 'measurements.csv')
    return send_from_directory(
        directory=os.path.dirname(csv_file),
        path=os.path.basename(csv_file),
        as_attachment=True,
        mimetype='text/csv',
        download_name='measurements.csv'
    )
