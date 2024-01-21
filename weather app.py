"""Weather App
Imagine building a Weather App. Write a function weather_advice(temperature, precipitation) that 
provides advice based on the current weather conditions. If it's hot and sunny, suggest wearing 
sunscreen; if it's raining, recommend carrying an umbrella; and if it's cold, suggest dressing warmly"""
temperature=int(input("Enter Temperature: "))
precipitation=input("Enter Precipitation (Rain,Snow,NO): ")
def weather_advice(temperature,precipitation):
    if temperature>34 and precipitation=="No":
        return """Sunny weather 
Use light-weight and breathable fabrics, such as cotton.
Choose light colors because they help in feeling less heat in hot weather."""
    elif temperature<25 and precipitation=="Rain":
        return """cool and rainy day 
Go outside with an umbrella. 
Use waterproof and quick-dry fabrics.
Use an umbrella and raincoat."""
    elif temperature<10 and precipitation=="Snow":
        return """Winter
Use heavy fabrics, such as wool.
Utilize layering so that you can adjust your clothes.
Use warm accessories like gloves, scarf, and cap."""
result=weather_advice(temperature,precipitation)
print(result)










