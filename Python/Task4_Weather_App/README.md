# Basic Weather App

## Project Description
The Basic Weather App is a Python application that retrieves real-time weather information for a city using the OpenWeatherMap API.

## Features
- Accepts a city name from the user.
- Fetches live weather information.
- Displays temperature.
- Displays weather conditions.
- Shows humidity and other weather details.
- Uses an API key stored securely in an environment file.

## Technologies Used
- Python 3
- Requests
- Python-dotenv
- OpenWeatherMap API

## Installation
Install the required libraries:

pip install requests python-dotenv

## How to Run
1. Download or clone this repository.
2. Install the required libraries.
3. Create a `.env` file in the project folder.
4. Add your API key:

API_KEY=your_api_key

5. Run the application:

python weather_app.py

## Security
The `.env` file is excluded using `.gitignore` to protect the API key.

## Internship
Oasis Infobyte – Python Programming Internship
