import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://tl.rulate.ru/book/16292/327323/ready_new'
    response = requests.get(url)
    print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    part = soup.find('div', class_='text-container')
    # print(part.text)
    with open('page.txt', 'a', encoding='UTF-8') as file:       #достать сам текст из контейнера
        file.write(part.text)

    with open('output.html', 'a', encoding='UTF-8') as file:        #достать страницу
        file.write(response.text)


if __name__ == '__main__':
    main()