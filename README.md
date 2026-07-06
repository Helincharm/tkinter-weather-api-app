# Pixel Weather App

Pixel Weather App is a Python desktop application that displays real-time weather information using the OpenWeatherMap API. The project uses a pixel art themed interface built with Tkinter and dynamically changes the displayed scene according to the current weather condition.

This project was developed as a personal portfolio project to practice API integration, GUI development, environment-based API key management, and basic error handling in Python.

---

## Features

- Real-time weather data using OpenWeatherMap API
- Pixel art themed desktop interface
- Weather-based visual screens:
  - Sunny
  - Cloudy
  - Partly Cloudy
  - Rainy
  - Snowy
- Pixel-style temperature display on the interface
- Background music support with Pygame
- Image handling with Pillow
- API key protection using `.env` file
- Basic API error handling and status code checks
- Organized project structure for GitHub and portfolio usage

---

## Technologies Used

- Python
- Tkinter
- Requests
- Pillow
- Pygame
- Python Dotenv
- OpenWeatherMap API

---

## Project Structure

```txt
pixel-weather-app/
│
├── assets/
│   ├── images/
│   │   ├── sunny.png
│   │   ├── cloudy.png
│   │   ├── cloudy_sunny.png
│   │   ├── rainy.png
│   │   ├── snowy.png
│   │   └── screenshot.png
│   │
│   ├── sounds/
│   │   └── background_music.mp3
│   │
│   └── texts/
│       ├── sunny_text.png
│       ├── cloudy_text.png
│       ├── rainy_text.png
│       └── snowy_text.png
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/pixel-weather-app.git
```

Go to the project folder:

```bash
cd pixel-weather-app
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

This project uses the OpenWeatherMap API. To run the application, you need an API key.

Create a `.env` file in the project root directory:

```env
WEATHER_API_KEY=your_api_key_here
```

An example file is provided as `.env.example`:

```env
WEATHER_API_KEY=your_api_key_here
```

The real `.env` file is ignored by Git for security reasons and should not be uploaded to GitHub.

---

## Usage

Run the application with:

```bash
python tkinter-weather-api-app.py
```

After launching the app, the program sends a request to the OpenWeatherMap API and displays the current weather condition with a matching pixel art screen.

---

## How It Works

The application sends a request to the OpenWeatherMap current weather endpoint. The returned JSON data is processed to determine the current weather condition and temperature.

Example logic:

- If the API returns `Clear`, the sunny screen is displayed.
- If the API returns `Clouds`, a cloudy or partly cloudy screen is displayed.
- If the API returns `Rain`, `Drizzle`, or `Thunderstorm`, the rainy screen is displayed.
- If the API returns `Snow`, the snowy screen is displayed.

The temperature value is drawn on the Tkinter canvas using a custom pixel-style display.

---

## Screenshot

![Pixel Weather App Screenshot](assets/images/screenshot.png)

---

## Security

The API key is not written directly inside the source code. Instead, it is stored in a local `.env` file.

The `.gitignore` file prevents sensitive and unnecessary files from being uploaded:

```gitignore
.env
__pycache__/
*.pyc
```

This keeps the API key private while still allowing other users to run the project by creating their own `.env` file.

---

## What I Practiced

While developing this project, I practiced:

- Building a desktop GUI with Tkinter
- Working with external APIs
- Sending HTTP requests with Python
- Reading and processing JSON data
- Managing images with Pillow
- Playing background music with Pygame
- Using environment variables for API key security
- Handling API errors and invalid responses
- Preparing a project for GitHub and portfolio presentation

---

## Future Improvements

Possible improvements for future versions:

- Add city search input
- Add location-based weather detection
- Add 5-day weather forecast
- Add animated weather effects
- Add sound on/off settings
- Add multiple theme options
- Improve UI responsiveness
- Package the project as an executable application

---

## Project Status

The core version of the project is completed. Future updates may include city selection, forecast support, and additional animations.