from flask import Blueprint, render_template, request

bp = Blueprint('home', __name__, url_prefix='/home')


table_data = [
    {'name': 'Strawberry A', 'temperature': 22, 'humidity': 80, 'soil_moisture': 30},
    {'name': 'Strawberry B', 'temperature': 24, 'humidity': 75, 'soil_moisture': 35},
    {'name': 'Strawberry C', 'temperature': 20, 'humidity': 85, 'soil_moisture': 25},
    {'name': 'Strawberry D', 'temperature': 23, 'humidity': 78, 'soil_moisture': 32},
]

@bp.route('/')
def home():
   
    sort_by = request.args.get('sort_by', 'name')  
    sort_order = request.args.get('sort_order', 'asc')  
    filter_name = request.args.get('filter_name', '')  

   
    filtered_data = [row for row in table_data if filter_name.lower() in row['name'].lower()]

 
    if sort_order == 'asc':
        filtered_data.sort(key=lambda x: x[sort_by])
    else:
        filtered_data.sort(key=lambda x: x[sort_by], reverse=True)

    return render_template('home.html', table_data=filtered_data, sort_by=sort_by, sort_order=sort_order, filter_name=filter_name)