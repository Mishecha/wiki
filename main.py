import requests
from bs4 import BeautifulSoup
from docx import Document

def parse_wikipedia_article(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Ошибка при получении статьи")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    doc = Document()

    title = soup.find(id="firstHeading").text
    doc.add_heading(title, 0)

    doc.save('wikipedia_article.docx')

url = input("Введите ссылку на статью Википедии: ")
parse_wikipedia_article(url)