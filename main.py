import requests


def main():
    url = 'https://www.52shuku.vip/yanqing/hx4r_2828.html'
    response = requests.get(url)
    print(response.status_code)
    with open('output.html', 'a', encoding='UTF-8') as file:
        file.write(response.text)


if __name__ == '__main__':
    main()