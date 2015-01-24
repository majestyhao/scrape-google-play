'''
Created on Jan 23, 2015
@author: Hao

for crawling
'''

import os

os.system("python3 getAppList.py")

categories = ['BOOKS_AND_REFERENCE', 'BUSINESS', 'COMICS', 'COMMUNICATION', 'EDUCATION', 'ENTERTAINMENT', 'FINANCE',
              'HEALTH_AND_FITNESS', 'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'APP_WALLPAPER', 'MEDIA_AND_VIDEO', 'MEDICAL',
              'MUSIC_AND_AUDIO', 'NEWS_AND_MAGAZINES', 'PERSONALIZATION', 'PHOTOGRAPHY', 'PRODUCTIVITY', 'SHOPPING',
              'SOCIAL', 'SPORTS', 'TOOLS', 'TRANSPORTATION', 'TRAVEL_AND_LOCAL', 'WEATHER', 'ARCADE', 'BRAIN', 'CARDS',
              'CASUAL', 'GAME_WALLPAPER', 'RACING', 'SPORTS_GAMES', 'GAME_WIDGETS', 'GAME']


for category in [x for x in categories]:
    print(" Cateory = ", category)
    os.system("mkdir " + category)
    os.system("mv googleplaycrawler-0.3.jar " + category)
    os.system("mv crawler.conf " + category)
    # os.system("cd " + category)
    applist = open(category + "_list.txt")
    while True:
        line = applist.readline()
        if len(line) == 0:
            break
        #os.system("java -jar " + category + "/googleplaycrawler-0.3.jar -f " + category + "/crawler.conf download " + line)
        os.system("cd " + category + "; java -jar googleplaycrawler-0.3.jar -f crawler.conf download " + line)
    applist.close
    os.system("mv " + category + "/googleplaycrawler-0.3.jar ./")
    os.system("mv " + category + "/crawler.conf ./")
