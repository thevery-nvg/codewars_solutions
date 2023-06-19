import os
import requests
import json
import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from bs4 import BeautifulSoup

user = os.getenv('CODEWARS_USER')


def get_total_pages():
    """Возвращает количество страниц, на которых есть данные"""
    url = f"https://www.codewars.com/api/v1/users/{user}/code-challenges/completed?page=0"
    return requests.get(url).json()["totalPages"]


def make_list_completed_challenges():
    resp = []
    for page in range(get_total_pages()):
        url = f"https://www.codewars.com/api/v1/users/{user}/code-challenges/completed?page={page}"
        resp.extend(requests.get(url).json()['data'])
    if Path("D:\\Python\\codewars_solutions\\data.json").exists():
        with open('data.json') as file:
            old_data = json.load(file)
        for k in old_data:
            if k in resp:
                del resp[k]
        with open('new_data.json', 'w') as file:
            json.dump(resp, file, indent=4, ensure_ascii=False)
    else:
        with open(f'data.json', 'w') as file:
            json.dump(resp, file, indent=4, ensure_ascii=False)


def parse_katas():
    # Создание объекта драйвера
    options = Options()
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=options))

    # Авторизация
    url = "https://www.codewars.com/users/sign_in"
    browser.get(url=url)
    input_email = browser.find_element(By.ID, "user_email")
    input_password = browser.find_element(By.ID, "user_password")
    input_email.clear()
    input_password.clear()
    input_email.send_keys(os.getenv("CODEWARS_EMAIL"))
    input_password.send_keys(os.getenv('CODEWARS_PASSWORD'))
    input_password.send_keys(Keys.ENTER)

    # Сохраняем решенные задачи по папкам
    count = 0
    if Path("D:\\Python\\codewars_solutions\\new_data.json").exists():
        with open('new_data.json') as file:
            d = json.load(file)
        Path("D:\\Python\\codewars_solutions\\new_data.json").unlink()
        with open('data.json') as file:
            old = json.load(file)
        with open('data.json', 'w') as file:
            old.extend(d)
            json.dump(old, file, indent=4, ensure_ascii=False)

    else:
        with open('data.json') as file:
            d = json.load(file)
    for i in d:
        count += 1
        url = f"https://www.codewars.com/kata/{i['id']}/train/python"
        browser.get(url=url)
        time.sleep(2)
        html = browser.page_source

        soup = BeautifulSoup(html, 'lxml')
        if soup is None:
            continue
        code = soup.find('pre', class_="p-2 my-2 border overflow-x-auto")

        for color in ['white', 'yellow', 'blue', 'purple', 'black', 'red']:
            rank = soup.find('div', class_=f"small-hex is-extra-wide is-{color}-rank")
            if rank is not None:
                break
        try:
            rank = rank.find(class_="inner-small-hex").find('span').text.replace(' ', '_')
        except:
            print(f"{count=} ERROR {i['slug']}\n{url}")
            with open(f'{count}_error_{i["id"]}.html', 'w') as file:
                file.write(html)
            continue
        data = f"\n'''{url}'''\n\n\n{code.text}"
        name = re.sub(r'[\:\*\?\<\>\|\+\.\,\^]', '', i['slug'])
        path = Path.cwd()
        if not path.joinpath(f'{rank}').exists():
            path.joinpath(f'{rank}').mkdir()
        with open(f"{rank}\\{name}.py", 'w', encoding='utf-8') as file:
            file.write(data)
        print(f"Completed solution #{count} {name=}\n{url}")


def main():
    make_list_completed_challenges()
    parse_katas()


if __name__ == '__main__':
    main()
