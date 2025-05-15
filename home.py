from flask import Blueprint, render_template, request

# Create the Blueprint with the name 'home'
bp = Blueprint('home', __name__, url_prefix='/home')

# Sample data (replace with your actual data source, e.g., a database)
table_data = [
    {'name': 'Strawberry A', 'temperature': 22, 'humidity': 80, 'soil_moisture': 30},
    {'name': 'Strawberry B', 'temperature': 24, 'humidity': 75, 'soil_moisture': 35},
    {'name': 'Strawberry C', 'temperature': 20, 'humidity': 85, 'soil_moisture': 25},
    {'name': 'Strawberry D', 'temperature': 23, 'humidity': 78, 'soil_moisture': 32},
]

@bp.route('/')
def home():
    # Get sorting and filtering parameters from URL
    sort_by = request.args.get('sort_by', 'name')  # Default to sorting by 'name'
    sort_order = request.args.get('sort_order', 'asc')  # Default to ascending order
    filter_name = request.args.get('filter_name', '')  # Default to no filtering

    # Filter the data based on the 'filter_name' query parameter
    filtered_data = [row for row in table_data if filter_name.lower() in row['name'].lower()]

    # Sorting logic
    if sort_order == 'asc':
        filtered_data.sort(key=lambda x: x[sort_by])
    else:
        filtered_data.sort(key=lambda x: x[sort_by], reverse=True)

    # Use the existing home.html template (not in a subdirectory)
    return render_template('home.html', table_data=filtered_data, sort_by=sort_by, sort_order=sort_order, filter_name=filter_name)