import requests
from bs4 import BeautifulSoup
from flask import Flask

schoolURL = "https://school.busanedu.net/pcs-h/main.do"

async def getMeal():
    res = requests.get(schoolURL)
    soup = BeautifulSoup(res.content, 'html.parser')
    mealList = soup.select_one('.meal_list').text
    return mealList
