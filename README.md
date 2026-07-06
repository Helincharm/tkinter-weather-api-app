## Author

Developed by Helincharm as a personal Python portfolio project.

 # Pixel Weather App.

---
Pixel Weather App is a Python desktop application that displays real-time weather information with a pixel art themed interface. The application uses the OpenWeatherMap API to retrieve current weather data and updates the visual scene based on the current weather condition.

This project was developed as a personal portfolio project to demonstrate API integration, GUI development, JSON data processing, asset management, and basic error handling in Python.

---

## Features

- Real-time weather data using OpenWeatherMap API
- Pixel art themed desktop interface
- Weather-based visual screens
- Custom pixel-style temperature display
- Background music support
- Image rendering with Pillow
- API response handling and status code control
- Organized asset structure for images, sounds, and text graphics

---

## Weather Conditions Supported

The application changes the interface according to the weather data returned by the API:

- `Clear` → Sunny screen
- `Clouds` → Cloudy or partly cloudy screen
- `Rain`, `Drizzle`, `Thunderstorm` → Rainy screen
- `Snow` → Snowy screen

The current temperature is displayed on the screen using a custom pixel-style drawing system.

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
tkinter-weather-api-app/
│
├── assets/
│   ├── images/
│   ├── sounds/
│   └── texts/
│
├── tkinter-weather-api-app.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Helincharm/tkinter-weather-api-app.git
```

Go to the project folder:

```bash
cd tkinter-weather-api-app
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## API Key Configuration

This project uses the OpenWeatherMap API.

An example configuration file is included in the repository:

```txt
.env.example
```

```

To run the project, replace `your_api_key_here` with your own OpenWeatherMap API key.

You can create an API key from OpenWeatherMap:

```txt
https://openweathermap.org/
```

This repository does not include a real API key.

---

## Usage

Run the application with:

```bash
python tkinter-weather-api-app.py
```

After launching, the application sends a request to the OpenWeatherMap API and displays the current weather condition with a matching pixel art screen.

---

## How It Works

The application sends an HTTP request to the OpenWeatherMap current weather endpoint. The returned JSON response is processed to extract the weather condition and temperature value.

The main weather condition determines which visual screen is displayed. The temperature value is then drawn on the Tkinter canvas using a custom pixel-style text rendering system.

---

## Skills Demonstrated

This project demonstrates practical experience with:

- Python desktop application development
- GUI programming with Tkinter
- Working with external APIs
- Sending HTTP requests
- Processing JSON responses
- Managing image assets with Pillow
- Using audio in a Python application with Pygame
- Handling API errors and invalid responses
- Structuring a project for GitHub and portfolio use


---

## License

This project is shared publicly for portfolio and review purposes.

Reuse, redistribution, or modification is not permitted without explicit permission.