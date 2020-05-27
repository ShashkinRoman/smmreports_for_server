import os
from webdriver import webdriver_conf
from modules import fb_adsmanager_parser, instagram_direct_parser, config
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
load_dotenv()


def ceonnect_google_sheets():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv('json_keyfile'), scope)
    client = gspread.authorize(creds)
    sheet = client.open(os.getenv('name_sheet_kans')).sheet1
    return sheet


def write_result(fb_result, final_leads):
    """write result in google_sheets for yesterday and print"""
    sheet = ceonnect_google_sheets()
    search = sheet.find(config.Weekday.yesterday_for_google_sheets())
    date = config.Weekday.yesterday_for_google_sheets()
    sheet.update_cell(int(search.row), int(search.col) + 2, str(fb_result))
    sheet.update_cell(int(search.row), int(search.col) + 4, str(final_leads))
    row_col1 = sheet.cell(int(search.row), int(search.col) + 6).value
    row_col2 = sheet.cell(int(search.row), int(search.col) + 5).value
    row_col3 = sheet.cell(int(search.row), int(search.col) + 1).value
    print('\n--------------------------------------------------------------------------')
    print('Данные по KANS успешно записаны в таблицу. Дата: ', date)
    print('Выручка', str(row_col1), '\nСтоимость заказа', str(row_col2),
          '\nЗатраты по рекламе', str(fb_result), '\nКоличество покупок', str(row_col3),
          '\nКоличество диалогов', str(final_leads))


def main():
    # all variables
    fb_url_first_part = os.getenv('url_first_part_kans')
    fb_url_second_part = os.getenv('url_second_part_kans')
    login_facebook_bm = os.getenv('log')
    pass_facebook_bm = os.getenv('pass')
    direct_url = os.getenv('url_kans_messenger')
    driver = webdriver_conf.Webdriver.driver
    number_sum = 2
    # take info from facebook and direct instagram web version
    try:
        fb_adsmanager_parser.fb_authorization(driver, login_facebook_bm, pass_facebook_bm)
    except:
        pass
    try:
        fb_sum = fb_adsmanager_parser.get_info_fb(driver, fb_url_first_part, fb_url_second_part, number_sum)
    except:
        fb_sum = "not found"
    try:
        chats = instagram_direct_parser.parse_chat(driver, direct_url)
    except:
        chats = "not count"
    # write result and close driver
    write_result(fb_sum, chats)


if __name__ == '__main__':
    main()
