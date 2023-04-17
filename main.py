import openpyxl
import pandas as pd
from pyautogui import size
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import time
import datetime
import pyautogui
import pyperclip
import csv
import sys
import os
import math
import requests
import re
import random
import chromedriver_autoinstaller
from PyQt5.QtWidgets import QWidget, QApplication, QTreeView, QFileSystemModel, QVBoxLayout, QPushButton, QInputDialog, \
    QLineEdit, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QCoreApplication
from selenium.webdriver import ActionChains
from datetime import datetime, date, timedelta
import numpy
import datetime
from window import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



def get_news(keyword):
    cookies = {
        'NNB': 'IZBJERH4DQMGI',
        'nx_ssl': '2',
        'ASID': '798f73fa0000018710b1765100000069',
        'CBI_SES': 'z/bB+dJz1Jkkcex3afxFCTWZmycH17VF26Hk8p3dZrxmLnIQlvB3kiZVhZtC4AQhePFU8xycJv+n2FHLfETNvFakwg0OzMWQdVSaewz4dU8+8qginjzS8gsFSwMJsgemdFb/rmbk7wODZJt14M3ArmmCyRb0iF+DcYO9eHZsaVKMOHpQIq3xiy/FXGH4cVqQpHQByNMZKNNKO6REpss8Alhda9LL47c3xtY4GwJo4UYy/9orLCajwLU/ZNsTIv2RrFVqyzU6B4DzYnmdyt/cZzXd53soc/wrDKMPrkV8M1+UiPZy3nE8LJ1kaLvUaOzpru8JTNzirIn6feKP1zNlcPtFTS38K8UVfKQB/qaa/NOFV2ysWke7RkSgPJNE/vW+C2CMub/675nSCqoGb7QrhTttA3dcMT5MAnv90Y+oY3keEVYjtqlZLCDSXcameHlvtZ9BhZjN73uaGO1zv/+24B2regAH8amL06gL7y3tYjY=',
        '_naver_usersession_': '2QacchkbUgAKJCnqgnpsKfli',
        'nid_inf': '-1301193424',
        'NID_AUT': 'gcMRtUGaqkIrIA3N4IZVXgmQEpFaa+vBBt5JprursD/XiZFZRy2HsTY3RDlloFgj',
        'NID_JKL': '0mfi8F6SaYqMxcjF5XTtKxVb1QHBb4gW3twm3gFiIMM=',
        'NID_SES': 'AAABrDYXXZwrcnEl6mBAscxFhq5o64FeKBc547rx4Z2WJP3AHxGLgL02YRYMpZD143M4HUKqHscqe+qdhqUGDT4T2ys3bVGQi3HF7ZwhvN6GAS0MkOMBh2nLJ/lvIzzdJ9dZ1rXEMKs6leL9LqvJeOrXSy/GWTrPIQDWk3mwhvuoS26ZrQAMYM41FHsdhN4HXkVDvGn3vC6dqzLea9Pm+4W5pS4Jpb/YyeZuqp3obBtOI/Ox4kfMemMr6EJoknCy9U9H0lPS2M8a+pkPObmPVp9Ea4yOhNWGCjLxxq9Q1PgI8smIAMngD2a4RU8bWtX7f4f9925R/NqlwPUkDMHSgMjJcxr2qBXmsh2Pbc5FXOiAULVX84Mf+95SSJSMSv+578X00UntHudSytDNe7oWVWBvOM2fPnp4IrzH48/0mRfdJyhmmZI5n22Yp/atuAhWebqgFeaVXsUEvCFlVA8OeBOZLjkDNmqvI7xw0losQmkkI43OUDV1IMGGGyNUjFzdDhaWHVGg3ci+pYqadFnqvXyk5ll7JuUw3drJsJjeS61WFm3ewhQ23OZP1TPZHEgOL6OSZw==',
        'CBI_CHK': '"r5V0mf9uRUZHZ/vmLGy3ez7f4/k4aqWXL5o03eN68foRF6vr8SfxFvlI+85vYVcKrwZpps2gKHNQX+ataQrIUGTL2zldbvohC/hpCypF3S0+KnoaTuvQS9tMcQY/s7igjoe5JIlmoOaQfGuDGze5zvH4UPUIsbXUOCqUFvjHzG0="',
        'page_uid': 'ivAUCwp0Jy0ssBCpPUosssssto0-231984',
    }

    headers = {
        'authority': 'search.naver.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'NNB=IZBJERH4DQMGI; nx_ssl=2; ASID=798f73fa0000018710b1765100000069; CBI_SES=z/bB+dJz1Jkkcex3afxFCTWZmycH17VF26Hk8p3dZrxmLnIQlvB3kiZVhZtC4AQhePFU8xycJv+n2FHLfETNvFakwg0OzMWQdVSaewz4dU8+8qginjzS8gsFSwMJsgemdFb/rmbk7wODZJt14M3ArmmCyRb0iF+DcYO9eHZsaVKMOHpQIq3xiy/FXGH4cVqQpHQByNMZKNNKO6REpss8Alhda9LL47c3xtY4GwJo4UYy/9orLCajwLU/ZNsTIv2RrFVqyzU6B4DzYnmdyt/cZzXd53soc/wrDKMPrkV8M1+UiPZy3nE8LJ1kaLvUaOzpru8JTNzirIn6feKP1zNlcPtFTS38K8UVfKQB/qaa/NOFV2ysWke7RkSgPJNE/vW+C2CMub/675nSCqoGb7QrhTttA3dcMT5MAnv90Y+oY3keEVYjtqlZLCDSXcameHlvtZ9BhZjN73uaGO1zv/+24B2regAH8amL06gL7y3tYjY=; _naver_usersession_=2QacchkbUgAKJCnqgnpsKfli; nid_inf=-1301193424; NID_AUT=gcMRtUGaqkIrIA3N4IZVXgmQEpFaa+vBBt5JprursD/XiZFZRy2HsTY3RDlloFgj; NID_JKL=0mfi8F6SaYqMxcjF5XTtKxVb1QHBb4gW3twm3gFiIMM=; NID_SES=AAABrDYXXZwrcnEl6mBAscxFhq5o64FeKBc547rx4Z2WJP3AHxGLgL02YRYMpZD143M4HUKqHscqe+qdhqUGDT4T2ys3bVGQi3HF7ZwhvN6GAS0MkOMBh2nLJ/lvIzzdJ9dZ1rXEMKs6leL9LqvJeOrXSy/GWTrPIQDWk3mwhvuoS26ZrQAMYM41FHsdhN4HXkVDvGn3vC6dqzLea9Pm+4W5pS4Jpb/YyeZuqp3obBtOI/Ox4kfMemMr6EJoknCy9U9H0lPS2M8a+pkPObmPVp9Ea4yOhNWGCjLxxq9Q1PgI8smIAMngD2a4RU8bWtX7f4f9925R/NqlwPUkDMHSgMjJcxr2qBXmsh2Pbc5FXOiAULVX84Mf+95SSJSMSv+578X00UntHudSytDNe7oWVWBvOM2fPnp4IrzH48/0mRfdJyhmmZI5n22Yp/atuAhWebqgFeaVXsUEvCFlVA8OeBOZLjkDNmqvI7xw0losQmkkI43OUDV1IMGGGyNUjFzdDhaWHVGg3ci+pYqadFnqvXyk5ll7JuUw3drJsJjeS61WFm3ewhQ23OZP1TPZHEgOL6OSZw==; CBI_CHK="r5V0mf9uRUZHZ/vmLGy3ez7f4/k4aqWXL5o03eN68foRF6vr8SfxFvlI+85vYVcKrwZpps2gKHNQX+ataQrIUGTL2zldbvohC/hpCypF3S0+KnoaTuvQS9tMcQY/s7igjoe5JIlmoOaQfGuDGze5zvH4UPUIsbXUOCqUFvjHzG0="; page_uid=ivAUCwp0Jy0ssBCpPUosssssto0-231984',
        'referer': 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%22%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90%22&sort=0&photo=0&field=0&pd=4&ds=2023.04.13.09.00&de=2023.04.14.09.00&cluster_rank=22&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:1d,a:all&start=11',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="111.0.5563.149", "Not(A:Brand";v="8.0.0.0", "Chromium";v="111.0.5563.149"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={}&sort=0&photo=0&field=0&pd=4&ds=2023.04.13.09.00&de=2023.04.14.09.00&cluster_rank=35&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:1d,a:all&start=1'.format(keyword),
        cookies=cookies,
        headers=headers,
    )
    soup=BeautifulSoup(response.text,'lxml')
    return soup

