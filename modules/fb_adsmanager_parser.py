from modules import config
from dotenv import load_dotenv
from time import sleep
load_dotenv()


def fb_authorization(fb_driver, login_facebook_bm, pass_facebook_bm):
    """authorization in facebook"""
    fb_driver.get("https://www.facebook.com/ads/manager/accounts/")
    login = fb_driver.find_element_by_id('email')
    login.send_keys(login_facebook_bm)
    password = fb_driver.find_element_by_id('pass')
    password.send_keys(pass_facebook_bm)
    login_button = fb_driver.find_element_by_id('loginbutton')
    login_button.click()
    return fb_driver


def get_info_fb(fb_driver, fb_url_first_part, fb_url_second_part, number_sum):
    """" get info about target ads cost"""
    sleep(3)
    url = config.Weekday().url_fb_ad(fb_url_first_part, fb_url_second_part)
    fb_driver.get(url)
    sleep(1)
    sum = fb_driver.find_elements_by_class_name('_1876')
    # print(sum[1].text)
    summa = sum[number_sum].text[0:-2]
    final_sum = summa.replace(' ', '')
    # print(final_sum)
    return final_sum


