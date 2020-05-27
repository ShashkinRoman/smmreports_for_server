import os
from webdriver import webdriver_conf
from modules import fb_adsmanager_parser, moy_sklad_parser, instagram_direct_parser, config
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
load_dotenv()


def ceonnect_google_sheets():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv('json_keyfile'), scope)
    client = gspread.authorize(creds)
    sheet = client.open(os.getenv('name_sheet')).sheet1
    return sheet


def write_result(final_val, final_cost, final_doc, fb_result, final_leads):
    """write result in google_sheets for yesterday and print"""
    sheet = ceonnect_google_sheets()
    search = sheet.find(config.Weekday.yesterday_for_google_sheets())
    date = config.Weekday.yesterday_for_google_sheets()
    row_col1 = sheet.update_cell(int(search.row), int(search.col) + 1, str(final_val))
    row_col2 = sheet.update_cell(int(search.row), int(search.col) + 2, str(final_cost))
    row_col3 = sheet.update_cell(int(search.row), int(search.col) + 3, str(fb_result))
    row_col4 = sheet.update_cell(int(search.row), int(search.col) + 4, str(final_doc))
    row_col5 = sheet.update_cell(int(search.row), int(search.col) + 5, str(final_leads))
    print('\n--------------------------------------------------------------------------')
    print('Данные по BESUTYMARKET успешно записаны в таблицу. Дата: ', date)
    print('Выручка', str(final_val), '\nСебестоимость', str(final_cost),
          '\nЗатраты по рекламе', str(fb_result), '\nКоличество покупок', str(final_doc),
          '\nКоличество диалогов', str(final_leads))


def main():
    # all variables
    fb_url_first_part = os.getenv('url_first_part')
    fb_url_second_part = os.getenv('url_second_part')
    ms_url_first_part = os.getenv('msurl_yesterday_one_part')
    ms_url_second_part = os.getenv('msurl_yesterday_two_part')
    login_facebook_bm = os.getenv('log')
    pass_facebook_bm = os.getenv('pass')
    login_ms = os.getenv('mslog')
    pass_ms = os.getenv('mspass')
    direct_url = os.getenv('url_bm_messages')
    number_sum = 1
    driver = webdriver_conf.Webdriver.driver

    # take info from facebook and direct instagram web version
    fb_adsmanager_parser.fb_authorization(driver, login_facebook_bm, pass_facebook_bm)
    try:
        fb_sum = fb_adsmanager_parser.get_info_fb(driver, fb_url_first_part, fb_url_second_part, number_sum)
    except:
        fb_sum = "not found"
    try:
        chats_count = instagram_direct_parser.parse_chat(driver, direct_url)
    except:
        chats_count = "not count"
    # print('end insta parse')

    moy_sklad_parser.ms_authorization(driver, login_ms, pass_ms)
    try:
        val, cost, doc = moy_sklad_parser.get_info_ms(driver, ms_url_first_part, ms_url_second_part)
    except:
        val, cost, doc = "not count", "not count", "not count"
    # print(val, cost, doc)

    # write rezult and close driver
    write_result(val, cost, doc, fb_sum, chats_count)



if __name__ == '__main__':
    main()
