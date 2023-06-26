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


class CWParser:
    def __init__(self):
        self.user = os.getenv('CODEWARS_USER')
        self.email = os.getenv("CODEWARS_EMAIL")
        self.password = os.getenv('CODEWARS_PASSWORD')
        # Создание объекта драйвера
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=Options()))

    def _auth(self):
        # Авторизация
        url = "https://www.codewars.com/users/sign_in"
        self.browser.get(url=url)
        input_email = self.browser.find_element(By.ID, "user_email")
        input_password = self.browser.find_element(By.ID, "user_password")
        input_email.clear()
        input_password.clear()
        input_email.send_keys(os.getenv("CODEWARS_EMAIL"))
        input_password.send_keys(os.getenv('CODEWARS_PASSWORD'))
        input_password.send_keys(Keys.ENTER)

    def _check_old(self, new_katas):
        d=[]
        # Проверяем парсились ли уже задачи
        if Path("data.json").exists():
            with open('data.json') as file:
                d = json.load(file)
            for k in d:
                if k in new_katas:
                    del new_katas[k]
        with open('data.json', 'w') as file:
            d.extend(new_katas)
            json.dump(d, file, indent=4, ensure_ascii=False)
        return new_katas

    def _get_total_pages(self):
        """Возвращает количество страниц, на которых есть данные"""
        url = f"https://www.codewars.com/api/v1/users/{self.user}/code-challenges/completed?page=0"
        return requests.get(url).json()["totalPages"]

    def _make_list_completed_challenges(self):
        # Возвращает список решенных задач
        resp = []
        for page in range(self._get_total_pages()):
            url = f"https://www.codewars.com/api/v1/users/{self.user}/code-challenges/completed?page={page}"
            resp.extend(requests.get(url).json()['data'])
        return self._check_old(resp)

    def parse(self):
        self._auth()
        count = 0
        for i in self._make_list_completed_challenges():
            count += 1
            url = f"https://www.codewars.com/kata/{i['id']}/train/python"
            self.browser.get(url=url)
            time.sleep(2)
            html = self.browser.page_source

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


if __name__ == '__main__':
    CWParser().parse()
