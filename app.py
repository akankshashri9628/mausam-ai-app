import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mausam - Personalized AI Engine", page_icon="🌤️", layout="wide")

# Header Section
st.title("🌤️ 'Mausam' Smart Personalization Engine")
st.caption("SIH Problem Statement: SIH26076 | Ministry of Earth Sciences (IMD)")

st.sidebar.header("🕹️ Demo Controls (Simulate Context)")
# Persona Selector for Presentation
persona = st.sidebar.selectbox(
    "Select User Persona:",
    ["🌾 Kisan / Farmer Mode", "🚗 Commuter / Traveller Mode", "🏃 Health & Fitness Mode", "🚨 Emergency Red Alert Mode"]
)

# Simulated Weather Conditions
location = st.sidebar.text_input("Live Location", "Lucknow, UP")
temp = "32°C"
humidity = "78%"

st.sidebar.markdown("---")
st.sidebar.info("💡 **Judge Pitch:** App automatically selects layout based on GPS, Season & IMD Hazard Score.")

# --- DYNAMIC UI RENDERING LOGIC ---

# 1. KISAN / FARMER MODE
if persona == "🌾 Kisan / Farmer Mode":
    st.success(f"📍 Location Detected: {location} | **Persona: Agricultural Dashboard**")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Rainfall Probability", "85%", "High Chance Today")
    col2.metric("Soil Moisture", "42%", "+5% from Yesterday")
    col3.metric("Wind Speed", "14 km/h", "Safe for Spraying")
    
    st.subheader("👨‍🌾 Agromet Advisories (Kisan Bulletin)")
    st.warning("⚠️ **Farmer Alert:** Heavy rainfall expected in the next 24 hours. Postpone paddy harvesting and clear drainage channels.")
    st.info("🚜 **Mandi Weather:** High humidity expected at local mandi yard. Keep harvested wheat covered.")

# 2. COMMUTER / TRAVELLER MODE
elif persona == "🚗 Commuter / Traveller Mode":
    st.info(f"📍 Location Detected: {location} | **Persona: Travel & Visibility Dashboard**")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Road Visibility", "1.2 km", "-300m (Mist/Fog)")
    col2.metric("Hourly Storm Risk", "Low", "Safe till 6 PM")
    col3.metric("Current Temp", temp, humidity)
    
    st.subheader("🚗 Highway & Route Advisories")
    st.write("✅ **NH-24 Route:** Open, clear roads.")
    st.write("⚠️ **Expressway Warning:** Expect sudden rain showers post 5:00 PM. Keep vehicle speed under 60 km/h.")

# 3. HEALTH & FITNESS MODE
elif persona == "🏃 Health & Fitness Mode":
    st.success(f"📍 Location Detected: {location} | **Persona: Environmental Health Index**")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("AQI Index", "142", "Moderate Air Quality")
    col2.metric("UV Index", "8 (High)", "Wear Sunscreen")
    col3.metric("Humidity", humidity, "High Sweat Rate")
    
    st.subheader("🏋️ Active Lifestyle Forecast")
    st.write("🟢 **Best Workout Window:** 6:00 AM - 8:00 AM (Optimal AQI & Temp).")
    st.write("🔴 **Avoid Outdoor Running:** Between 12:00 PM - 3:00 PM due to high UV rays.")

# 4. EMERGENCY RED ALERT MODE
elif persona == "🚨 Emergency Red Alert Mode":
    st.error("🚨 CRITICAL WEATHER HAZARD DETECTED IN YOUR ZONE!")
    st.markdown("## 🔴 CYCLONE / SEVERE STORM OVERRIDE DASHBOARD")
    
    st.error("""
    **IMD RED ALERT (Next 12 Hours):**
    - **Wind Gusts:** Up to 90 km/h expected.
    - **Evacuation Zone:** Low-lying areas near rivers.
    - **Emergency Helpline:** 1077 (Disaster Control Room)
    """)
    st.button("📲 Send SOS Location to Local Disaster Relief")

# Footer
st.markdown("---")
st.caption("Powered by Context-Aware Dynamic Card Sorting Algorithm | MoES / IMD Prototype")