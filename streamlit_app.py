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

# Clean, professional CSS styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem;
        border-radius: 1rem;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        margin: 0;
        font-weight: 700;
    }
    
    .main-header p {
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    .status-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .alert-box {
        padding: 1.2rem;
        border-radius: 0.8rem;
        margin: 1rem 0;
        border-left: 5px solid;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    
    .warning {
        background-color: #fff3cd;
        border-color: #ffc107;
        color: #856404;
    }
    
    .danger {
        background-color: #f8d7da;
        border-color: #dc3545;
        color: #721c24;
    }
    
    .success {
        background-color: #d4edda;
        border-color: #28a745;
        color: #155724;
    }
    
    .info {
        background-color: #d1ecf1;
        border-color: #17a2b8;
        color: #0c5460;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin: 0.5rem;
        border: 1px solid #e9ecef;
    }
    
    .metric-card h4 {
        color: #495057;
        margin: 0.5rem 0;
    }
    
    .metric-card p {
        color: #6c757d;
        margin: 0;
        font-size: 0.9rem;
    }
    
    .sidebar-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.2rem;
        border-radius: 0.8rem;
        color: white;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin: 0.5rem;
        display: block;
    }
    
    .section-header {
        background: linear-gradient(90deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        color: black;
    }
    
    .section-header h4 {
        color: black;
        margin: 0;
        font-weight: 600;
    }
    
    .simulation-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 0.8rem;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .simulation-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    
    .progress-container {
        background: #f8f9fa;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .summary-metrics {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def display_header():
    """Display clean header without images"""
    st.markdown("""
    <div class="main-header">
        <h1>🛩️ Flight Hazard Alert & Crash Response System</h1>
        <p>Real-Time Flight Hazard Detection and Automated Emergency Response</p>
    </div>
    """, unsafe_allow_html=True)

def display_features():
    """Display key features with clean styling"""
    st.markdown("### 🚀 System Features")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="feature-icon">📊</div>
            <h4>Real-Time Monitoring</h4>
            <p>Live flight data tracking with instant updates</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="feature-icon">⚠️</div>
            <h4>Hazard Detection</h4>
            <p>AI-powered risk assessment and prediction</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="feature-icon">🚨</div>
            <h4>Alert System</h4>
            <p>Multi-level notifications and emergency response</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="feature-icon">📈</div>
            <h4>Data Analysis</h4>
            <p>FAA incident integration and pattern recognition</p>
        </div>
        """, unsafe_allow_html=True)

def main():
    # Display clean header
    display_header()
    
    # Display features
    display_features()
    
    # Sidebar with clean styling
    with st.sidebar:
        st.markdown('<div class="sidebar-header"><h3>🎛️ Flight Controls</h3></div>', unsafe_allow_html=True)
        
        # Simulation parameters
        st.markdown('<div class="section-header"><h4>⚙️ Simulation Settings</h4></div>', unsafe_allow_html=True)
        flight_duration = st.slider("Flight Duration (time steps)", 10, 50, 25)
        simulation_speed = st.slider("Simulation Speed (seconds per step)", 0.1, 2.0, 0.5)
        
        # Aircraft parameters
        st.markdown('<div class="section-header"><h4>✈️ Aircraft Configuration</h4></div>', unsafe_allow_html=True)
        aircraft_type = st.selectbox(
            "Aircraft Type",
            ["Commercial Airliner", "Private Jet", "Cargo Aircraft", "Military Aircraft"]
        )
        
        # Hazard detection sensitivity
        st.markdown('<div class="section-header"><h4>⚠️ Hazard Detection</h4></div>', unsafe_allow_html=True)
        g_force_threshold = st.slider("G-Force Warning Threshold", 1.5, 4.0, 2.5)
        altitude_threshold = st.slider("Low Altitude Threshold (ft)", 1000, 5000, 3000)
        speed_threshold = st.slider("High Speed Threshold (knots)", 200, 400, 250)
        
        # Safety tips
        st.markdown('<div class="section-header"><h4>💡 Safety Tips</h4></div>', unsafe_allow_html=True)
        st.info("""
        • Monitor G-force levels during maneuvers
        • Maintain safe altitude during approach
        • Check weather conditions regularly
        • Follow standard operating procedures
        """)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="section-header"><h4>📊 Real-Time Flight Monitoring</h4></div>', unsafe_allow_html=True)
        
        # Create placeholders for real-time updates
        chart_placeholder = st.empty()
        status_placeholder = st.empty()
        
    with col2:
        st.markdown('<div class="section-header"><h4>🚨 Alert Dashboard</h4></div>', unsafe_allow_html=True)
        alert_placeholder = st.empty()
        
        # Display system status
        st.markdown("""
        <div class="metric-card">
            <div class="feature-icon">🛡️</div>
            <h4>System Status</h4>
            <p>All systems operational</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Initialize data storage
    if 'flight_data' not in st.session_state:
        st.session_state.flight_data = []
        st.session_state.hazard_history = []
        st.session_state.alert_system = AlertSystem()
    
    # Start simulation button with clean styling
    if st.button("🚀 Start Flight Simulation", type="primary", use_container_width=True):
        st.session_state.flight_data = []
        st.session_state.hazard_history = []
        st.session_state.alert_system = AlertSystem()
        
        # Progress bar with clean styling
        st.markdown('<div class="progress-container">', unsafe_allow_html=True)
        progress_bar = st.progress(0)
        status_text = st.empty()
        st.markdown('</div>', unsafe_allow_html=True)
        
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
        
        # Final summary with clean styling
        st.success("✅ Flight simulation completed!")
        show_simulation_summary()

def update_visualizations(chart_placeholder, status_placeholder, alert_placeholder):
    """Update real-time visualizations with clean styling"""
    if not st.session_state.flight_data:
        return
    
    # Create flight monitoring chart
    df = pd.DataFrame(st.session_state.flight_data)
    times = list(range(len(df)))
    
    # Create subplots with clean styling
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=('🛩️ Altitude (ft)', '⚡ Speed (knots)', '🔄 G-Force'),
        vertical_spacing=0.1
    )
    
    # Altitude plot
    fig.add_trace(
        go.Scatter(x=times, y=df['altitude'], name='Altitude', 
                  line=dict(color='#667eea', width=3)),
        row=1, col=1
    )
    
    # Speed plot
    fig.add_trace(
        go.Scatter(x=times, y=df['speed'], name='Speed', 
                  line=dict(color='#764ba2', width=3)),
        row=2, col=1
    )
    
    # G-Force plot
    fig.add_trace(
        go.Scatter(x=times, y=df['g_force'], name='G-Force', 
                  line=dict(color='#f093fb', width=3)),
        row=3, col=1
    )
    
    # Add hazard markers
    for hazard in st.session_state.hazard_history:
        time_idx = hazard['time']
        if time_idx < len(df):
            fig.add_annotation(
                x=time_idx, y=df.iloc[time_idx]['altitude'],
                text="⚠️", showarrow=True, arrowhead=2, arrowcolor="red",
                row=1, col=1
            )
    
    # Clean layout
    fig.update_layout(
        height=600, 
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12, color='#495057'),
        margin=dict(l=50, r=50, t=50, b=50)
    )
    
    chart_placeholder.plotly_chart(fig, use_container_width=True)
    
    # Update status with clean styling
    if st.session_state.flight_data:
        latest_data = st.session_state.flight_data[-1]
        status_html = f"""
        <div class="status-card">
            <h4>🛩️ Current Flight Status</h4>
            <p><strong>Aircraft:</strong> {latest_data['registration']}</p>
            <p><strong>Altitude:</strong> {latest_data['altitude']:,} ft</p>
            <p><strong>Speed:</strong> {latest_data['speed']} knots</p>
            <p><strong>G-Force:</strong> {latest_data['g_force']:.1f}G</p>
            <p><strong>Turbulence:</strong> {'Yes' if latest_data['turbulence'] else 'No'}</p>
            <p><strong>Time:</strong> {latest_data['timestamp']}</p>
        </div>
        """
        status_placeholder.markdown(status_html, unsafe_allow_html=True)
    
    # Update alerts with clean styling
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
    """Display simulation summary with clean styling"""
    st.markdown('<div class="section-header"><h4>📈 Simulation Summary</h4></div>', unsafe_allow_html=True)
    
    # Summary metrics in a grid
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Time Steps", len(st.session_state.flight_data))
    
    with col2:
        st.metric("Hazards Detected", len(st.session_state.hazard_history))
    
    with col3:
        if st.session_state.flight_data:
            avg_altitude = sum(d['altitude'] for d in st.session_state.flight_data) / len(st.session_state.flight_data)
            st.metric("Average Altitude", f"{avg_altitude:,.0f} ft")
    
    # Hazard breakdown with clean styling
    if st.session_state.hazard_history:
        st.markdown('<div class="section-header"><h4>⚠️ Hazard Analysis</h4></div>', unsafe_allow_html=True)
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
        
        # Final message
        st.markdown("""
        <div class="metric-card">
            <div class="feature-icon">🛩️</div>
            <h4>Simulation Complete</h4>
            <p>Safe skies start with vigilant monitoring</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 