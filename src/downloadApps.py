'''
Created on Jan 23, 2015
@author: Hao

for crawling
'''

import os


categories = ['BOOKS_AND_REFERENCE', 'BUSINESS', 'COMICS', 'COMMUNICATION', 'EDUCATION', 'ENTERTAINMENT', 'FINANCE',
              'HEALTH_AND_FITNESS', 'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'APP_WALLPAPER', 'MEDIA_AND_VIDEO', 'MEDICAL',
              'MUSIC_AND_AUDIO', 'NEWS_AND_MAGAZINES', 'PERSONALIZATION', 'PHOTOGRAPHY', 'PRODUCTIVITY', 'SHOPPING',
              'SOCIAL', 'SPORTS', 'TOOLS', 'TRANSPORTATION', 'TRAVEL_AND_LOCAL', 'WEATHER', 'ARCADE', 'BRAIN', 'CARDS',
              'CASUAL', 'GAME_WALLPAPER', 'RACING', 'SPORTS_GAMES', 'GAME_WIDGETS', 'GAME']


for category in [x for x in categories]:
    print(" Cateory = ", category)
    applist = open(category + "_list.txt")
    while True:
        line = applist.readline()
        if len(line) == 0:
            break
        os.system("java -jar googleplaycrawler-0.3.jar -f crawler.conf download " + line)
    applist.close
