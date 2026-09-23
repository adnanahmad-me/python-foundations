# Celsius → Fahrenheit : formula --> °F = (°C × 1.8) + 32
tempC=float(input("Enter temperature(°C): "))
tempF= (tempC*1.8)+32
print(f"{tempC}°C is equal to {tempF}°F.\n")

# Fahrenheit → Celsius : formula --> °C = (°F - 32) × (5 / 9)
tempF=float(input("Enter temperature(°F): "))
tempC= (tempF-32)*(5/9)
print(f"{tempF}°F is equal to {tempC}°C.")