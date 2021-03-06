from datetime import timedelta, datetime
from provider.utils import get_dom


URL = "http://bridges.hu/#heti-menu"

def getMenu(today):
    day = today.weekday() + 1
    menu = ''
    try:
        dom = get_dom(URL)
        weekly_menu = dom.xpath('//section[@id="heti-menu"]//p')
        date = weekly_menu[0].text_content().strip()[0:10]
        this_week = lambda date: datetime.strptime(date, '%Y.%m.%d').date() > today.date() - timedelta(days=6)
        if this_week(date)  and today.weekday() < 5:
            menu = weekly_menu[day].text_content()
            menu = menu.replace('1.', '<br>1.')
            menu = menu.replace('2.', '<br>2.')
            menu = menu + '<br>' + weekly_menu[6].text_content()
    except:
        pass

    return {
        'name': 'Bridges',
        'url':URL,
        'menu': menu
    }

if __name__ == "__main__":
    print(getMenu(datetime.today()))
