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
        'selected_date': None
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
            template_vars['selected_date'] = selected_date
        except Exception as e:
            flash(f"Invalid date format: {str(e)}", "danger")
            return render_template('table/table.html', **template_vars)
    else:
        # Default to showing data from today
        today = datetime.today().date()
        filtered_data = df[df['Date'] == today]
        template_vars['selected_date'] = today

    # Check if the filtered data is empty
    if filtered_data.empty:
        date_str = selected_date.strftime('%Y-%m-%d') if selected_date else 'today'
        flash(f"No data available for {date_str}.", "warning")
        return render_template('table/table.html', **template_vars)

    try:
        # Sort by time for better display
        filtered_data = filtered_data.sort_values(['Date', 'Time'])
        
        # Reorder columns to: Temp, Soil Temp, Humidity, Soil Humidity, Light Intensity
        desired_order = ['Date', 'Time', 'Temperature', 'Soil Temp', 'Humidity', 'Soil Humidity', 'Light Intensity']
        # Keep only columns that exist in the dataframe
        cols_to_use = [c for c in desired_order if c in filtered_data.columns]
        filtered_data = filtered_data[cols_to_use]
        
        # Convert to list of dictionaries with proper formatting
        template_vars['measurements'] = filtered_data.to_dict(orient='records')
        
    except Exception as e:
        flash(f"Error processing data: {str(e)}", "danger")
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