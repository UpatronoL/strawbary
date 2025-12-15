# 🍓 Strawberry Environmental Monitoring System

A comprehensive **web-based dashboard** for monitoring and analyzing environmental conditions in strawberry cultivation facilities.  
This system provides **real-time sensor data visualization**, **alert management**, and **detailed analytics** to optimize growing conditions.

---

## ✨ Features

### 🏠 Dashboard (Home)

**Real-time Monitoring**
- Air temperature and humidity
- Soil moisture levels
- Light intensity
- Ground temperature

**Smart Alert System**
- Configurable threshold-based alerts
- Alert history tracking with status management
- Resolution tracking and analytics
- Alert categories:
  - Temperature
  - Moisture
  - Lighting
  - System status

**Additional Features**
- Auto-refresh every **5 minutes**
- Daily statistics and **24-hour analytics**
- Smart tips with context-aware cultivation recommendations

---

### 📊 Measurements Table

**Detailed Data View**
- Comprehensive table of all sensor readings

**Advanced Filtering**
- Date-based filtering
- Column-specific search
- DataTables integration (sorting & pagination)

**Utilities**
- Export data as CSV
- Quick statistics:
  - Total records
  - Time range coverage

---

### 📈 Summary View

**Daily Aggregations**
- Maximum, minimum, and average values

**Time-based Analysis**
- Daily averages
- Daytime averages (6 AM – 6 PM)
- Nighttime averages (6 PM – 6 AM)

**Tracked Parameters**
- Air temperature and humidity
- Ground temperature and humidity
- Light intensity

---

### 📉 Analysis Dashboard

**Trend Analysis**
- Hourly environmental patterns for the current day

**Weekly Analysis**
- 7-day daytime averages
- 7-day nighttime averages
- 7-day whole-day averages

**Visualization**
- Interactive graphs (click to enlarge)
- Side-by-side parameter comparisons

---

### 🔔 Alert History

**Comprehensive Tracking**
- Complete alert log with metadata

**Advanced Filtering**
- By type: danger, warning, info
- By category: temperature, moisture, lighting, system
- By severity: critical, high, medium, low
- By status: active, resolved, acknowledged

**Management Tools**
- Bulk alert actions
- Analytics dashboard for alert trends
- Export detailed alert reports

---

## 🛠️ Technology Stack

### Backend
- **Framework:** Flask 2.3.3
- **Server:** Gunicorn (production)
- **Data Processing:**
  - Pandas 2.1.1
  - NumPy 1.26.4
- **Visualization:** Matplotlib 3.8.0
- **Forms:** Flask-WTF 1.1.1, WTForms 3.1.2

### Frontend
- **Languages:** HTML5, CSS3, JavaScript (ES6+)
- **UI Components:**
  - DataTables
  - Font Awesome icons
  - Custom CSS with CSS variables

**Frontend Features**
- Responsive design
- Dark / light theme toggle
- Multi-language support (English / Japanese)
- Real-time clock and countdown timers

---

## 💾 Data Storage

- **Sensor Data:** CSV files
- **Configuration:** JSON files

### File Structure
```text
app/data/
├── measurements.csv
├── alert_settings.json
└── alert_history.json
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

```bash
git clone <repository-url>
cd strawbary
pip install -r requirements.txt
mkdir -p app/data
python run.py
```

Access the application at:  
`http://localhost:5000`
