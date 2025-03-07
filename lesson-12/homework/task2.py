import sqlite3
import requests
from bs4 import BeautifulSoup

with sqlite3.connect('jobs.db') as con:
    cursor = con.cursor()
    query = "CREATE TABLE Jobs(Title text, Company text, Location text, Aplication_link text)"
    cursor.execute(query)

with sqlite3.connect('jobs.db') as con:
    cursor = con.cursor()
    request = requests.get('https://realpython.github.io/fake-jobs/')
    soup = BeautifulSoup(request.content, 'html.parser')
    postings = soup.find_all('div', class_='card-content')
    values = []
    for post in postings:
        title = post.find('h2', class_='title').text
        company = post.find('h3', class_='company').text
        location = post.find('p', class_='location').text
        application_link = post.find_all('a')[1].get('href')
        value = (title, company, location, application_link)
        values.append(value)

    cursor.executemany('Insert into Jobs Values(?, ?, ?, ?)', values)