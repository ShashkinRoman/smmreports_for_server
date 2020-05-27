import os
from distutils.command.config import config
from time import sleep
from webdriver import webdriver_conf
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from modules import config
# from data_parse import fb_authorization
load_dotenv()


# не считаются первые 6 диалогов
def first_scrolling(driver):  # todo клик перенести в мейн, здесь оставить только скролл, разбить на первый скрол и последующие
    scroll = driver.find_element_by_xpath(
        '//*[@id="u_0_u"]/div/div/div/table/tbody/tr/td[2]/div/div/div[2]/div/div/div/div[2]/div/div[9]/div')
    scroll.click()


# 1 страница 9 диалогов и 18 скролов
def scrolling(driver):
    scroll = driver.find_element_by_xpath(
        '//*[@id="u_0_u"]/div/div/div/table/tbody/tr/td[2]/div/div/div[2]/div/div/div/div[2]/div/div[10]/div')
    for i in range(0, 19):
        scroll.send_keys(Keys.ARROW_DOWN)
        sleep(0.5)
    print('end scroll')


# ищем все даты элементов на странице
def find_leads(driver):
    driver = driver
    leads = driver.find_elements_by_class_name('timestamp')
    return leads


# считаем количество всех лидов за указанную дату
#todo add count leads: for everything leads save title in list and scroll. after scroll chek have title in list.
# if have dont add, and returned len(list)
def count_leads(counter=0):
    end_sheck = 0
    counter_funk = counter
    driver = webdriver_conf.Webdriver().driver
    weekday = config.Weekday()
    yesterday = weekday.text_day(weekday.yesterday_datetime)
    day_before_yesterday = weekday.text_day(weekday.day_before_yesterday_datetime)
    leads = find_leads(driver)
    for lead in leads:
        if lead.get_attribute('title') == yesterday:
            counter_funk += 1
        if lead.get_attribute('title') == day_before_yesterday:
            # print(counter_funk)
            end_sheck = 1
    else:
        if end_sheck == 1:
            leads_func = Leads().leads
            leads_func.clear()
            leads_func.append(str(counter_funk))
            return 1
        scrolling(driver)
        counter += count_leads(counter_funk)
    return 1
    # if counter_funk > 0:
    #     scrolling(driver)
    #     count_leads(driver, yesterday, day_before_yesterday, counter)
    # scrolling(driver)
    # count_leads(driver, yesterday, day_before_yesterday, counter)


class Leads():
    leads = []


def parse_chat(driver, direct_url):
    # fb_authorization(driver)
    driver.get(direct_url)
    # weekday = Weekday()
    # yesterday = weekday.text_day(weekday.yesterday_datetime)
    # day_before_yesterday = weekday.text_day(weekday.day_before_yesterday_datetime)
    sleep(2)
    first_scrolling(driver)
    lead = count_leads(counter=0)
    # так и не победил рекурсию, поэтому костыльный вывод с сохранением результата в новый класс
    l = Leads().leads
    # print(l[0])
    return l[0]
