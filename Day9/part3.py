countries = ["India", "France", "Japan", "Canada"]
capitals = ["New Delhi", "Paris", "Tokyo", "Ottawa"]
country_dict = dict(zip(countries, capitals))
country = input("Enter country name: ")
if country in country_dict:
    print(f"The capital of {country} is {country_dict[country]}.")