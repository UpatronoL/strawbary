from flask import Blueprint, render_template, request, current_app, flash, jsonify, redirect, url_for
import pandas as pd
import os
import json
from datetime import datetime, timedelta
import numpy as np

bp = Blueprint('home', __name__, url_prefix='/home')

DEFAULT_ALERT_SETTINGS = {
    'temp_min': 18.0,
    'temp_max': 28.0,
    'soil_moisture_min': 25.0,
    'soil_moisture_max': 70.0,
    'light_min': 200.0,
    'ground_temp_min': 15.0,
    'ground_temp_max': 25.0,
    'connection_timeout': 10
}

def load_alert_settings():
    """Load alert settings from JSON file"""
    settings_file = os.path.join(current_app.root_path, 'data', 'alert_settings.json')
    
    settings = DEFAULT_ALERT_SETTINGS.copy()
    
    if os.path.exists(settings_file):
        try:
            with open(settings_file, 'r') as f:
                saved_settings = json.load(f)
                settings.update(saved_settings)
        except:
            pass
            
    return settings

def save_alert_settings_to_file(settings):
    """Save alert settings to JSON file"""
    settings_file = os.path.join(current_app.root_path, 'data', 'alert_settings.json')
    os.makedirs(os.path.dirname(settings_file), exist_ok=True)
    try:
        with open(settings_file, 'w') as f:
            json.dump(settings, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving settings: {e}")
        return False

def load_alert_history():
    """Load alert history from JSON file"""
    alerts_file = os.path.join(current_app.root_path, 'data', 'alert_history.json')
    
    if not os.path.exists(alerts_file):
        # Create empty alert history file if it doesn't exist
        os.makedirs(os.path.dirname(alerts_file), exist_ok=True)
        with open(alerts_file, 'w') as f:
            json.dump([], f)
        return []
    
    try:
        with open(alerts_file, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_alert_history(alerts):
    """Save alert history to JSON file"""
    alerts_file = os.path.join(current_app.root_path, 'data', 'alert_history.json')
    os.makedirs(os.path.dirname(alerts_file), exist_ok=True)
    
    try:
        with open(alerts_file, 'w') as f:
            json.dump(alerts, f, indent=2, default=str)
    except Exception as e:
        print(f"Error saving alert history: {e}")

def add_alert_to_history(alert_data):
    """Add new alert to history with unique ID and enhanced metadata"""
    alerts = load_alert_history()
    
    # Create unique alert ID
    alert_id = f"alert_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(alerts)}"
    
    enhanced_alert = {
        'id': alert_id,
        'message': alert_data['message'],
        'type': alert_data['type'],
        'icon': alert_data['icon'],
        'timestamp': alert_data['timestamp'],
        'datetime_created': datetime.now().isoformat(),
        'age_minutes': alert_data.get('age_minutes', 0),
        'status': 'active',  # active, acknowledged, resolved
        'severity': get_alert_severity(alert_data),
        'category': get_alert_category(alert_data['message']),
        'sensor_value': extract_sensor_value(alert_data['message']),
        'resolution_time': None,
        'notes': []
    }
    
   
    existing_alert = find_similar_active_alert(alerts, enhanced_alert)
    if existing_alert:
      
        existing_alert['timestamp'] = alert_data['timestamp']
        existing_alert['datetime_created'] = datetime.now().isoformat()
        existing_alert['age_minutes'] = alert_data.get('age_minutes', 0)
        existing_alert['sensor_value'] = enhanced_alert['sensor_value']
    else:
        alerts.append(enhanced_alert)
    

    if len(alerts) > 1000:
        alerts = alerts[-1000:]
    
    save_alert_history(alerts)
    return alerts

def find_similar_active_alert(alerts, new_alert):
    """Find similar active alert to prevent duplicates"""
    for alert in alerts:
        if (alert['status'] == 'active' and 
            alert['category'] == new_alert['category'] and
            alert['type'] == new_alert['type']):
            return alert
    return None

def get_alert_severity(alert_data):
    """Determine alert severity based on type and message content"""
    severity_map = {
        'danger': 'high',
        'warning': 'medium', 
        'info': 'low'
    }
    
    base_severity = severity_map.get(alert_data['type'], 'medium')
    
    message = alert_data['message'].lower()
    if 'connection' in message or 'offline' in message or 'alert-connection' in message:
        return 'critical'
    elif any(word in message for word in ['extreme', 'critical', 'emergency']):
        return 'critical'
    elif any(word in message for word in ['high', 'low']) and ('temperature' in message or 'temp' in message):
        temp_value = extract_sensor_value(alert_data['message'])
        if temp_value:
            try:
                temp = float(temp_value)
                if temp < 10 or temp > 35:
                    return 'high'
            except:
                pass
    
    return base_severity

def get_alert_category(message):
    """Categorize alert based on message content"""
    message_lower = message.lower()
    
    if 'temperature' in message_lower or 'alert-temp' in message_lower or 'ground-temp' in message_lower:
        return 'temperature'
    elif 'humidity' in message_lower or 'moisture' in message_lower or 'alert-soil-moisture' in message_lower:
        return 'moisture'
    elif 'light' in message_lower or 'alert-light' in message_lower:
        return 'lighting'
    elif 'connection' in message_lower or 'sensor' in message_lower or 'alert-connection' in message_lower:
        return 'system'
    else:
        return 'general'

def extract_sensor_value(message):
    """Extract numerical sensor value from alert message"""
    import re
    
    # Handle key|value format
    if '|' in message:
        try:
            return message.split('|')[1]
        except IndexError:
            pass
  
    patterns = [
        r'(\d+\.?\d*)\s*°C',
        r'(\d+\.?\d*)\s*%',
        r'(\d+\.?\d*)\s*Lux'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, message)
        if match:
            return match.group(1)
    
    return None

def update_alert_ages(alerts):
    """Update age_minutes for all active alerts"""
    current_time = datetime.now()
    
    for alert in alerts:
        if alert['status'] == 'active':
            try:
                created_time = datetime.fromisoformat(alert['datetime_created'])
                age_delta = current_time - created_time
                alert['age_minutes'] = int(age_delta.total_seconds() / 60)
                
 
                if alert['age_minutes'] > 1440:  # 24 hours
                    alert['status'] = 'auto_resolved'
                    alert['resolution_time'] = current_time.isoformat()
            except (ValueError, KeyError):
               
                alert['age_minutes'] = 0
    
    return alerts

def get_alert_statistics(alerts):
    """Calculate alert statistics for dashboard"""
    if not alerts:
        return {
            'total_alerts_24h': 0,
            'active_alerts': 0,
            'resolved_alerts_24h': 0,
            'critical_alerts': 0,
            'most_common_category': 'N/A',
            'avg_resolution_time': 'N/A'
        }
    
    current_time = datetime.now()
    last_24h = current_time - timedelta(hours=24)
    
    recent_alerts = []
    for alert in alerts:
        try:
            alert_time = datetime.fromisoformat(alert['datetime_created'])
            if alert_time >= last_24h:
                recent_alerts.append(alert)
        except (ValueError, KeyError):
            continue
    
    active_alerts = [alert for alert in alerts if alert.get('status') == 'active']
    resolved_24h = [
        alert for alert in recent_alerts 
        if alert.get('status') in ['resolved', 'acknowledged']
    ]
    critical_alerts = [
        alert for alert in active_alerts 
        if alert.get('severity') in ['critical', 'high']
    ]
    
   
    if recent_alerts:
        categories = [alert.get('category', 'general') for alert in recent_alerts]
        most_common = max(set(categories), key=categories.count)
    else:
        most_common = 'N/A'
    
  
    resolved_with_time = [
        alert for alert in alerts 
        if alert.get('status') == 'resolved' and alert.get('resolution_time')
    ]
    
    if resolved_with_time:
        resolution_times = []
        for alert in resolved_with_time:
            try:
                created = datetime.fromisoformat(alert['datetime_created'])
                resolved = datetime.fromisoformat(alert['resolution_time'])
                resolution_times.append((resolved - created).total_seconds() / 60)
            except (ValueError, KeyError):
                continue
        
        if resolution_times:
            avg_resolution = sum(resolution_times) / len(resolution_times)
            avg_resolution_str = f"{avg_resolution:.0f} min"
        else:
            avg_resolution_str = 'N/A'
    else:
        avg_resolution_str = 'N/A'
    
    return {
        'total_alerts_24h': len(recent_alerts),
        'active_alerts': len(active_alerts),
        'resolved_alerts_24h': len(resolved_24h),
        'critical_alerts': len(critical_alerts),
        'most_common_category': most_common,
        'avg_resolution_time': avg_resolution_str
    }

def get_latest_sensor_data():
    """Get the most recent sensor readings and calculate basic statistics"""
    csv_file = os.path.join(current_app.root_path, 'data', 'measurements.csv')
    
  
    sensor_data = {
        'current': {
            'temperature': 'N/A',
            'ground_temperature': 'N/A',
            'humidity': 'N/A', 
            'soil_moisture': 'N/A',
            'light_intensity': 'N/A'
        },
        'today_stats': {
            'temp_min': 'N/A',
            'temp_max': 'N/A', 
            'temp_avg': 'N/A',
            'ground_temp_min': 'N/A',
            'ground_temp_max': 'N/A',
            'ground_temp_avg': 'N/A',
            'humidity_min': 'N/A',
            'humidity_max': 'N/A',
            'soil_moisture_min': 'N/A',
            'soil_moisture_max': 'N/A',
            'soil_moisture_avg': 'N/A',
            'light_min': 'N/A',
            'light_max': 'N/A',
            'light_avg': 'N/A'
        },
        'alerts': [],
        'last_updated': 'No data available',
        'system_status': 'offline',
        'total_readings_today': 0,
        'next_refresh': None,
        'data_freshness_minutes': 0
    }
    
    if not os.path.exists(csv_file):
        return sensor_data
        
    # Load alert settings
    settings = load_alert_settings()
    
    try:
        df = pd.read_csv(csv_file)
        if df.empty:
            return sensor_data
            
      
        df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
        df['Date'] = pd.to_datetime(df['Date']).dt.date
        
   
        df = df.sort_values('datetime')
        
  
        today = datetime.now().date()
        today_data = df[df['Date'] == today]
        
     
        latest_reading = df.iloc[-1] if not df.empty else None
        
        if latest_reading is not None:
            sensor_data['current'] = {
                'temperature': f"{latest_reading['Temperature']:.1f}°C" if pd.notna(latest_reading['Temperature']) else 'N/A',
                'ground_temperature': f"{latest_reading['Soil Temp']:.1f}°C" if pd.notna(latest_reading['Soil Temp']) else 'N/A',
                'humidity': f"{latest_reading['Humidity']:.1f}%" if pd.notna(latest_reading['Humidity']) else 'N/A',
                'soil_moisture': f"{latest_reading['Soil Humidity']:.1f}%" if pd.notna(latest_reading['Soil Humidity']) else 'N/A',
                'light_intensity': f"{latest_reading['Light Intensity']:.0f} Lux" if pd.notna(latest_reading['Light Intensity']) else 'N/A'
            }
            sensor_data['last_updated'] = latest_reading['datetime'].strftime('%B %d, %I:%M %p')
            sensor_data['system_status'] = 'online'
            
           
            time_diff = datetime.now() - latest_reading['datetime']
            sensor_data['data_freshness_minutes'] = int(time_diff.total_seconds() / 60)
            
            # Calculate next expected refresh time (every 5 minutes)
            next_refresh = latest_reading['datetime'] + timedelta(minutes=5)
            sensor_data['next_refresh'] = next_refresh.strftime('%I:%M %p')
        
        # Calculate today's statistics for all parameters
        if not today_data.empty:
            sensor_data['total_readings_today'] = len(today_data)
            sensor_data['today_stats'] = {
                # Temperature stats
                'temp_min': f"{today_data['Temperature'].min():.1f}°C" if pd.notna(today_data['Temperature'].min()) else 'N/A',
                'temp_max': f"{today_data['Temperature'].max():.1f}°C" if pd.notna(today_data['Temperature'].max()) else 'N/A',
                'temp_avg': f"{today_data['Temperature'].mean():.1f}°C" if pd.notna(today_data['Temperature'].mean()) else 'N/A',
                # Ground temperature stats
                'ground_temp_min': f"{today_data['Soil Temp'].min():.1f}°C" if pd.notna(today_data['Soil Temp'].min()) else 'N/A',
                'ground_temp_max': f"{today_data['Soil Temp'].max():.1f}°C" if pd.notna(today_data['Soil Temp'].max()) else 'N/A',
                'ground_temp_avg': f"{today_data['Soil Temp'].mean():.1f}°C" if pd.notna(today_data['Soil Temp'].mean()) else 'N/A',
                # Humidity stats
                'humidity_min': f"{today_data['Humidity'].min():.1f}%" if pd.notna(today_data['Humidity'].min()) else 'N/A',
                'humidity_max': f"{today_data['Humidity'].max():.1f}%" if pd.notna(today_data['Humidity'].max()) else 'N/A',
                'humidity_avg': f"{today_data['Humidity'].mean():.1f}%" if pd.notna(today_data['Humidity'].mean()) else 'N/A',
                # Soil moisture stats (Ground Humidity)
                'soil_moisture_min': f"{today_data['Soil Humidity'].min():.1f}%" if pd.notna(today_data['Soil Humidity'].min()) else 'N/A',
                'soil_moisture_max': f"{today_data['Soil Humidity'].max():.1f}%" if pd.notna(today_data['Soil Humidity'].max()) else 'N/A',
                'soil_moisture_avg': f"{today_data['Soil Humidity'].mean():.1f}%" if pd.notna(today_data['Soil Humidity'].mean()) else 'N/A',
                # Light intensity stats
                'light_min': f"{today_data['Light Intensity'].min():.0f} Lux" if pd.notna(today_data['Light Intensity'].min()) else 'N/A',
                'light_max': f"{today_data['Light Intensity'].max():.0f} Lux" if pd.notna(today_data['Light Intensity'].max()) else 'N/A',
                'light_avg': f"{today_data['Light Intensity'].mean():.0f} Lux" if pd.notna(today_data['Light Intensity'].mean()) else 'N/A'
            }
        
        # Generate intelligent alerts based on actual data with timestamps
        current_alerts = []
        current_time = datetime.now()
        
        if latest_reading is not None:
            alert_timestamp = latest_reading['datetime'].strftime('%I:%M %p')
            
            # Temperature alerts
            if pd.notna(latest_reading['Temperature']):
                if latest_reading['Temperature'] > float(settings.get('temp_max', 28)):
                    current_alerts.append({
                        'id': f"temp_high_{int(current_time.timestamp())}",
                        'icon': 'fas fa-thermometer-full',
                        'message': f"alert-temp-high|{latest_reading['Temperature']:.1f}",
                        'type': 'warning',
                        'timestamp': alert_timestamp,
                        'age_minutes': sensor_data['data_freshness_minutes']
                    })
                elif latest_reading['Temperature'] < float(settings.get('temp_min', 18)):
                    current_alerts.append({
                        'id': f"temp_low_{int(current_time.timestamp())}",
                        'icon': 'fas fa-thermometer-empty', 
                        'message': f"alert-temp-low|{latest_reading['Temperature']:.1f}",
                        'type': 'warning',
                        'timestamp': alert_timestamp,
                        'age_minutes': sensor_data['data_freshness_minutes']
                    })
            
            # Ground Temperature alerts
            if pd.notna(latest_reading['Soil Temp']):
                if latest_reading['Soil Temp'] > float(settings.get('ground_temp_max', 25)):
                    current_alerts.append({
                        'id': f"ground_temp_high_{int(current_time.timestamp())}",
                        'icon': 'fas fa-thermometer-full',
                        'message': f"alert-ground-temp-high|{latest_reading['Soil Temp']:.1f}",
                        'type': 'warning',
                        'timestamp': alert_timestamp,
                        'age_minutes': sensor_data['data_freshness_minutes']
                    })
                elif latest_reading['Soil Temp'] < float(settings.get('ground_temp_min', 15)):
                    current_alerts.append({
                        'id': f"ground_temp_low_{int(current_time.timestamp())}",
                        'icon': 'fas fa-thermometer-empty', 
                        'message': f"alert-ground-temp-low|{latest_reading['Soil Temp']:.1f}",
                        'type': 'warning',
                        'timestamp': alert_timestamp,
                        'age_minutes': sensor_data['data_freshness_minutes']
                    })
            
            # Soil moisture alerts
            if pd.notna(latest_reading['Soil Humidity']):
                if latest_reading['Soil Humidity'] < float(settings.get('soil_moisture_min', 25)):
                    current_alerts.append({
                        'id': f"moisture_low_{int(current_time.timestamp())}",
                        'icon': 'fas fa-tint',
                        'message': f"alert-soil-moisture-low|{latest_reading['Soil Humidity']:.1f}",
                        'type': 'danger',
                        'timestamp': alert_timestamp,
                        'age_minutes': sensor_data['data_freshness_minutes']
                    })
                elif latest_reading['Soil Humidity'] > float(settings.get('soil_moisture_max', 70)):
                    current_alerts.append({
                        'id': f"moisture_high_{int(current_time.timestamp())}",
                        'icon': 'fas fa-tint',
                        'message': f"alert-soil-moisture-high|{latest_reading['Soil Humidity']:.1f}", 
                        'type': 'info',
                        'timestamp': alert_timestamp,
                        'age_minutes': sensor_data['data_freshness_minutes']
                    })
            
            # Light intensity alerts
            if pd.notna(latest_reading['Light Intensity']):
                if latest_reading['Light Intensity'] < float(settings.get('light_min', 200)):
                    current_alerts.append({
                        'id': f"light_low_{int(current_time.timestamp())}",
                        'icon': 'fas fa-sun',
                        'message': f"alert-light-low|{latest_reading['Light Intensity']:.0f}",
                        'type': 'info',
                        'timestamp': alert_timestamp,
                        'age_minutes': sensor_data['data_freshness_minutes']
                    })
        
        # Check data freshness - alert if data is old
        if latest_reading is not None:
            time_diff = datetime.now() - latest_reading['datetime']
            timeout_mins = int(settings.get('connection_timeout', 10))
            if time_diff > timedelta(minutes=timeout_mins):
                current_alerts.append({
                    'id': f"connection_{int(current_time.timestamp())}",
                    'icon': 'fas fa-wifi',
                    'message': f'alert-connection|{int(time_diff.total_seconds() / 60)}',
                    'type': 'warning',
                    'timestamp': current_time.strftime('%I:%M %p'),
                    'age_minutes': 0
                })
        
        # Add new alerts to history
        for alert in current_alerts:
            add_alert_to_history(alert)
        
        sensor_data['alerts'] = current_alerts
        
    except Exception as e:
        print(f"Error reading sensor data: {e}")
        
    return sensor_data

@bp.route('/')
def home():
    # Get real sensor data
    sensor_data = get_latest_sensor_data()
    
    # Load and update alert history
    alert_history = load_alert_history()
    alert_history = update_alert_ages(alert_history)
    save_alert_history(alert_history)
    
    # Get alert statistics
    alert_stats = get_alert_statistics(alert_history)
    
    # Load alert settings
    alert_settings = load_alert_settings()
    
    # Get recent alert history (last 10 alerts for sidebar)
    recent_alerts = []
    for alert in alert_history:
        try:
            alert_time = datetime.fromisoformat(alert['datetime_created'])
            if alert_time >= datetime.now() - timedelta(hours=24):
                recent_alerts.append(alert)
        except (ValueError, KeyError):
            continue
    
    recent_alerts = sorted(recent_alerts, key=lambda x: x['datetime_created'], reverse=True)[:10]
    
    # Smart tips based on current conditions
    tips = [
        "tip-water-morning",
        "tip-soil-moisture",
        "tip-temp-monitor",
        "tip-light-exposure",
        "tip-check-humidity"
    ]
    
    # Select tip based on current conditions or random
    current_tip = tips[0]  # Default tip
    if sensor_data['alerts']:
        # If there are alerts, provide relevant tip
        alert_types = [alert['message'].lower() for alert in sensor_data['alerts']]
        if any('moisture' in alert for alert in alert_types):
            current_tip = tips[1]
        elif any('temperature' in alert for alert in alert_types):
            current_tip = tips[2]
        elif any('light' in alert for alert in alert_types):
            current_tip = tips[3]
    
    return render_template('home.html', 
                         sensor_data=sensor_data,
                         current_tip=current_tip,
                         alert_stats=alert_stats,
                         recent_alert_history=recent_alerts,
                         alert_settings=alert_settings,
                         default_settings=DEFAULT_ALERT_SETTINGS)

@bp.route('/alert-history')
def alert_history():
    """Dedicated alert history page"""
    # Get filter parameters
    filter_type = request.args.get('type', 'all')
    filter_category = request.args.get('category', 'all')  
    filter_severity = request.args.get('severity', 'all')
    filter_status = request.args.get('status', 'all')
    search_query = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    per_page = 25
    
    # Load and update alert history
    alerts = load_alert_history()
    alerts = update_alert_ages(alerts)
    
    # Apply filters
    filtered_alerts = alerts
    
    if filter_type != 'all':
        filtered_alerts = [a for a in filtered_alerts if a.get('type') == filter_type]
    
    if filter_category != 'all':
        filtered_alerts = [a for a in filtered_alerts if a.get('category') == filter_category]
        
    if filter_severity != 'all':
        filtered_alerts = [a for a in filtered_alerts if a.get('severity') == filter_severity]
        
    if filter_status != 'all':
        filtered_alerts = [a for a in filtered_alerts if a.get('status') == filter_status]
    
    if search_query:
        search_lower = search_query.lower()
        filtered_alerts = [
            a for a in filtered_alerts 
            if search_lower in a.get('message', '').lower() or 
               search_lower in a.get('category', '').lower()
        ]
    
    # Sort by creation time (newest first)
    filtered_alerts = sorted(filtered_alerts, 
                           key=lambda x: x.get('datetime_created', ''), 
                           reverse=True)
    
    # Pagination
    total_alerts = len(filtered_alerts)
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    paginated_alerts = filtered_alerts[start_idx:end_idx]
    
    total_pages = (total_alerts + per_page - 1) // per_page
    
    # Get alert statistics
    alert_stats = get_alert_statistics(alerts)
    
    # Get filter options
    filter_options = {
        'types': list(set(a.get('type', 'info') for a in alerts if a.get('type'))),
        'categories': list(set(a.get('category', 'general') for a in alerts if a.get('category'))),
        'severities': list(set(a.get('severity', 'medium') for a in alerts if a.get('severity'))),
        'statuses': list(set(a.get('status', 'active') for a in alerts if a.get('status')))
    }
    
    return render_template('alert_history.html',
                         alerts=paginated_alerts,
                         alert_stats=alert_stats,
                         filter_options=filter_options,
                         current_filters={
                             'type': filter_type,
                             'category': filter_category,
                             'severity': filter_severity,
                             'status': filter_status,
                             'search': search_query
                         },
                         pagination={
                             'page': page,
                             'total_pages': total_pages,
                             'total_alerts': total_alerts,
                             'per_page': per_page
                         })

@bp.route('/resolve-alert/<alert_id>', methods=['POST'])
def resolve_alert(alert_id):
    """Mark alert as resolved"""
    alerts = load_alert_history()
    
    for alert in alerts:
        if alert.get('id') == alert_id:
            alert['status'] = 'resolved'
            alert['resolution_time'] = datetime.now().isoformat()
            
            # Add resolution note if provided
            note = ''
            if request.is_json:
                note = request.json.get('note', '') if request.json else ''
            else:
                note = request.form.get('note', '')
            
            if note:
                alert['notes'].append({
                    'timestamp': datetime.now().isoformat(),
                    'type': 'resolution',
                    'content': note
                })
            
            save_alert_history(alerts)
            
            if request.is_json:
                return jsonify({'success': True, 'message': 'Alert resolved successfully'})
            else:
                flash('Alert resolved successfully', 'success')
                return redirect(request.referrer or url_for('home.alert_history'))
    
    if request.is_json:
        return jsonify({'success': False, 'message': 'Alert not found'}), 404
    else:
        flash('Alert not found', 'error')
        return redirect(url_for('home.alert_history'))

@bp.route('/delete-alert/<alert_id>', methods=['POST'])
def delete_alert(alert_id):
    """Permanently delete an alert"""
    alerts = load_alert_history()
    initial_len = len(alerts)
    alerts = [a for a in alerts if a.get('id') != alert_id]
    
    if len(alerts) < initial_len:
        save_alert_history(alerts)
        if request.is_json:
            return jsonify({'success': True, 'message': 'Alert deleted successfully'})
        else:
            flash('Alert deleted successfully', 'success')
            return redirect(request.referrer or url_for('home.alert_history'))
    
    if request.is_json:
        return jsonify({'success': False, 'message': 'Alert not found'}), 404
    else:
        flash('Alert not found', 'error')
        return redirect(url_for('home.alert_history'))

@bp.route('/save-alert-settings', methods=['POST'])
def save_alert_settings():
    """Save updated alert settings"""
    try:
        data = request.json
        settings = {
            'temp_min': float(data.get('temp_min', 18)),
            'temp_max': float(data.get('temp_max', 28)),
            'soil_moisture_min': float(data.get('soil_moisture_min', 25)),
            'soil_moisture_max': float(data.get('soil_moisture_max', 70)),
            'light_min': float(data.get('light_min', 200)),
            'ground_temp_min': float(data.get('ground_temp_min', 15)),
            'ground_temp_max': float(data.get('ground_temp_max', 25)),
            'connection_timeout': int(data.get('connection_timeout', 10))
        }
        if save_alert_settings_to_file(settings):
            return jsonify({'success': True, 'message': 'Settings saved successfully'})
        return jsonify({'success': False, 'message': 'Failed to save settings file'}), 500
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@bp.route('/download-report')
def download_report():
    """Generate and download a comprehensive dashboard report as CSV"""
    from flask import make_response
    import io
    import csv
    from datetime import datetime
    
    def format_alert_msg(msg):
        """Helper to format alert keys back to English for CSV"""
        if '|' in msg:
            key, val = msg.split('|')
            if 'temp-high' in key: return f"High temperature alert: {val}°C"
            if 'temp-low' in key: return f"Low temperature alert: {val}°C"
            if 'ground-temp-high' in key: return f"High Soil Temp: {val}°C"
            if 'ground-temp-low' in key: return f"Low Soil Temp: {val}°C"
            if 'soil-moisture-low' in key: return f"Low Soil Humidity: {val}%"
            if 'soil-moisture-high' in key: return f"High Soil Humidity: {val}%"
            if 'light-low' in key: return f"Low light conditions: {val} Lux"
            if 'connection' in key: return f"Sensor connection issue - last data received {val} minutes ago"
        return msg

    # Get current sensor data
    sensor_data = get_latest_sensor_data()
    
    # Get alert statistics
    alert_history = load_alert_history()
    alert_stats = get_alert_statistics(alert_history)
    
    # Create CSV content in memory
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Professional report header
    report_date = datetime.now().strftime('%Y-%m-%d')
    report_time = datetime.now().strftime('%H:%M:%S')
    
    writer.writerow(['STRAWBERRY ENVIRONMENTAL MONITORING SYSTEM'])
    writer.writerow(['OPERATIONAL STATUS REPORT WITH ALERT HISTORY'])
    writer.writerow([''])
    writer.writerow(['Report Information'])
    writer.writerow(['Report Date:', report_date])
    writer.writerow(['Report Time:', report_time])
    writer.writerow(['System Status:', sensor_data['system_status'].upper()])
    writer.writerow(['Data Source:', 'Automated Environmental Sensors'])
    writer.writerow(['Report Type:', 'Real-time Dashboard Summary with Alert Analytics'])
    writer.writerow([''])
    
    # Executive Summary with Alert Statistics
    writer.writerow(['EXECUTIVE SUMMARY'])
    writer.writerow([''])
    
    status_summary = "OPERATIONAL" if sensor_data['system_status'] == 'online' else "ATTENTION REQUIRED"
    alert_count = len(sensor_data['alerts'])
    
    writer.writerow(['Overall System Status:', status_summary])
    writer.writerow(['Active Alerts Count:', alert_count])
    writer.writerow(['Critical Alerts (24h):', alert_stats['critical_alerts']])
    writer.writerow(['Total Alerts (24h):', alert_stats['total_alerts_24h']])
    writer.writerow(['Resolved Alerts (24h):', alert_stats['resolved_alerts_24h']])
    writer.writerow(['Most Common Alert Category:', alert_stats['most_common_category'].title()])
    writer.writerow(['Average Resolution Time:', alert_stats['avg_resolution_time']])
    writer.writerow(['Data Collection Status:', 'ACTIVE' if sensor_data['total_readings_today'] > 0 else 'INACTIVE'])
    writer.writerow(['Total Readings Today:', sensor_data['total_readings_today']])
    writer.writerow(['Last Data Update:', sensor_data['last_updated']])
    writer.writerow(['Data Freshness:', f"{sensor_data['data_freshness_minutes']} minutes ago"])
    writer.writerow([''])
    
    # Current Environmental Conditions
    writer.writerow(['CURRENT ENVIRONMENTAL CONDITIONS'])
    writer.writerow([''])
    writer.writerow(['Parameter', 'Current Value', 'Unit', 'Status'])
    
    # Add status indicators for each parameter
    def get_parameter_status(param_name, value_str):
        if 'N/A' in value_str:
            return 'NO DATA'
        try:
            if param_name == 'Temperature':
                val = float(value_str.replace('°C', ''))
                if 18 <= val <= 24:
                    return 'OPTIMAL'
                elif 15 <= val <= 28:
                    return 'ACCEPTABLE'
                else:
                    return 'SUBOPTIMAL'
            elif param_name == 'Humidity':
                val = float(value_str.replace('%', ''))
                if 60 <= val <= 70:
                    return 'OPTIMAL'
                elif 50 <= val <= 80:
                    return 'ACCEPTABLE'
                else:
                    return 'SUBOPTIMAL'
            elif param_name == 'Soil Humidity':
                val = float(value_str.replace('%', ''))
                if 30 <= val <= 70:
                    return 'OPTIMAL'
                elif 20 <= val <= 80:
                    return 'ACCEPTABLE'
                else:
                    return 'SUBOPTIMAL'
            elif param_name == 'Light Intensity':
                val = float(value_str.replace(' Lux', ''))
                if 400 <= val <= 800:
                    return 'OPTIMAL'
                elif 200 <= val <= 1000:
                    return 'ACCEPTABLE'
                else:
                    return 'SUBOPTIMAL'
            elif param_name == 'Soil Temp':
                val = float(value_str.replace('°C', ''))
                if 15 <= val <= 25:
                    return 'OPTIMAL'
                else:
                    return 'ACCEPTABLE'
        except:
            return 'UNKNOWN'
        return 'ACCEPTABLE'
    
    writer.writerow(['Temperature', sensor_data['current']['temperature'].replace('°C', ''), '°C', 
                    get_parameter_status('Temperature', sensor_data['current']['temperature'])])
    writer.writerow(['Soil Temp', sensor_data['current']['ground_temperature'].replace('°C', ''), '°C', 
                    get_parameter_status('Soil Temp', sensor_data['current']['ground_temperature'])])
    writer.writerow(['Humidity', sensor_data['current']['humidity'].replace('%', ''), '%', 
                    get_parameter_status('Humidity', sensor_data['current']['humidity'])])
    writer.writerow(['Soil Humidity', sensor_data['current']['soil_moisture'].replace('%', ''), '%', 
                    get_parameter_status('Soil Humidity', sensor_data['current']['soil_moisture'])])
    writer.writerow(['Light Intensity', sensor_data['current']['light_intensity'].replace(' Lux', ''), 'Lux', 
                    get_parameter_status('Light Intensity', sensor_data['current']['light_intensity'])])
    writer.writerow([''])
    
    # Alert Analysis with Enhanced History Data
    writer.writerow(['ALERT ANALYSIS & HISTORY'])
    writer.writerow([''])
    if sensor_data['alerts']:
        writer.writerow(['Current Active Alerts'])
        writer.writerow(['Priority', 'Alert Description', 'Alert Time', 'Age (minutes)', 'Recommendation'])
        for i, alert in enumerate(sensor_data['alerts'], 1):
            priority = 'HIGH' if alert['type'] == 'danger' else 'MEDIUM' if alert['type'] == 'warning' else 'LOW'
            recommendation = ''
            if 'temperature' in alert['message'].lower():
                recommendation = 'Adjust environmental controls'
            elif 'moisture' in alert['message'].lower():
                recommendation = 'Check irrigation system'
            elif 'light' in alert['message'].lower():
                recommendation = 'Verify lighting conditions'
            elif 'connection' in alert['message'].lower():
                recommendation = 'Check sensor connectivity'
            else:
                recommendation = 'Monitor conditions closely'
            
            writer.writerow([priority, format_alert_msg(alert['message']), alert['timestamp'], 
                           alert['age_minutes'], recommendation])
        writer.writerow([''])
    
    # Alert History Summary (last 24 hours)
    recent_alerts = [
        alert for alert in alert_history 
        if datetime.fromisoformat(alert['datetime_created']) >= datetime.now() - timedelta(hours=24)
    ]
    
    writer.writerow(['24-HOUR ALERT HISTORY SUMMARY'])
    writer.writerow([''])
    writer.writerow(['Metric', 'Count', 'Percentage of Total'])
    
    if recent_alerts:
        total_recent = len(recent_alerts)
        
        # By type
        type_counts = {}
        for alert in recent_alerts:
            type_counts[alert.get('type', 'info')] = type_counts.get(alert.get('type', 'info'), 0) + 1
        
        writer.writerow(['Alert Distribution by Type'])
        for alert_type, count in type_counts.items():
            percentage = (count / total_recent) * 100
            writer.writerow([f'{alert_type.title()} Alerts', count, f'{percentage:.1f}%'])
        
        writer.writerow([''])
        
        # By category
        category_counts = {}
        for alert in recent_alerts:
            category_counts[alert.get('category', 'general')] = category_counts.get(alert.get('category', 'general'), 0) + 1
            
        writer.writerow(['Alert Distribution by Category'])
        for category, count in category_counts.items():
            percentage = (count / total_recent) * 100
            writer.writerow([f'{category.title()} Issues', count, f'{percentage:.1f}%'])
        
        writer.writerow([''])
        
        # By severity
        severity_counts = {}
        for alert in recent_alerts:
            severity_counts[alert.get('severity', 'medium')] = severity_counts.get(alert.get('severity', 'medium'), 0) + 1
            
        writer.writerow(['Alert Distribution by Severity'])
        for severity, count in severity_counts.items():
            percentage = (count / total_recent) * 100
            writer.writerow([f'{severity.title()} Severity', count, f'{percentage:.1f}%'])
            
    else:
        writer.writerow(['NO ALERTS IN LAST 24 HOURS'])
        writer.writerow(['System operating normally'])
    
    writer.writerow([''])
    
    # Daily Performance Analytics
    writer.writerow(['DAILY PERFORMANCE ANALYTICS'])
    writer.writerow([''])
    writer.writerow(['Metric', 'Value', 'Performance Indicator'])
    
    def format_temp_performance(min_temp, max_temp):
        try:
            min_val = float(min_temp.replace('°C', ''))
            max_val = float(max_temp.replace('°C', ''))
            if 18 <= min_val and max_val <= 26:
                return 'EXCELLENT'
            elif 15 <= min_val and max_val <= 30:
                return 'GOOD'
            else:
                return 'NEEDS ATTENTION'
        except:
            return 'INSUFFICIENT DATA'
    
    temp_performance = format_temp_performance(sensor_data['today_stats']['temp_min'], 
                                              sensor_data['today_stats']['temp_max'])
    
    writer.writerow(['Temperature Range', 
                    f"{sensor_data['today_stats']['temp_min']} to {sensor_data['today_stats']['temp_max']}", 
                    temp_performance])
    writer.writerow(['Temperature Average', sensor_data['today_stats']['temp_avg'], 
                    'CALCULATED' if 'N/A' not in sensor_data['today_stats']['temp_avg'] else 'NO DATA'])
    writer.writerow(['Humidity Range', 
                    f"{sensor_data['today_stats']['humidity_min']} to {sensor_data['today_stats']['humidity_max']}", 
                    'MONITORED'])
    writer.writerow(['Data Collection Rate', f"{sensor_data['total_readings_today']} samples", 
                    'ACTIVE' if sensor_data['total_readings_today'] > 50 else 'LOW FREQUENCY'])
    writer.writerow(['Alert Response Efficiency', alert_stats['avg_resolution_time'], 
                    'GOOD' if 'min' in alert_stats['avg_resolution_time'] else 'N/A'])
    writer.writerow([''])
    
    # Compliance and Quality Metrics
    writer.writerow(['COMPLIANCE & QUALITY METRICS'])
    writer.writerow([''])
    writer.writerow(['Metric', 'Status', 'Notes'])
    writer.writerow(['Data Completeness', 
                    'COMPLETE' if sensor_data['total_readings_today'] > 0 else 'INCOMPLETE',
                    f"Collected {sensor_data['total_readings_today']} data points today"])
    writer.writerow(['System Uptime', 
                    'OPERATIONAL' if sensor_data['system_status'] == 'online' else 'DEGRADED',
                    'Based on most recent sensor communication'])
    writer.writerow(['Alert Response', 
                    'MONITORED' if len(sensor_data['alerts']) == 0 else f'{len(sensor_data["alerts"])} ALERTS ACTIVE',
                    'Automated monitoring system with history tracking'])
    writer.writerow(['Alert History Retention', 
                    'ACTIVE', 
                    f'Maintaining {len(alert_history)} historical alert records'])
    writer.writerow([''])
    
    # Detailed Alert History (last 50 alerts)
    writer.writerow(['DETAILED ALERT HISTORY (LAST 50 EVENTS)'])
    writer.writerow([''])
    writer.writerow(['Alert ID', 'Date/Time', 'Type', 'Category', 'Severity', 'Message', 'Status', 'Resolution Time'])
    
    recent_detailed = sorted(alert_history, key=lambda x: x.get('datetime_created', ''), reverse=True)[:50]
    
    for alert in recent_detailed:
        try:
            created_dt = datetime.fromisoformat(alert['datetime_created'])
            resolution_time = 'N/A'
            
            if alert.get('resolution_time'):
                resolved_dt = datetime.fromisoformat(alert['resolution_time'])
                resolution_minutes = (resolved_dt - created_dt).total_seconds() / 60
                resolution_time = f"{resolution_minutes:.0f} min"
            
            writer.writerow([
                alert.get('id', 'N/A'),
                created_dt.strftime('%Y-%m-%d %H:%M:%S'),
                alert.get('type', 'info').title(),
                alert.get('category', 'general').title(),
                alert.get('severity', 'medium').title(),
                format_alert_msg(alert.get('message', 'No message')),
                alert.get('status', 'active').title(),
                resolution_time
            ])
        except (ValueError, KeyError):
            continue
    
    writer.writerow([''])
    
    # Report Footer
    writer.writerow(['REPORT CERTIFICATION'])
    writer.writerow([''])
    writer.writerow(['Generated By:', 'Strawberry Environmental Monitoring System v2.0'])
    writer.writerow(['Report Features:', 'Real-time Data + Alert History Analytics'])
    writer.writerow(['Authorized By:', 'Automated Reporting System with Alert Tracking'])
    writer.writerow(['Report Validity:', '24 Hours from Generation Time'])
    writer.writerow(['Alert History Coverage:', f'{len(alert_history)} total alerts tracked'])
    writer.writerow(['Contact Information:', 'support@strawberrymonitoring.com'])
    writer.writerow([''])
    writer.writerow(['END OF REPORT'])
    
    # Create response
    output.seek(0)
    response = make_response(output.getvalue())
    
    # Set headers for file download
    filename = f"Environmental_Report_with_Alerts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    response.headers['Content-Type'] = 'text/csv; charset=utf-8'
    
    return response