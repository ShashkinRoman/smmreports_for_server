import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()


class Weekday():
    """ all actions with week day"""
    def __init__(self):
        self.today_datetime = datetime.now()
        self.yesterday_datetime = self.today_datetime + timedelta(days=-1)
        self.day_before_yesterday_datetime = self.yesterday_datetime + timedelta(days=-1)

    @staticmethod
    def text_day(datetime_day):
        """"convert week day in number"""
        number_day = datetime_day.isoweekday()
        week_days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда',
                     4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}
        text_day = week_days[number_day]
        return text_day

    @staticmethod
    def convert_dates_for_urls():
        """add 0 for day,mont. need for text urls"""
        today = datetime.now()
        yesterday = today + timedelta(days=-1)
        if yesterday.day < 10:
            yest_day = '0' + str(yesterday.day)
        else:
            yest_day = str(yesterday.day)
        if yesterday.month < 10:
            yest_month = '0' + str(yesterday.month)
        else:
            yest_month = str(yesterday.month)
        if yesterday.day < 10:
            day_now = '0' + str(today.day)
        else:
            day_now = str(today.day)
        if yesterday.month < 10:
            month_now = '0' + str(today.month)
        else:
            month_now = str(today.month)
        return today, yesterday, yest_day, yest_month, day_now, month_now

    @staticmethod
    def url_fb_ad(fb_url_first_part, fb_url_second_part):
        today, yesterday, yest_day, yest_month, day_now, month_now = Weekday().convert_dates_for_urls()
        yesterday_for_url = yest_day + '-' + yest_month + '-' + str(yesterday.year) + '_' + day_now + '-' + month_now + '-' + str(today.year)
        # print('yesterday_for_url', yesterday_for_url)
        url = fb_url_first_part + yesterday_for_url + fb_url_second_part
        return url

    @staticmethod
    def url_ms(ms_url_first_part, ms_url_second_part):
        today, yesterday, yest_day, yest_month, day_now, month_now = Weekday().convert_dates_for_urls()
        yesterday_for_url_ms = yest_day + '.' + yest_month + '.' + str(
            yesterday.year) + '%2000:00:00,' + yest_day + '.' + month_now + '.' + str(today.year) + '%2023:59:59'
        url_ms = ms_url_first_part + str(yesterday_for_url_ms) + ms_url_second_part
        return url_ms

    @staticmethod
    def yesterday_for_google_sheets():
        yesterday = datetime.now() + timedelta(days=-1)
        _, _, day, month, _, _ = Weekday.convert_dates_for_urls()
        yesterday_correct = day + '.' + month + '.' + str(yesterday.year)
        return yesterday_correct