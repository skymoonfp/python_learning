#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
按每月中固定某天定时执行
"""

import calendar
import datetime

import mytime


def day_in_month_range(shu_day: int, schedule_time: str, begin_date: str = "2000-01-01 00:00:00",
                       end_date: str = "2099-12-31 23:59:59"):
    """
    每月中的某天（给定日份超出当月天数时，按当月最后一天处理）
    :param begin_date: 执行开始时间；格式：yyyy-mm-dd hh:mm:ss
    :param end_date: 执行结束时间；格式：yyyy-mm-dd hh:mm:ss
    :param shu_day: 每月中的哪一天执行
    :param schedule_time: shu_day中的哪个时间执行；格式：hh:mm:ss
    :return: 所有要执行的时间（格式化时间）的list
    """
    dates = []  # 开始时间到结束时间之间的所有日子
    dt = datetime.datetime.strptime(begin_date, "%Y-%m-%d %H:%M:%S")
    date = begin_date[:]
    while date <= end_date:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d %H:%M:%S")
    da_month = []  # 取dates的yyyy-mm构成，不重复
    for i in dates:
        if i[:7] not in da_month:
            da_month.append(i[:7])

    new_months = []  # 开始时间到结束时间之间的所有要执行的时间
    first_month = int(begin_date[8:10])  # 开始时间的日份
    if first_month <= shu_day:  # 执行开始时间的月份中不包含shu_day日份时，从下个月的shu_day开始
        new_months.append(da_month[0] + "-" + str(shu_day) + " " + schedule_time)
    for i in da_month[1:]:
        days = calendar.monthrange(int(i[:4]), int(i[5:7]))[1]  # 给定年份月份中的日子数
        if shu_day < 29:
            new_months.append(i + "-" + str(shu_day).zfill(2) + " " + schedule_time)
        elif shu_day == 29:  # 每月中29日执行
            if days >= 29:
                new_months.append(i + "-" + "29" + " " + schedule_time)
            else:  # 该月中没有29日时
                new_months.append(i + "-" + "28" + " " + schedule_time)
        elif shu_day == 30:  # 每月中30日执行
            if days == 28:
                new_months.append(i + "-" + "28" + " " + schedule_time)
            elif days == 29:
                new_months.append(i + "-" + "29" + " " + schedule_time)
            elif days >= 30:
                new_months.append(i + "-" + "30" + " " + schedule_time)
        elif shu_day == 31:  # 每月中31日执行
            if days == 28:
                new_months.append(i + "-" + "28" + " " + schedule_time)
            elif days == 29:
                new_months.append(i + "-" + "29" + " " + schedule_time)
            elif days == 30:
                new_months.append(i + "-" + "30" + " " + schedule_time)
            elif days == 31:
                new_months.append(i + "-" + "31" + " " + schedule_time)
        else:
            pass
    last_time = datetime.datetime.strptime(new_months[-1], "%Y-%m-%d %H:%M:%S")
    end_date_time = datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    if last_time > end_date_time:  # new_months中最后一个要执行的时间超出给定执行结束时间时
        new_months = new_months[:-1]
    return new_months


def timing_monthly_run(day_in_months: list, function, *args):
    days = []  # 存放转换成时间戳的day_in_months
    datetime_run = 0  # 下一个要运行的时间
    for day_in_month in day_in_months:
        days.append(mytime.mktime(mytime.strptime(day_in_month, "%Y-%m-%d %H:%M:%S")))

    while True:
        current_time = mytime.time()
        for i in range(len(day_in_months)):
            if current_time == days[i]:
                datetime_run = current_time + 1  # 推迟1秒
            elif days[1] < current_time < days[i + 1]:
                datetime_run = days[i + 1] + 1  # 推迟1秒
            else:
                pass

        while mytime.time() < datetime_run:
            mytime.sleep(1)
        else:
            function(*args)


def test(a, b):
    print(a + b)


if __name__ == "__main__":
    while True:
        timing_monthly_run(day_in_month_range(10, "12:00:00", "2016-01-01", "2019-12-31"), test, 2, 3)
