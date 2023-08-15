"""
IMDB Rating
"""
import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top"
response = requests.get(url)
html_index = response.content

soup = BeautifulSoup(html_index,"html.parser")

a = float(input("Rating eingeben:"))

tit = soup.find_all("td", {"class":"titleColumn"})
ratings = soup.find_all("td", {"class":{"ratingColumn imdbRating"}})

for title, rating in zip(tit,ratings):
    title = title.text
    rating = rating.text

    title = title.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating)>a):
        print("Name: {} Rating: {}".format(title,rating))
