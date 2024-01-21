'''Crop Monitoring System
Imagine you are developing a Crop Monitoring System for farmers. Write a Python function 
monitor_crop(temperature, humidity, rainfall) that takes environmental conditions as input and returns 
"Watering needed" if the humidity is low and rainfall is below average, and "Optimal conditions" 
otherwise.'''
#Normal temperature 25, Humidity 50% and rainfall aaverage is 135
def monitor_crop(temperature, humidity, rainfall):
    #water need
    if temperature==25 and humidity==50 and rainfall==135:
        return "Balnce water"
    elif temperature>=25 and humidity>=50 and rainfall>=135:
        return "Balance Water"
    elif  temperature<=25 and humidity<=50 and rainfall<=135:
        return "More Water need"
    elif  temperature>=25 and humidity<=50 and rainfall<=135:
        return "More Water need"
    elif temperature<=25 and humidity>=50 and rainfall>=135:
        return "Balance water"
    elif  temperature<=25 and humidity>=50 and rainfall<=135:
        return "More water Need"
    elif temperature>=25 and humidity<=50 and rainfall>=135:
        return "Balance Water"
    elif  temperature>=25 and humidity>=50 and rainfall<=135:
        return "More Water need"
    elif  temperature<=25 and humidity<=50 and rainfall>=135:
        return "Balance Water"
temperature=int(input("Enter Temperature: "))
humidity=int(input("Enter Humidity: "))
rainfall=int(input("Enter rainfall: "))
result=monitor_crop(temperature, humidity, rainfall)
print(result)