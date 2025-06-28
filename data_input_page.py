import streamlit as st
import pandas as pd
from data_import import load_faa_ntsb_data

def show_data_input_page():
    st.title("📊 Data Input & Configuration")
    st.markdown("### Customize Flight Parameters and View Real Aviation Data")
    
    # Create tabs for different data input sections
    tab1, tab2, tab3 = st.tabs(["✈️ Flight Parameters", "📈 Real FAA Data", "⚙️ System Configuration"])
    
    with tab1:
        st.header("✈️ Custom Flight Parameters")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Aircraft Configuration")
            aircraft_type = st.selectbox(
                "Aircraft Type",
                ["Boeing 737", "Airbus A320", "Boeing 777", "Airbus A350", "Private Jet", "Cargo Aircraft"]
            )
            
            aircraft_registration = st.text_input(
                "Aircraft Registration",
                value="N12345",
                help="Enter aircraft registration number (e.g., N12345)"
            )
            
            flight_number = st.text_input(
                "Flight Number",
                value="FL123",
                help="Enter flight number"
            )
            
        with col2:
            st.subheader("Flight Route")
            departure_airport = st.text_input("Departure Airport", value="JFK")
            arrival_airport = st.text_input("Arrival Airport", value="LAX")
            
            flight_phase = st.selectbox(
                "Current Flight Phase",
                ["Takeoff", "Climb", "Cruise", "Descent", "Landing", "Taxi"]
            )
        
        st.subheader("Environmental Conditions")
        col3, col4, col5 = st.columns(3)
        
        with col3:
            weather_condition = st.selectbox(
                "Weather Condition",
                ["Clear", "Cloudy", "Rain", "Snow", "Fog", "Thunderstorm"]
            )
            
        with col4:
            visibility = st.slider("Visibility (miles)", 0.0, 10.0, 5.0)
            
        with col5:
            wind_speed = st.slider("Wind Speed (knots)", 0, 50, 10)
    
    with tab2:
        st.header("📈 Real FAA Accident & Incident Data")
        
        if st.button("🔄 Load Latest FAA Data"):
            with st.spinner("Loading FAA accident and incident data..."):
                try:
                    df = load_faa_ntsb_data()
                    
                    st.success(f"✅ Successfully loaded {len(df)} records from FAA database")
                    
                    # Show data summary
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Total Records", len(df))
                    with col2:
                        st.metric("Date Range", f"{df['EVENT_LCL_DATE'].min()} to {df['EVENT_LCL_DATE'].max()}")
                    with col3:
                        st.metric("Unique Aircraft", df['REGIST_NBR'].nunique())
                    
                    # Show sample data
                    st.subheader("Sample Data")
                    st.dataframe(df.head(10), use_container_width=True)
                    
                    # Data analysis
                    st.subheader("Data Analysis")
                    
                    # Event types
                    if 'EVENT_TYPE_DESC' in df.columns:
                        event_counts = df['EVENT_TYPE_DESC'].value_counts()
                        st.bar_chart(event_counts)
                    
                    # Geographic distribution
                    if 'LOC_STATE_NAME' in df.columns:
                        state_counts = df['LOC_STATE_NAME'].value_counts().head(10)
                        st.write("Top 10 States by Incidents:")
                        st.dataframe(state_counts)
                        
                except Exception as e:
                    st.error(f"❌ Error loading FAA data: {str(e)}")
                    st.info("Using sample data for demonstration...")
                    
                    # Create sample data
                    sample_data = {
                        'EVENT_LCL_DATE': ['2023-01-15', '2023-02-20', '2023-03-10'],
                        'LOC_STATE_NAME': ['California', 'Texas', 'Florida'],
                        'EVENT_TYPE_DESC': ['Incident', 'Accident', 'Incident'],
                        'ACFT_MAKE_NAME': ['Boeing', 'Airbus', 'Boeing'],
                        'ACFT_MODEL_NAME': ['737', 'A320', '777']
                    }
                    df = pd.DataFrame(sample_data)
                    st.dataframe(df, use_container_width=True)
    
    with tab3:
        st.header("⚙️ System Configuration")
        
        st.subheader("Hazard Detection Sensitivity")
        
        col1, col2 = st.columns(2)
        
        with col1:
            g_force_warning = st.slider(
                "G-Force Warning Threshold",
                min_value=1.0,
                max_value=5.0,
                value=2.5,
                step=0.1,
                help="G-Force level that triggers a warning"
            )
            
            altitude_warning = st.slider(
                "Low Altitude Warning (ft)",
                min_value=500,
                max_value=5000,
                value=3000,
                step=100,
                help="Altitude below which warnings are triggered"
            )
            
        with col2:
            speed_warning = st.slider(
                "High Speed Warning (knots)",
                min_value=150,
                max_value=500,
                value=250,
                step=10,
                help="Speed above which warnings are triggered"
            )
            
            crash_threshold = st.slider(
                "Crash Detection Threshold (G-Force)",
                min_value=3.0,
                max_value=10.0,
                value=5.0,
                step=0.5,
                help="G-Force level that triggers crash detection"
            )
        
        st.subheader("Alert System Configuration")
        
        alert_types = st.multiselect(
            "Enable Alert Types",
            ["Cockpit Warnings", "Ground Control Alerts", "Emergency Alerts", "Email Notifications", "SMS Alerts"],
            default=["Cockpit Warnings", "Ground Control Alerts", "Emergency Alerts"]
        )
        
        auto_response = st.checkbox(
            "Enable Automatic Emergency Response",
            value=True,
            help="Automatically dispatch search and rescue teams"
        )
        
        # Save configuration
        if st.button("💾 Save Configuration"):
            config = {
                "g_force_warning": g_force_warning,
                "altitude_warning": altitude_warning,
                "speed_warning": speed_warning,
                "crash_threshold": crash_threshold,
                "alert_types": alert_types,
                "auto_response": auto_response
            }
            
            st.session_state.config = config
            st.success("✅ Configuration saved successfully!")
            
            # Show saved config
            st.json(config)

if __name__ == "__main__":
    show_data_input_page() 