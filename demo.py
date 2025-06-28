#!/usr/bin/env python3
"""
Flight Hazard Alert and Crash Response System - Demo Script
==========================================================

This script demonstrates how to use both the command line and web interfaces
of the Flight Hazard Alert and Crash Response System.

Author: College Project
Purpose: Aviation Safety System Demonstration
"""

import os
import sys
import subprocess
import time

def print_banner():
    """Print the system banner"""
    print("=" * 70)
    print("🛩️  Flight Hazard Alert & Crash Response System")
    print("   Real-Time Flight Hazard Detection and Emergency Response")
    print("=" * 70)
    print()

def show_menu():
    """Display the main menu"""
    print("🎮 Choose Your Interface:")
    print("1. 🌐 Web Interface (Streamlit) - Interactive & Visual")
    print("2. 💻 Command Line Interface - Fast & Simple")
    print("3. 📊 Data Import Demo - Real FAA Data")
    print("4. ⚙️  System Components Test")
    print("5. 📖 View Documentation")
    print("6. 🚪 Exit")
    print()

def run_web_interface():
    """Launch the Streamlit web interface"""
    print("🌐 Launching Web Interface...")
    print("📱 Opening browser at: http://localhost:8501")
    print("⏳ Please wait for the web interface to load...")
    print()
    
    try:
        # Check if streamlit is installed
        import streamlit
        print("✅ Streamlit is installed")
        
        # Launch streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
        
    except ImportError:
        print("❌ Streamlit not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "streamlit", "plotly"])
        print("✅ Installation complete. Please run this script again.")
    except KeyboardInterrupt:
        print("\n🛑 Web interface stopped by user")
    except Exception as e:
        print(f"❌ Error launching web interface: {e}")

def run_command_line():
    """Run the command line interface"""
    print("💻 Running Command Line Interface...")
    print("📊 Starting flight simulation...")
    print()
    
    try:
        subprocess.run([sys.executable, "main.py"])
    except KeyboardInterrupt:
        print("\n🛑 Command line interface stopped by user")
    except Exception as e:
        print(f"❌ Error running command line interface: {e}")

def run_data_demo():
    """Demonstrate data import functionality"""
    print("📊 Running Data Import Demo...")
    print("🔄 Loading real FAA accident and incident data...")
    print()
    
    try:
        subprocess.run([sys.executable, "data_import.py"])
    except Exception as e:
        print(f"❌ Error running data demo: {e}")

def test_components():
    """Test individual system components"""
    print("⚙️  Testing System Components...")
    print()
    
    components = [
        ("Flight Simulation", "flight_sim.py"),
        ("Hazard Detection", "hazard_detection.py"),
        ("Alert System", "alert_system.py"),
        ("Visualization", "visualization.py")
    ]
    
    for name, file in components:
        print(f"🧪 Testing {name}...")
        try:
            result = subprocess.run([sys.executable, file], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"✅ {name} test passed")
            else:
                print(f"❌ {name} test failed")
        except Exception as e:
            print(f"❌ Error testing {name}: {e}")
        print()

def show_documentation():
    """Display documentation and help"""
    print("📖 System Documentation")
    print("=" * 40)
    print()
    
    print("🎯 Project Overview:")
    print("   This system simulates a real-time flight hazard detection")
    print("   and emergency response system for aviation safety.")
    print()
    
    print("🚀 Key Features:")
    print("   • Real-time flight data monitoring")
    print("   • Automated hazard detection")
    print("   • Multi-level alert system")
    print("   • Interactive web interface")
    print("   • Real FAA data integration")
    print()
    
    print("📁 Files:")
    print("   • streamlit_app.py - Web interface")
    print("   • main.py - Command line interface")
    print("   • data_import.py - FAA data import")
    print("   • flight_sim.py - Flight data simulation")
    print("   • hazard_detection.py - Hazard detection logic")
    print("   • alert_system.py - Alert system")
    print("   • visualization.py - Charts and graphs")
    print()
    
    print("🛠️  Usage:")
    print("   • Web Interface: streamlit run streamlit_app.py")
    print("   • Command Line: python main.py")
    print("   • Data Import: python data_import.py")
    print()

def main():
    """Main demo function"""
    print_banner()
    
    while True:
        show_menu()
        
        try:
            choice = input("🎯 Enter your choice (1-6): ").strip()
            
            if choice == "1":
                run_web_interface()
            elif choice == "2":
                run_command_line()
            elif choice == "3":
                run_data_demo()
            elif choice == "4":
                test_components()
            elif choice == "5":
                show_documentation()
            elif choice == "6":
                print("👋 Thank you for using the Flight Hazard Alert System!")
                print("🛩️  Safe flying!")
                break
            else:
                print("❌ Invalid choice. Please enter 1-6.")
            
            if choice in ["1", "2", "3", "4"]:
                input("\n⏸️  Press Enter to continue...")
                print()
                
        except KeyboardInterrupt:
            print("\n\n👋 Demo stopped by user. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main() 