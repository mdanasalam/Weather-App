import requests

def get_weather(city, api_key):
    # OpenWeatherMap API URL for current weather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Send GET request to OpenWeatherMap API
        response = requests.get(url)
        
        # Print the raw response text for debugging
        print(response.text)  # This will print the raw response from the API

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()  # Parse the JSON response
            # Extract data from the response
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            # Display the weather data
            print(f"Weather in {city}: {weather}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"City {city} not found or invalid API key.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Replace with your OpenWeatherMap API key
    api_key = "23a1631c5357fb21b47c77fe23765958"
    
    # Ask the user to enter a city name
    city = input("Enter the city name: ")
    
    # Call the get_weather function
    get_weather(city, api_key)

if __name__ == "__main__":
    main()