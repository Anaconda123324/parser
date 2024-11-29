import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://mebel-v-koroleve.ru/shkafyi-v-koroleve'
    response = requests.get(url)
    print(response.status_code)
    # print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    spoon = soup.find_all('div', class_="product-card__info")
    print([i.text for i in spoon])

    with open('page.txt', 'a', encoding='UTF-8') as file:
        file.write(''.join([i.text for i in spoon]))

    with open('output.html', 'a', encoding='UTF-8') as file:        #достать страницу
        file.write(response.text)

    # soup = BeautifulSoup(response.text, 'html.parser')
    # part = soup.find('div', class_='text-container')
    # # print(part.text)
    # with open('page.txt', 'a', encoding='UTF-8') as file:       #достать сам текст из контейнера
    #     file.write(part.text)

    # with open('output.html', 'a', encoding='UTF-8') as file:        #достать страницу
    #     file.write(response.text)


if __name__ == '__main__':
    main()