import os

# Create backend directory structure if needed
os.makedirs("backend", exist_ok=True)

# 1. package.json
package_json = """{
  "name": "mausam-ai-backend",
  "version": "1.0.0",
  "description": "Backend API for Mausam AI Pro - Fetching Weather, AQI & Forecast",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "dotenv": "^16.3.1",
    "express": "^4.18.2",
    "node-fetch": "^2.7.0"
  }
}
"""

with open("package.json", "w", encoding="utf-8") as f:
    f.write(package_json)

# 2. .env.example
env_example = """# OpenWeatherMap API Key (Get a free key from https://openweathermap.org/api)
OPENWEATHER_API_KEY=your_openweather_api_key_here
PORT=5000
"""

with open(".env.example", "w", encoding="utf-8") as f:
    f.write(env_example)

# 3. server.js (Node.js Express Backend)
server_js = """const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 5000;
const API_KEY = process.env.OPENWEATHER_API_KEY;

// Endpoint 1: Health Check
app.get('/', (req, res) => {
    res.json({ status: "ok", message: "Mausam AI Pro Backend is running smoothly!" });
});

// Endpoint 2: Fetch Current Weather, AQI & Forecast by Lat/Lon
app.get('/api/weather', async (req, res) => {
    try {
        const { lat, lon } = req.query;

        if (!lat || !lon) {
            return res.status(400).json({ error: "Latitude (lat) and Longitude (lon) are required." });
        }

        if (!API_KEY) {
            return res.status(500).json({ error: "OPENWEATHER_API_KEY is missing in backend environment variables." });
        }

        // Fetch Current Weather
        const weatherUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${API_KEY}`;
        const weatherRes = await fetch(weatherUrl);
        const weatherData = await weatherRes.json();

        // Fetch AQI Data
        const aqiUrl = `https://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${API_KEY}`;
        const aqiRes = await fetch(aqiUrl);
        const aqiData = await aqiRes.json();

        // Fetch 5 Day / 3 Hour Forecast
        const forecastUrl = `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&units=metric&appid=${API_KEY}`;
        const forecastRes = await fetch(forecastUrl);
        const forecastData = await forecastRes.json();

        res.json({
            weather: weatherData,
            aqi: aqiData,
            forecast: forecastData
        });

    } catch (error) {
        console.error("Backend Weather Fetch Error:", error);
        res.status(500).json({ error: "Failed to fetch real-time weather data from OpenWeather API." });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
"""

with open("server.js", "w", encoding="utf-8") as f:
    f.write(server_js)

print("Backend files generated successfully!")
