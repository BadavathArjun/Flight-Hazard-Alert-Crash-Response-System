# Flight Hazard Alert and Crash Response System

## 🛩️ Real-Time Flight Hazard Detection and Automated Emergency Response System

A comprehensive software simulation of an intelligent aviation safety system that detects flight hazards in real-time and automatically triggers emergency response protocols.

## 🎯 Project Overview

This system addresses critical aviation safety challenges by providing:
- **Real-time hazard detection** using AI and sensor data
- **Automated cockpit warnings** for pilots
- **Instant crash alerts** with GPS coordinates to rescue teams
- **Reduced emergency response time** to improve survival rates
- **Interactive web interface** for real-time monitoring and configuration

## 🚀 Key Features

### 1. **Real-Time Flight Data Monitoring**
- Altitude tracking (5,000-35,000 ft)
- Speed monitoring (200-600 knots)
- G-Force analysis (0.8-3.0G normal range)
- Turbulence detection

### 2. **Intelligent Hazard Detection**
- **High G-Force Detection**: Alerts when G-force exceeds 2.5G
- **Terrain Risk Assessment**: Warns of low altitude + high speed combinations
- **Turbulence Monitoring**: Detects and reports turbulence conditions
- **Crash Prediction**: Identifies critical crash conditions (G-force > 5.0G or altitude < 1,000ft)

### 3. **Multi-Level Alert System**
- **Cockpit Warnings**: Real-time pilot notifications
- **Ground Control Alerts**: Air traffic control notifications
- **Emergency Crash Alerts**: Automatic search & rescue dispatch

### 4. **Interactive Web Interface (NEW!)**
- **Real-time Flight Monitoring**: Live charts and visualizations
- **User Input Controls**: Customize simulation parameters
- **Data Input Forms**: Aircraft configuration and flight parameters
- **Real FAA Data Integration**: View actual aviation incident data
- **System Configuration**: Adjust hazard detection sensitivity

### 5. **Data Integration**
- **Real FAA Accident Data**: Integration with official aviation incident databases
- **Synthetic Flight Simulation**: Realistic flight data generation for testing
- **Historical Analysis**: Pattern recognition from past accidents

### 6. **Visualization Dashboard**
- Real-time flight monitoring graphs
- Hazard annotation on flight paths
- Multi-parameter visualization (altitude, speed, G-force)
- Interactive Plotly charts

## 📁 Project Structure

```
AIR/
├── main.py                 # Main integration script
├── streamlit_app.py        # Interactive web application
├── data_input_page.py      # Data input and configuration page
├── run_streamlit.py        # Streamlit launcher script
├── data_import.py          # FAA/NTSB data import
├── flight_sim.py           # Flight data simulation
├── hazard_detection.py     # Hazard & crash detection logic
├── alert_system.py         # Multi-level alert system
├── visualization.py        # Flight monitoring dashboard
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── flight_monitoring.png   # Generated visualization
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Choose your interface**:
   - **Command Line Interface**: `python main.py`
   - **Web Interface**: `streamlit run streamlit_app.py`

## 🎮 How to Use

### Option 1: Interactive Web Interface (Recommended)

**Launch the Streamlit app**:
```bash
streamlit run streamlit_app.py
```

**Or use the launcher script**:
```bash
python run_streamlit.py
```

**Web Interface Features**:
- 🎛️ **Interactive Controls**: Adjust simulation parameters in real-time
- 📊 **Live Monitoring**: Real-time flight data visualization
- ⚙️ **Custom Configuration**: Set hazard detection thresholds
- 📈 **Data Input**: Configure aircraft and flight parameters
- 🚨 **Alert Dashboard**: Live hazard and crash alerts
- 📱 **Responsive Design**: Works on desktop and mobile

### Option 2: Command Line Interface

**Quick Start**:
```bash
python main.py
```

This will:
1. Start a 25-step flight simulation
2. Monitor flight parameters in real-time
3. Detect and alert on hazards
4. Generate a flight monitoring visualization
5. Display comprehensive alert summary

### Individual Components

**Test Data Import**:
```bash
python data_import.py
```

**Test Flight Simulation**:
```bash
python flight_sim.py
```

**Test Hazard Detection**:
```bash
python hazard_detection.py
```

**Test Alert System**:
```bash
python alert_system.py
```

**Generate Visualization**:
```bash
python visualization.py
```

## 📊 System Output

### Web Interface Features
- **Real-time Charts**: Interactive Plotly visualizations
- **Live Status Updates**: Current flight parameters
- **Alert Notifications**: Real-time hazard warnings
- **Configuration Panels**: User-adjustable settings
- **Data Tables**: FAA accident data analysis

### Console Output Example
```
🛩️  Flight Hazard Alert and Crash Response System
============================================================
Real-Time Flight Hazard Detection and Automated Emergency Response
============================================================
Starting flight simulation for 25 time steps...
Monitoring: Altitude, Speed, G-Force, Turbulence
------------------------------------------------------------
⏰ Time  0: Alt= 15432ft, Speed= 445kts, G= 1.2
⏰ Time  5: Alt= 28765ft, Speed= 523kts, G= 2.8
🛩️  COCKPIT WARNING [14:23:45]: High G-Force! Possible collision risk.
🏢 GROUND ALERT [14:23:45]: Aircraft N45678
   Location: 34.5678°N, 123.4567°E
   Issue: High G-Force! Possible collision risk.
