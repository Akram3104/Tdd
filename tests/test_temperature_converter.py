import pytest
from temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius, fahrenheit_to_kelvin, kelvin_to_fahrenheit

@pytest.mark.parametrize("input_temp, expected_output", [
    (0, 32),
    (100, 212),
    (-40, -40)
])
def test_celsius_to_fahrenheit(input_temp, expected_output):
    assert celsius_to_fahrenheit(input_temp) == expected_output

@pytest.mark.parametrize("input_temp, expected_output", [
    (32, 0),
    (212, 100),
    (-40, -40)
])
def test_fahrenheit_to_celsius(input_temp, expected_output):
    assert fahrenheit_to_celsius(input_temp) == expected_output

@pytest.mark.parametrize("input_temp, expected_output", [
    (0, 273.15),
    (100, 373.15),
    (-273.15, 0)
])
def test_celsius_to_kelvin(input_temp, expected_output):
    assert celsius_to_kelvin(input_temp) == expected_output

@pytest.mark.parametrize("input_temp, expected_output", [
    (273.15, 0),
    (373.15, 100),
    (0, -273.15)
])
def test_kelvin_to_celsius(input_temp, expected_output):
    assert kelvin_to_celsius(input_temp) == expected_output

@pytest.mark.parametrize("input_temp, expected_output", [
    (32, 273.15),
    (212, 373.15),
    (-459.67, 0)
])
def test_fahrenheit_to_kelvin(input_temp, expected_output):
    assert fahrenheit_to_kelvin(input_temp) == expected_output

@pytest.mark.parametrize("input_temp, expected_output", [
    (273.15, 32),
    (373.15, 212),
    (0, -459.67)
])
def test_kelvin_to_fahrenheit(input_temp, expected_output):
    assert kelvin_to_fahrenheit(input_temp) == expected_output
