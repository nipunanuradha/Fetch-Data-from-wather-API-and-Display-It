# 🌤️ WeatherPro Elite Max v10.0

**WeatherPro Elite Max** is a professional-grade, full-stack weather analytics dashboard designed to provide hyper-local real-time weather data, environmental intelligence, and personal planning tools. Built with a focus on high-performance API integration and a seamless UI/UX, it serves as a complete weather command center.

---

## 🚀 Key Features

### 📡 Advanced Visualizations
* **Live Satellite View:** Integrated **Windy API** for real-time cloud and atmospheric motion tracking.
* **Interactive Street Maps:** **Google Maps** integration to visualize precise city locations.
* **Dynamic Analytics:** Interactive **24-hour variation graphs** and **7-day historical trends** using Chart.js.

### 🍃 Environmental Intelligence
* **Detailed AQI Dashboard:** Comprehensive tracking of air quality parameters including **CO, NO2, O3, SO2, PM2.5, and PM10**.
* **Weather Parameters:** Real-time monitoring of UV Index, Humidity, Visibility, and Atmospheric Pressure.

### 🔔 Smart Alert System
* **Multi-Channel Notifications:** Instant **SMS alerts via Twilio**, **Email notifications via SMTP**, and native **Browser Desktop Alerts** for severe weather conditions.

### 🎙️ Interactive & Global Tools
* **Voice Search:** Hands-free weather queries using built-in speech recognition support for multiple languages.
* **Multi-language Support:** Fully localized in **English, Sinhala, Tamil, French, and Spanish**.
* **Global Market Widget:** Real-time **Currency Converter (USD to LKR)** and Timezone-aware live clocks.

### 📅 Lifestyle & Planning
* **Weather-Smart Planner:** An intelligent event manager that cross-references your schedule with local rain probabilities.
* **Celestial Tracking:** Live tracking of **Sunrise/Sunset** and **Moonrise/Moonset** cycles.
* **Live World News:** Automatic hourly updates of global weather and climate news with image thumbnails.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Flask (Web Framework)
* **Frontend:** JavaScript (ES6+), HTML5, Tailwind CSS
* **Data Visualization:** Chart.js
* **APIs:** WeatherAPI (Core Data), NewsAPI (News), Windy (Satellite), Google Maps (GIS)
* **Infrastructure:** Gunicorn (WSGI Server), Render (Deployment)
* **PWA:** Progressive Web App support for Android/iOS installation.

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/WeatherPro-Elite-Max.git](https://github.com/your-username/WeatherPro-Elite-Max.git)
cd WeatherPro-Elite-Max

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

### 3. Environment Configuration

Create a `.env` file in the root directory and add your API credentials:

```env
WEATHER_API_KEY=your_weatherapi_key
NEWS_API_KEY=your_newsapi_key
TWILIO_SID=your_sid
TWILIO_TOKEN=your_token
TWILIO_PHONE=your_twilio_number
EMAIL_USER=your_email
EMAIL_PASS=your_app_password

```

### 4. Run Locally

```bash
python app.py

```

Open `http://127.0.0.1:5000` in your browser.

```
live site - https://weatherpro-elite-max.onrender.com

---

## 📱 Mobile Support (PWA)

This application is fully optimized for mobile devices. To use it as an app:

1. Open the live URL in your mobile browser.
2. Select "Add to Home Screen" or "Install App" from the browser menu.
3. The app will be added to your app drawer as a standalone application.

---

## 🤝 Contribution

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page].
---

**Developed with ❤️ by Anuradha** [LinkedIn](https://www.linkedin.com/in/anuradha-athukorala)
