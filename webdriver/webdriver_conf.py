import os
from selenium import webdriver
from pathlib import Path  # python3 only
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from pathlib import Path  # python3 only
env_path = Path('/home/roman/PycharmProjects/smmreports') / '.env'
load_dotenv(dotenv_path=env_path)


class Webdriver():
    def func_webdriver(): #todo переделать на класс, чтобы вызывая экземляр класса оставалась одна и та же сессия
        path = os.getenv('chrome_driver')
        options = Options()
        # options.binary_location = "usr/bin/google-chrome"
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--window-size=1500,1000")
        options.add_argument("--disable-notifications")

        # options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path=path, options=options)
        return driver
    driver = func_webdriver()


def main():
    driver = Webdriver().driver


if __name__ == '__main__':
    main()
