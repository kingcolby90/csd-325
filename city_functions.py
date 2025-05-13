# city_functions.py#
# This module contains a function to format city and country names.
def city_country(city, country, population=None):
    if population:
        return f"{city}, {country} - population {population}"
    return f"{city}, {country}"
print(city_country("Santiago", "Chile"))
print(city_country("Santiago", "Chile", 5000000))
print(city_country("Santiago", "Chile", 5000000, "Spanish"))