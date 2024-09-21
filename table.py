from flask import (
    Blueprint, flash, render_template, current_app
)
import pandas as pd
from datetime import datetime, timedelta
import os
from .form import DateRange

bp = Blueprint('table', __name__)


@bp.route('/', methods=('GET', 'POST'))
def table():
    csv_file = os.path.join(current_app.root_path, 'data', 'measurements.csv')
    form = DateRange()

    if not os.path.exists(csv_file):
        flash("Data file not found. Please upload data or generate measurements.", "danger")
        return render_template('table/table.html', measurements=[], form=form)

    df = pd.read_csv(csv_file)

    if form.validate_on_submit():
        start_date = pd.to_datetime(form.start_date.data)
        end_date = pd.to_datetime(form.end_date.data)

        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

        filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
        data = filtered_df.to_dict(orient='records')

        if filtered_df.empty:
            flash("No data found for the selected data range", "warning")
    else:
        today = datetime.today()
        thirty_days_ago = today - timedelta(days=30)

        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')  # Ensure Date is datetime
        filtered_df = df[(df['Date'] >= thirty_days_ago) & (df['Date'] <= today)]
        data = filtered_df.to_dict(orient='records')

    return render_template('table/table.html', measurements=data, form=form)
