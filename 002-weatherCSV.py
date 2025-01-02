"""Created with gemini - still buggy"""

import requests
from bs4 import BeautifulSoup
import csv
import os

def get_weather_data(cep):
  """
  Scrapes weather data for a Brazilian city using its CEP from a website.

  Args:
    cep: The CEP of the city.

  Returns:
    A dictionary containing the weather data, or None if an error occurs.
  """
  try:
    # Use the CEP to get the city name 
    cep_api_url = f'https://viacep.com.br/ws/{cep}/json/'
    cep_response = requests.get(cep_api_url)
    cep_data = cep_response.json()

    if 'localidade' in cep_data:
      city_name = cep_data['localidade']

      # **Replace this with the URL of the weather website you want to scrape**
      #weather_url = f'https://www.example-weather-website.com/weather/{city_name}'  
      weather_url = f'https://www.accuweather.com/en/br/pelotas/35733/weather-forecast/35733'

      response = requests.get(weather_url)
      soup = BeautifulSoup(response.content, 'html.parser')

      # Add checks to see if the elements are found before accessing .text
      temperature_elem = soup.find('div', class_='temperature')
      if temperature_elem:
        temperature = temperature_elem.text.strip()
      else:
        temperature = "N/A"  # Or handle the error as you prefer

      humidity_elem = soup.find('span', id='humidity')
      if humidity_elem:
        humidity = humidity_elem.text.strip()
      else:
        humidity = "N/A"

      description_elem = soup.find('p', class_='weather-description')
      if description_elem:
        description = description_elem.text.strip()
      else:
        description = "N/A"

      weather_info = {
          'city': city_name,
          'temperature': temperature,
          'humidity': humidity,
          'description': description
      }
      return weather_info
    else:
      print("Invalid CEP.")
      return None

  except Exception as e:
    print(f"An error occurred: {e}")
    return None

def save_to_csv(weather_data, filename='weather_data.csv'):
  """
  Saves weather data to a CSV file.

  Args:
    weather_data: A dictionary containing the weather data.
    filename: The name of the CSV file.
  """
  try:
    # Check if the file exists
    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
      fieldnames = ['city', 'temperature', 'humidity', 'description']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

      # Write the header only if the file is new
      if not file_exists:
        writer.writeheader()

      writer.writerow(weather_data)
    print(f"Weather data saved to {filename}")

  except Exception as e:
    print(f"An error occurred while saving to CSV: {e}")

if __name__ == '__main__':
  cep = input("Enter the CEP of the Brazilian city: ")
  weather_data = get_weather_data(cep)
  if weather_data:
    save_to_csv(weather_data)
