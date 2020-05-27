from projects import kans, beautymarket
from webdriver import webdriver_conf


def main():
    driver = webdriver_conf.Webdriver.driver
    try:
        beautymarket.main()
    except Exception as exc:
        print('\n-----------------------------------------------'), \
        print(exc), \
        print('\n-----------------------------------------------')

    try:
        kans.main()
    except Exception as exc:
        print('\n-----------------------------------------------'), \
        print(exc), \
        print('\n-----------------------------------------------')

    driver.close()


if __name__ == "__main__":
    main()