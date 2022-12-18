
from bs4 import BeautifulSoup
import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0, private, must-revalidate',
    'cookie': 'ajs_anonymous_id=d597cdf8-6c9f-4eeb-afe2-8f53ff8f06bb; _angellist=ad40f9d6004c5cc2c3a6f9883a6b59af; _gid=GA1.2.478670641.1671364290; _fbp=fb.1.1671364290175.2091791927; _gcl_au=1.1.1597598821.1671364290; ln_or=eyI1MTA5NjIiOiJkIiwiMzY0NjY0NCI6ImQiLCIzNjQ2NjQ0LDUxMDk2MiI6ImQifQ==; _hjSessionUser_1444722=eyJpZCI6IjFjMWZiNjJlLWIwMzMtNWM4MC1iMjJiLWQ3MDI0YTA3ZDZkNCIsImNyZWF0ZWQiOjE2NzEzNjQyOTA1ODYsImV4aXN0aW5nIjp0cnVlfQ==; cookie-consent=1; g_state={"i_p":1671380084107,"i_l":1}; __stripe_mid=67ea874d-9c2b-405e-8543-211ff98bc7431e6d07; _hjSession_1444722=eyJpZCI6IjE1NTBkNjIxLTkwZmQtNDgxMC1hNTYwLTcyNGI1ZGFhYTlhMyIsImNyZWF0ZWQiOjE2NzEzODYxNjg3ODAsImluU2FtcGxlIjpmYWxzZX0=; _ga_705F94181H=GS1.1.1671386168.4.1.1671386477.59.0.0; _ga=GA1.1.1268127501.1671364290; datadome=tDvcAsyc9LFfd2Vbsq-03jU52Lux9KDHKGBk2Bk1Gri4P2LbjrAvxG5UriHlG4JhiUDlD8uBInWw3D9v-Mz9gzgmn~cMlV2unNJEleyVy_3bhqDR3McowIjDl0Nbktl',
}

def get_data(url):
    response = requests.get(url=url, headers=headers, timeout=5)
    print(response)

    soup = BeautifulSoup(response.text, 'lxml')
    try:
        user_name = soup.find('h1', class_="u-fontSize25 u-fontSize24SmOnly u-fontWeight500").text.strip()
    except:
        user_name = soup.find('h1', class_="u-fontSize32 u-fontSize24SmOnly u-fontWeight500 s-vgBottom0_5").text.strip()
    try:
        LinkedIn_profile = soup.find('a', class_="icon link_el fontello-linkedin")['href']
    except:
        LinkedIn_profile = 'None'
    print(f"{user_name}'s LinkedIn url: {LinkedIn_profile}")
    with open(file=f'{user_name}.txt', mode='w') as file:
        print(f"Cоздан '{user_name}.txt")
        file.write(f"{user_name}'s LinkedIn url: {LinkedIn_profile}")


def get_user_data(file):
    with open(file=file) as file:
        src = file.read()
        src_ = src.split('\n')
    with open(file=f'result.txt', mode='w') as file:
        i = 1
        for url in src_:
            print(url[:-1])
            response = requests.get(url=url[:-1], headers=headers, timeout=15)
            print(response)
            soup = BeautifulSoup(response.text, 'lxml')
            try:
                user_name = soup.find('h1', class_="u-fontSize25 u-fontSize24SmOnly u-fontWeight500").text.strip()
            except:
                user_name = soup.find('h1', class_="u-fontSize32 u-fontSize24SmOnly u-fontWeight500 s-vgBottom0_5").text.strip()
            try:
                LinkedIn_profile = soup.find('a', class_="icon link_el fontello-linkedin")['href']
            except:
                LinkedIn_profile = 'None'
            print(f"{i} - {user_name}'s LinkedIn url: {LinkedIn_profile}")
            print('=======')
            file.write(f"{i} - {user_name}'s LinkedIn url: {LinkedIn_profile}\n")
            i += 1
    print(f"Cоздан 'result.txt")

def main():
    input_ = None
    while not input_:
        option = input('1 - Использовать ссылку отдельного пользователя\n'
                       '2 - Использовать список ссылок из файла\n'
                       'Введите цифру: ')
        try:
            option = int(option)
        except:
            print('Пожалуйста, используйте только цифры "1" или "2"\n')
        if option == 1 or option == 2:
            input_ = True

    if option == 1:
        url = input('Введите url пользователя: ')
        get_data(url)
    if option == 2:
        print('!ВНИМАНИЕ!\n'
              'Файл должен иметь расширение .txt и каждая строка файла должна содержать ссылку на отдельный аккаунт пользователя!')
        file = input('Укажите путь к файлу: ')
        get_user_data(file)

if __name__ == '__main__':
    main()
