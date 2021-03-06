from datetime import datetime as dt
from multiprocessing import Pool

import config

from provider import pqs
from provider import kompot
from provider import bridges
from provider import tenminutes
from provider import opus
from provider import burgerking
from provider import subway
from provider import dezso
from provider import manga
from provider import intenzo
from provider import golvonal
from provider import gilice
from provider import veranda
from provider import otszaz
from provider import portum
from provider import muzikum
from provider import amici
from provider import foodie
from provider import weekend

FOODSOURCES = [
    weekend,
    bridges,
    pqs,
    kompot,
    gilice,
    tenminutes,
    dezso,
    amici,
    veranda,
    golvonal,
    portum,
    foodie,
    opus,
    manga,
    intenzo,
    muzikum,
    burgerking,
    subway
]

def menuLoader(getMenu):
    today = dt.today()
    if config.OFFSET:
        from datetime import timedelta
        today = today + timedelta(days=config.OFFSET)
    try:
        menu = getMenu(today)
        return menu
    except:
        print(f"Exception when downloading { getMenu.__module__ }")
        return None

def getDailyMenuParallel():
    with Pool(config.POOL_SIZE) as pool:
        all_menu = pool.map(menuLoader, [r.getMenu for r in FOODSOURCES])
    return [i for i in all_menu if i]

if __name__ == "__main__":
    print(getDailyMenuParallel())
