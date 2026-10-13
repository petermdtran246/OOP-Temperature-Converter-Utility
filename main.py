class TemperatureConverter:
    @staticmethod
    def celcius_to_fahrenheit(celcius):
        return (celcius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celcius(farenheit):
        return (farenheit - 32) * 5/9
    @staticmethod
    def celcius_to_kelvin(celcius):
        return celcius + 273.15

    @staticmethod
    def kelvin_to_celcius(kelvin):
        return kelvin - 273.15
   
print(f'{TemperatureConverter.celcius_to_fahrenheit(100):.0f}')
print(f'{TemperatureConverter.fahrenheit_to_celcius(50):.0f}')
print(f'{TemperatureConverter.celcius_to_kelvin(300):.0f}')
print(f'{TemperatureConverter.kelvin_to_celcius(200):.0f}')