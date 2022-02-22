from datetime import datetime, timezone

import requests
from lxml import html

####################################################################
# API
####################################################################

def get_todays_horoscope(sunsign):
    url = "http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + sunsign
    response = requests.get(url)
    tree = html.fromstring(response.content)
    # date = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
    date = str(tree.xpath("//*[@id=\"main\"]/section/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/p/text()"))
    date = date.replace("']", "").replace("['", "")
    date_utc = datetime.now(timezone.utc)
    date_website = "-".join(date.split('-')[::-1])
    date_local = str(date_utc.astimezone()).split(' ')[0]

    if date_local < date_website:
        url = "https://www.ganeshaspeaks.com/horoscopes/yesterday-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        # horoscope = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = str(tree.xpath("//*[@id=\"horo_content\"]/text()"))
    elif date_local > date_website:
        url = "https://www.ganeshaspeaks.com/horoscopes/tomorrow-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        # horoscope = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = str(tree.xpath("//*[@id=\"horo_content\"]/text()"))
    else:
        # horoscope = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = str(tree.xpath("//*[@id=\"horo_content\"]/text()"))

    horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "").replace("[\'",
                                                                                                             "").replace(
        "\']", "")
    dict = {
        'date': date_local,
        'horoscope': horoscope,
        'sunsign': sunsign
    }

    return dict


def get_weekly_horoscope(sunsign):
    url = "http://www.ganeshaspeaks.com/horoscopes/weekly-horoscope/" + sunsign
    response = requests.get(url)
    tree = html.fromstring(response.content)
    # week = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
    week = str(tree.xpath("//*[@id=\"main\"]/section/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/p/text()"))
    week = week.replace("']", "").replace("['", "")
    # horoscope = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
    horoscope = str(tree.xpath("//*[@id=\"horo_content\"]/text()"))
    horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
    dict = {
        'week': week,
        'horoscope': horoscope,
        'sunsign': sunsign
    }

    return dict


def get_monthly_horoscope(sunsign):
    url = "http://www.ganeshaspeaks.com/horoscopes/monthly-horoscope/" + sunsign
    response = requests.get(url)
    tree = html.fromstring(response.content)
    # month = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
    month = str(tree.xpath("//*[@id=\"main\"]/section/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/p/text()"))
    month = month.replace("']", "").replace("['", "")
    # horoscope = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()[1]"))
    horoscope = str(tree.xpath("//*[@id=\"horo_content\"]/text()"))
    horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
    dict = {
        'month': month,
        'horoscope': horoscope,
        'sunsign': sunsign
    }

    return dict


def get_yearly_horoscope(sunsign):
    url = "http://www.ganeshaspeaks.com/horoscopes/yearly-horoscope/" + sunsign
    response = requests.get(url)
    tree = html.fromstring(response.content)
    # year = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
    year = str(tree.xpath("//*[@id=\"main\"]/section/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/p/text()"))
    year = year.replace("']", "").replace("['", "")
    # horoscope = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
    horoscope = str(tree.xpath("//*[@id=\"horo_content\"]/text()"))
    horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
    dict = {
        'year': year,
        'horoscope': horoscope,
        'sunsign': sunsign
    }

    return dict


if __name__ == '__main__':
    print(get_todays_horoscope("pisces"))
    print(get_weekly_horoscope("pisces"))
    print(get_monthly_horoscope("pisces"))
    print(get_yearly_horoscope("pisces"))
