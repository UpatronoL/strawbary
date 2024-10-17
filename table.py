from flask import (
    Blueprint, flash, render_template, current_app
)
import pandas as pd
from datetime import datetime
import os

bp = Blueprint('table', __name__)

@bp.route('/', methods=('GET', 'POST'))
def table():
    csv_file = os.path.join(current_app.root_path, 'data', 'measurements.csv')

    if not os.path.exists(csv_file):
        flash("Data file not found. Please upload data or generate measurements.", "danger")
        return render_template('table/table.html', measurements=[])

    df = pd.read_csv(csv_file)

    # Filter for today's data
    today = datetime.today().date()
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    today_data = df[df['Date'].dt.date == today]

    # Check if there is any data for today
    if today_data.empty:
        flash("No data available for today's date.", "warning")
        return render_template('table/table.html', measurements=[], max_temp=None, min_temp=None, mean_temp=None)

    # Get temperature statistics
    max_temp = today_data['Temperature'].max()
    min_temp = today_data['Temperature'].min()
    mean_temp = today_data['Temperature'].mean()

    # Convert to dict for table display
    data = today_data.to_dict(orient='records')

    return render_template('table/table.html', measurements=data, max_temp=max_temp, min_temp=min_temp, mean_temp=mean_temp)

