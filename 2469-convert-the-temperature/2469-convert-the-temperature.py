class Solution:
    def convertTemperature(self, celsius):
        # tính nhiệt độ Kelvin
        kelvin = celsius + 273.15

        # tính nhiệt độ Fahrenheit
        fahrenheit = celsius * 1.80 + 32.00

        # trả về dưới dạng mảng [Kelvin, Fahrenheit]
        return [kelvin, fahrenheit]