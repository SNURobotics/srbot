import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict

def parse_snu_menu():
    # 마지막 문자열은 식당 종류와 표시할 순서
    # 참고: http://mini.snu.kr/cafe/pick/
    # url = 'http://mini.snu.kr/cafe/today/kvdj'
    url = 'http://mini.snu.kr/cafe/today/'
    r = requests.get(url)
    r.encoding = 'utf-8'

    d_menu = {}
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.body.table.find_all('tr')
        for l in rows:
            if l.text in {'아침', '점심', '저녁'}:
                meal = l.text
                d_menu[meal] = OrderedDict()
                continue

            cafeteria, items = l.find_all('td')
            # 가격은 다 날리자
            items = [item.strip() for item in items.contents if not str(item).startswith('<')]
            d_menu[meal][cafeteria.text] = items
    else:
        print('error')
    return d_menu


def snu_menu(meal='all'):
    """parse SNU daily menu"""
    cafeterias = {'302동', '기숙사(901동)', '기숙사(919동)', '301동(교수)'}

    if meal in {'점심', '저녁'}:
        l_keys = [meal]
    else:
        l_keys = ['점심', '저녁']

    d_menu = parse_snu_menu()
    msg = ''
    for meal in l_keys:
        dd_menu = d_menu[meal]
        msg += f'*[{meal}]* http://mini.snu.ac.kr \n'
        for cafe, dish in dd_menu.items():
            if cafe in cafeterias:
                s_dish = '/'.join(dish)
                msg += f'*{cafe}* : {s_dish}\n'
    return msg


if __name__ == '__main__':
    print(snu_menu())

