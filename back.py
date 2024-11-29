import csv
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
url = "https://www.indianhealthyrecipes.com/"
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.content, 'html.parser')
recipes = soup.find_all('div', class_='kt-blocks-post-grid-item-inner')
print(recipes)
title = []
links = []
for de in recipes:
        titles = de.find('h2', class_='entry-title').text.strip()
        title.append(titles)
        link = de.find('a', href=True)['href']
        links.append(link)
title = []
links = []
for de in recipes:
        titles = de.find('h2', class_='entry-title').text.strip()
        title.append(titles)
        link = de.find('a', href=True)['href']
        links.append(link)
new_links = []
for k in links:
    response_recipe = requests.get(k)
    if response_recipe != 403:
        new_links.append(k)
# with open('recipes.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Title', 'Ingredients', 'Instructions'])
#     for i in new_links:
        r = requests.get('https://www.indianhealthyrecipes.com/chana-masala')
        soup = BeautifulSoup(r.content, 'html.parser')
        titles = soup.find_all('h1', class_='entry-title')
        for title in titles:
            title_text = [title.text.strip()]
            ingredients = soup.find_all('div' ,class_='wprm-recipe-ingredient-group')
        for ingredient in ingredients:
            ingredient_text = [ingredient.text.strip()]
            soup = BeautifulSoup(r.content, 'html.parser')
            instruction = soup.find_all('ul' ,class_='wprm-recipe-instructions')
        for instructions in instruction:
            instruction_text = [instructions.text.strip()]
            print(instruction_text)
        # writer.writerow([title_text, ', '.join(ingredient_text), ', '.join(instruction_text)])
    