## linkedin https://www.linkedin.com/posts/noor-fatima-2501b240a_well-thats-the-task-of-intermediate-difficulty-activity-7492205692741685248-xvDI?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGhS9dwBbGp1DjhFPZGT0Q7ib3ko4pit5Yk

# Weather App 🌤️

## Overview

The Weather App is a Python-based application that fetches **real-time weather information** for a city using the OpenWeather API.

The application uses the `requests` library to send API requests and displays important weather details such as temperature, humidity, and weather conditions.

## Objective

The objective of this project is to learn how to:

* Work with a weather API
* Send HTTP requests using Python
* Process JSON API responses
* Take user input
* Display real-time weather information
* Handle API and connection errors

## Features

* 🌍 Enter any city name
* 🌡️ Display current temperature
* 💧 Display humidity
* ☁️ Display current weather condition
* 🔄 Fetch real-time weather data
* ⚠️ Handle invalid city names
* 🛑 Handle connection/API errors

## Technologies Used

* **Python**
* **Requests**
* **OpenWeather API**

## Installation

### 1. Install Python

Make sure Python is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Install Requests

Open a terminal in the project folder and run:

```bash
pip install requests
```

Or install all dependencies using:

```bash
pip install -r requirements.txt
```

## API Key Setup

This project uses the **OpenWeather API**.

Create an account on OpenWeather and obtain an API key.

Then add your API key to the Python program:

```python
API_KEY = "YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your actual API key.

**Do not share or upload your API key publicly.**

## How to Run

Run the application using:

```bash
python app.py
```

The program will ask you to enter a city name:

```text
================================
       WEATHER APP
================================
Enter city name: Lahore
```

The application will then fetch and display the current weather information.

## Example Output

```text
===================================
        WEATHER INFORMATION
===================================
City        : Lahore, PK
Temperature : 31.5°C
Humidity    : 58%
Condition   : Clear Sky
===================================
```

The actual temperature, humidity, and weather condition will change according to the current weather.

## Error Handling

The application handles common problems such as:

* Invalid city names
* Empty city input
* Internet connection problems
* API request errors
* Invalid API responses

For example:

```text
Enter city name: xyzabc

City not found. Please check the city name.
```

## Learning Outcomes

By completing this project, I learned how to:

* Use the `requests` library
* Work with REST APIs
* Send GET requests
* Use API parameters
* Read JSON data
* Extract specific values from API responses
* Handle exceptions in Python
* Build a simple real-time API-based application

## Future Improvements

Possible improvements include:

* Add a graphical user interface
* Display weather icons
* Add a 5-day forecast
* Show wind speed and pressure
* Add automatic location detection
* Store recent searches
* Deploy the application online

## License

This project was created for educational and internship purposes.
