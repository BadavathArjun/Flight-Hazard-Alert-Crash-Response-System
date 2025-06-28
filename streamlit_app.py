import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
import random
from datetime import datetime
from flight_sim import generate_flight_data
from hazard_detection import detect_hazards, check_crash
from alert_system import AlertSystem

# Page configuration
st.set_page_config(
    page_title="Flight Hazard Alert System",
    page_icon="🛩️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .alert-box {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .warning {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
    }
    .danger {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    .success {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🛩️ Flight Hazard Alert & Crash Response System</h1>', unsafe_allow_html=True)
    st.markdown("### Real-Time Flight Hazard Detection and Automated Emergency Response")
    
    # Sidebar for user inputs
    st.sidebar.header("🎛️ Flight Simulation Controls")
    
    # Simulation parameters
    flight_duration = st.sidebar.slider("Flight Duration (time steps)", 10, 50, 25)
    simulation_speed = st.sidebar.slider("Simulation Speed (seconds per step)", 0.1, 2.0, 0.5)
    
    # Aircraft parameters
    st.sidebar.subheader("✈️ Aircraft Configuration")
    aircraft_type = st.sidebar.selectbox(
        "Aircraft Type",
        ["Commercial Airliner", "Private Jet", "Cargo Aircraft", "Military Aircraft"]
    )
    
    # Hazard detection sensitivity
    st.sidebar.subheader("⚠️ Hazard Detection Settings")
    g_force_threshold = st.sidebar.slider("G-Force Warning Threshold", 1.5, 4.0, 2.5)
    altitude_threshold = st.sidebar.slider("Low Altitude Threshold (ft)", 1000, 5000, 3000)
    speed_threshold = st.sidebar.slider("High Speed Threshold (knots)", 200, 400, 250)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📊 Real-Time Flight Monitoring")
        
        # Create placeholders for real-time updates
        chart_placeholder = st.empty()
        status_placeholder = st.empty()
        
    with col2:
        st.subheader("🚨 Alert Dashboard")
        alert_placeholder = st.empty()
        
    # Initialize data storage
    if 'flight_data' not in st.session_state:
        st.session_state.flight_data = []
        st.session_state.hazard_history = []
        st.session_state.alert_system = AlertSystem()
    
    # Start simulation button
    if st.button("🚀 Start Flight Simulation", type="primary"):
        st.session_state.flight_data = []
        st.session_state.hazard_history = []
        st.session_state.alert_system = AlertSystem()
        
        # Progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Simulation loop
        for t in range(flight_duration):
            # Generate flight data
            data = generate_flight_data()
            data['registration'] = f"N{random.randint(10000, 99999)}"
            data['timestamp'] = datetime.now().strftime("%H:%M:%S")
            st.session_state.flight_data.append(data)
            
            # Detect hazards with custom thresholds
            hazards = []
            if data["g_force"] > g_force_threshold:
                hazards.append(f"High G-Force ({data['g_force']:.1f}G)! Possible collision risk.")
            if data["altitude"] < altitude_threshold and data["speed"] > speed_threshold:
                hazards.append(f"Low Altitude ({data['altitude']}ft) & High Speed ({data['speed']}kts)! Terrain risk.")
            if data["turbulence"]:
                hazards.append("Turbulence detected! Advise altitude change.")
            
            # Record hazards
            if hazards:
                st.session_state.hazard_history.append({
                    'time': t,
                    'hazards': hazards,
                    'data': data
                })
            
            # Check for crash
            crash_detected = check_crash(data)
            
            # Update progress
            progress = (t + 1) / flight_duration
            progress_bar.progress(progress)
            status_text.text(f"Time Step {t + 1}/{flight_duration}")
            
            # Update visualizations
            update_visualizations(chart_placeholder, status_placeholder, alert_placeholder)
            
            # Simulate real-time delay
            time.sleep(simulation_speed)
            
            # Check for crash
            if crash_detected:
                st.error(f"💥 CRASH DETECTED at time {t}!")
                st.session_state.alert_system.send_emergency_alert(data)
                break
        
        progress_bar.empty()
        status_text.empty()
        
        # Final summary
        st.success("✅ Flight simulation completed!")
        show_simulation_summary()

def update_visualizations(chart_placeholder, status_placeholder, alert_placeholder):
    """Update real-time visualizations"""
    if not st.session_state.flight_data:
        return
    
    # Create flight monitoring chart
    df = pd.DataFrame(st.session_state.flight_data)
    times = list(range(len(df)))
    
    # Create subplots
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=('Altitude (ft)', 'Speed (knots)', 'G-Force'),
        vertical_spacing=0.1
    )
    
    # Altitude plot
    fig.add_trace(
        go.Scatter(x=times, y=df['altitude'], name='Altitude', line=dict(color='blue')),
        row=1, col=1
    )
    
    # Speed plot
    fig.add_trace(
        go.Scatter(x=times, y=df['speed'], name='Speed', line=dict(color='orange')),
        row=2, col=1
    )
    
    # G-Force plot
    fig.add_trace(
        go.Scatter(x=times, y=df['g_force'], name='G-Force', line=dict(color='green')),
        row=3, col=1
    )
    
    # Add hazard markers
    for hazard in st.session_state.hazard_history:
        time_idx = hazard['time']
        if time_idx < len(df):
            fig.add_annotation(
                x=time_idx, y=df.iloc[time_idx]['altitude'],
                text="⚠️", showarrow=True, arrowhead=2,
                row=1, col=1
            )
    
    fig.update_layout(height=600, showlegend=False)
    chart_placeholder.plotly_chart(fig, use_container_width=True)
    
    # Update status
    if st.session_state.flight_data:
        latest_data = st.session_state.flight_data[-1]
        status_html = f"""
        <div class="alert-box success">
            <h4>Current Flight Status</h4>
            <p><strong>Aircraft:</strong> {latest_data['registration']}</p>
            <p><strong>Altitude:</strong> {latest_data['altitude']:,} ft</p>
            <p><strong>Speed:</strong> {latest_data['speed']} knots</p>
            <p><strong>G-Force:</strong> {latest_data['g_force']:.1f}G</p>
            <p><strong>Turbulence:</strong> {'Yes' if latest_data['turbulence'] else 'No'}</p>
            <p><strong>Time:</strong> {latest_data['timestamp']}</p>
        </div>
        """
        status_placeholder.markdown(status_html, unsafe_allow_html=True)
    
    # Update alerts
    if st.session_state.hazard_history:
        latest_hazards = st.session_state.hazard_history[-1]['hazards']
        alert_html = f"""
        <div class="alert-box warning">
            <h4>⚠️ Latest Hazards Detected</h4>
            <ul>
        """
        for hazard in latest_hazards:
            alert_html += f"<li>{hazard}</li>"
        alert_html += "</ul></div>"
        alert_placeholder.markdown(alert_html, unsafe_allow_html=True)

def show_simulation_summary():
    """Display simulation summary"""
    st.subheader("📈 Simulation Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Time Steps", len(st.session_state.flight_data))
    
    with col2:
        st.metric("Hazards Detected", len(st.session_state.hazard_history))
    
    with col3:
        if st.session_state.flight_data:
            avg_altitude = sum(d['altitude'] for d in st.session_state.flight_data) / len(st.session_state.flight_data)
            st.metric("Average Altitude", f"{avg_altitude:,.0f} ft")
    
    # Hazard breakdown
    if st.session_state.hazard_history:
        st.subheader("⚠️ Hazard Analysis")
        hazard_df = pd.DataFrame([
            {
                'Time': h['time'],
                'Hazard Type': h['hazards'][0].split('!')[0] if h['hazards'] else 'None',
                'Altitude': h['data']['altitude'],
                'Speed': h['data']['speed'],
                'G-Force': h['data']['g_force']
            }
            for h in st.session_state.hazard_history
        ])
        st.dataframe(hazard_df, use_container_width=True)

if __name__ == "__main__":
    main() 