def get_article(soup):
    news_list_ul=soup.find('ul',attrs={'class':'list_news'})
    news_list=news_list_ul.find_all('li',attrs={'class':'bx'})
    print("뉴스갯수:",len(news_list))
    data_list=[]
    for news_list_elem in news_list:
        title=news_list_elem.find('a',attrs={'class':'news_tit'}).get_text()
        url=news_list_elem.find('a',attrs={'class':'news_tit'})['href']
        print('title:',title,'url:',url)
        data_list.append({'title':title,'url':url})
    return data_list


cred = credentials.Certificate("mykey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://recentnews-455d9-default-rtdb.asia-southeast1.firebasedatabase.app/'
    #'databaseURL' : '데이터 베이스 url'
})

db=firestore.client()
doc_ref = db.collection('subjects').document('subjects')
doc = doc_ref.get()
if doc.exists:
    keyword_info_list=doc.to_dict()['data']
    print('keyword_list: {}'.format(keyword_info_list))
else:
    print(u'No such document!')



for keyword_info in keyword_info_list:
    group_name=keyword_info['group']
    print('group_name:',group_name)
    for keyword in keyword_info['name']:
        keyword='"{}"'.format(keyword)
        print('★★★keyword★★★★:',keyword)
        soup=get_news(keyword)
        data_list=get_article(soup)
        print('data_list:',data_list)

        db=firebase_admin.db
        ref = db.reference()#db 위치 지정, 기본 가장 상단을 가르킴
        ref.update({keyword:data_list})
        # ref.update({'이름' : '김철수'}) #해당 변수가 없으면 생성한다.
        # [출처] [Python] 파이썬 Firebase Realtime DB 생성, 값 저장, 조회|작성자 넬티아
        print("====================================================")
        time.sleep(0.5)
