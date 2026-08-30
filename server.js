const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 5000;
const API_KEY = process.env.OPENWEATHER_API_KEY || "6ba3dd63fbaf16dcef89efbf48338170";

app.get('/', (req, res) => {
    res.json({ status: "ok", message: "Mausam AI Pro Backend is Running!" });
});

app.get('/api/weather', async (req, res) => {
    try {
        const { lat, lon } = req.query;
        if (!lat || !lon) return res.status(400).json({ error: "Lat and Lon required" });

        const weatherUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${API_KEY}`;
        const aqiUrl = `https://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${API_KEY}`;
        const forecastUrl = `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&units=metric&appid=${API_KEY}`;

        const [wRes, aRes, fRes] = await Promise.all([
            fetch(weatherUrl), fetch(aqiUrl), fetch(forecastUrl)
        ]);

        const weather = await wRes.json();
        const aqi = await aRes.json();
        const forecast = await fRes.json();

        res.json({ weather, aqi, forecast });
    } catch (err) {
        res.status(500).json({ error: "Failed to fetch weather data" });
    }
});

app.listen(PORT, () => console.log(`Server on port ${PORT}`));
