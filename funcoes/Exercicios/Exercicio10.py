def celsius_para_fahrenheit():
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius}°C equivalem a {fahrenheit:.1f}°F.")

celsius_para_fahrenheit()