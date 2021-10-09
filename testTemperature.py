from unittest import TestCase, main
from temperature import Temperature

class TestTemperature(TestCase):
    def test_celsiusToKelvinA(self):
        A = Temperature(celsius=35).kelvin
        B = 35 + 273.15
        self.assertEqual(A, B)
    
    def test_celsiusToKelvinB(self):
        A = Temperature(celsius=32).kelvin
        B = 32 + 273.15
        self.assertEqual(A, B)

    def test_fahrenheitToKelvinA(self):
        A = Temperature(fahrenheit=32).kelvin
        B = 273.15
        self.assertEqual(A, B)

    def test_fahrenheitToKelvinB(self):
        A = Temperature(fahrenheit=35.33).kelvin
        B = 275
        self.assertEqual(A, B)
    

if __name__ == "__main__":
    main()