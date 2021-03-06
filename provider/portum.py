from datetime import datetime, timedelta
from provider.utils import get_filtered_fb_post


URL = "https://www.facebook.com/PortumCorvin/posts/"
FB_ID = "728866253985071"

def getMenu(today):
    menu = ''
    if today.weekday() < 5:
        is_this_week = lambda date: datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z').date() > today.date() - timedelta(days=7)
        menu_filter = lambda post: is_this_week(post['created_time']) and "főételek" in post['message'].lower()
        menu = get_filtered_fb_post(FB_ID, menu_filter)
        if "Előételek:" in menu:
            menu = menu.split("Előételek:")[1].strip()
        menu = '<br>'.join(i for i in menu.split('\n') if i)

    return {
        'name': 'Portum',
        'url': URL,
        'menu': menu
    }

if __name__ == "__main__":
    print(getMenu(datetime.today()))
