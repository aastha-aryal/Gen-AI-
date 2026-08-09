import json
import os
import requests
from dotenv import load_dotenv

# Load API key safely from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


# fetch current weather using WeatherAPI
def get_weather_condition(city="Kathmandu"):
  url = "http://api.weatherapi.com/v1/current.json"
  params = {"key": API_KEY, "q": city, "aqi": "no"}

  try:
    response = requests.get(url, params=params, timeout=5)
    if response.status_code == 200:
      data = response.json()
      return data["current"]["condition"]["text"]
  except Exception as e:
    print(f"Weather API error: {e}")

  return "Unknown"


# 2. Function to build the daily routine list
def create_daily_routine():
  weather = get_weather_condition("Kathmandu")
  print(f"\nCurrent Weather in Kathmandu: {weather}")

  routine = []

  # Predefined task list
  tasks_to_schedule = [
      {
          "time": "07:00 AM",
          "activity": "Morning Exercise",
          "type": "outdoor",
          "priority": "High",
      },
      {
          "time": "09:00 AM",
          "activity": "Python API Coding Session",
          "type": "indoor",
          "priority": "High",
      },
      {
          "time": "02:00 PM",
          "activity": "Study GenAI Concepts & Prompting",
          "type": "indoor",
          "priority": "Medium",
      },
      {
          "time": "05:00 PM",
          "activity": "Evening Walk",
          "type": "outdoor",
          "priority": "Low",
      },
  ]

  # Loop through tasks and apply basic weather logic
  for item in tasks_to_schedule:
    status = "Scheduled"
    note = ""

    # If it's raining, flag outdoor activities
    if "rain" in weather.lower() and item["type"] == "outdoor":
      status = "Modified"
      note = "Rain alert! Consider shifting to indoor exercise/reading."

    routine.append({
        "time": item["time"],
        "activity": item["activity"],
        "priority": item["priority"],
        "status": status,
        "note": note,
    })

  return routine


# save routine to a JSON file
def save_routine_to_json(routine_data, filename="my_routine.json"):
  try:
    with open(filename, "w", encoding="utf-8") as file:
      json.dump(routine_data, file, indent=4)
    print(f"\nRoutine successfully generated and saved to '{filename}'!")
  except IOError as e:
    print(f"Error saving file: {e}")


# Main Execution Block
if __name__ == "__main__":
  my_routine = create_daily_routine()

  # Print formatted output to console
  print("\n--- YOUR GENERATED DAILY ROUTINE ---")
  for slot in my_routine:
    print(
        f"[{slot['time']}] {slot['activity']} ({slot['priority']} Priority)"
    )
    if slot["note"]:
      print(f"   ⚠️  Note: {slot['note']}")


  save_routine_to_json(my_routine)