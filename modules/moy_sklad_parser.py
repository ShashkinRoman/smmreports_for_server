from time import sleep
from modules import config


def ms_authorization(driver, login_ms, pass_ms):
    driver.get("https://www.moysklad.ru/login/")
    login = driver.find_element_by_xpath('/html/body/div[3]/main/div[1]/div/div[2]/div[1]/form/fieldset[1]/input')
    # login.click()
    login.send_keys(login_ms)
    # search and input pass
    password = driver.find_element_by_xpath(
        '/html/body/div[3]/main/div[1]/div/div[2]/div[1]/form/fieldset[2]/input')
    password.send_keys(pass_ms)
    # search and click button login
    login_button = driver.find_element_by_xpath(
        '/html/body/div[3]/main/div[1]/div/div[2]/div[1]/form/fieldset[3]/button')
    login_button.click()


def get_info_ms(ms_driver, ms_url_first_part, ms_url_second_part):
    sleep(2)
    url = config.Weekday().url_ms( ms_url_first_part, ms_url_second_part)
    ms_driver.get(url)
    sleep(3)
    try:
        button_panel = ms_driver.find_element_by_xpath(
        '//*[@id="site"]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td/div/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/div')
        button_buyer = button_panel.find_element_by_class_name('last').click()
    except:
        print(__file__, 'func get_info_ms, variable button_buyer not found')
    sleep(3)
    ms_driver.execute_script("window.scrollBy(0,3000)")
    try:
        val = ms_driver.find_element_by_xpath('//*[@id="DocumentTablePnl"]/tfoot/tr[2]/th[4]')
        final_val = str(val.text).replace(' ', '')
    except:
        print(__file__, 'func get_info_ms, variable val not found')
    try:
        cost = ms_driver.find_element_by_xpath(
            '//*[@id="DocumentTablePnl"]/tfoot/tr[2]/th[6]')
        final_cost = str(cost.text).replace(' ', '')
    except:
        print(__file__, 'func get_info_ms, variable cost not found')
    try:
        documents = ms_driver.find_element_by_class_name('pages')
        final_doc = str(documents.text).split()[-1]
    except:
        print(__file__, 'func get_info_ms, variable documents not found')
    return final_val, final_cost, final_doc