...
```

### Generated Files
- `flight_monitoring.png`: Flight visualization dashboard
- Console output with real-time alerts and summaries

## 🔬 Technical Implementation

### Hazard Detection Algorithm
```python
def detect_hazards(data):
    hazards = []
    if data["g_force"] > 2.5:
        hazards.append("High G-Force! Possible collision risk.")
    if data["altitude"] < 3000 and data["speed"] > 250:
        hazards.append("Low Altitude & High Speed! Terrain risk.")
    if data["turbulence"]:
        hazards.append("Turbulence detected! Advise altitude change.")
    return hazards
```

### Alert System Architecture
- **Cockpit Warnings**: Immediate pilot notification
- **Ground Alerts**: Air traffic control coordination
- **Emergency Alerts**: Search & rescue dispatch with GPS coordinates

### Web Interface Technology
- **Streamlit**: Interactive web framework
- **Plotly**: Real-time interactive charts
- **Pandas**: Data manipulation and analysis
- **Session State**: Persistent user configurations

## 🎓 College Presentation Features

### Demonstrates:
1. **Real-time Systems**: Live data processing and response
2. **AI/ML Concepts**: Pattern recognition and prediction
3. **Safety Engineering**: Risk assessment and mitigation
4. **Data Science**: Real aviation data integration
5. **Software Engineering**: Modular, scalable architecture
6. **Emergency Response**: Automated crisis management
7. **Web Development**: Interactive user interfaces
8. **User Experience**: Intuitive controls and visualizations

### Presentation Tips:
- **Web Interface**: Run `streamlit run streamlit_app.py` during your presentation
- **Interactive Demo**: Let audience adjust parameters and see real-time changes
- **Real Data**: Show FAA accident data integration
- **Visual Impact**: Highlight the interactive charts and alerts
- **Safety Impact**: Explain potential lives saved with this system

## 🔮 Future Enhancements

### Potential Additions:
1. **Machine Learning**: Predictive hazard modeling
2. **Weather Integration**: Real-time weather data
3. **Satellite Communication**: Global coverage
4. **Mobile App**: Pilot and ground crew interfaces
5. **Database Integration**: Historical accident analysis
6. **IoT Sensors**: Real aircraft sensor integration
7. **Cloud Deployment**: Web-based access for multiple users
8. **API Integration**: Connect with external aviation systems

## 📈 Impact & Benefits

### Safety Improvements:
- **Faster Response Time**: Automated alerts vs. manual detection
- **Better Coordination**: Multi-level alert system
- **Data-Driven Decisions**: Historical accident analysis
- **Reduced Accidents**: Proactive hazard detection

### Economic Benefits:
- **Reduced Insurance Costs**: Fewer accidents
- **Improved Efficiency**: Automated monitoring
- **Regulatory Compliance**: Enhanced safety standards

### User Experience:
- **Intuitive Interface**: Easy-to-use web controls
- **Real-time Feedback**: Immediate visual updates
- **Customizable**: User-defined parameters
- **Accessible**: Works on any device with a web browser

## 🤝 Contributing

This is a college project demonstrating aviation safety technology. For educational purposes and potential improvements, feel free to:
- Add new hazard detection algorithms
- Enhance the visualization system
- Integrate additional data sources
- Improve the alert system
- Add new web interface features

## 📄 License

This project is created for educational purposes as part of a college assignment on aviation safety systems.

---

**Built with ❤️ for Aviation Safety** 