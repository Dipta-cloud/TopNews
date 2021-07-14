import pycountry
import requests

api_key = "12c5418dc1fa47fe9c6af9119dc9bc67"
country = input("enter country name: ")
try:
    country_code = pycountry.countries.search_fuzzy(country)[0].alpha_2
except LookupError:
    raise ValueError("Country not recognized!")

try:
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country={country_code.lower()}&apiKey={api_key}")
except KeyError:
    raise ValueError("I don't recognize this country. Most likely, it is not supported")
else:
    data = response.json()
    if data["totalResults"] == 0:
        raise ValueError("I don't recognize this country. Most likely, it is not supported")
    for i in range(15):
        news = data['articles'][i]['title']
        print(i + 1, news)