import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
import time
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
        'nid_inf': '-1269953935',
        'NID_AUT': 'Ln4gCD/r/3SWhqnjssZP71cxA/BWq9oIgHT+nSI8OLwl6Fr+wPuGuLD4qO44H2eA',
        'NID_JKL': 'akhPL5feM2YpXPBpBZH05FCvhPP3AcHDTv5AeR4zWBE=',
        'CBI_SES': 'x8YSZY6qMwQCYCXBEQApC9usDmXhg8ce5gtAy0S68TliHHUkJ6KKt3Srpk3IgIx6DRkgrj9VBrf3m/cJlZDv7ljOEYBBu7G3qNrHss01yZhH0BH4Fx3dp5GElOoKsGlU/dprTH0oN4fTp5x7vj5MsnheRxGja0kF+3+zTYAcRC4n+UjeDJ++qkYmx3YZwb/TkjZikWZ5ynZ2IH0ZW1gpteoZAzOqUdc8Tp3ykyLLXnVdrhp+WwboTOcQv0aWXZYFxWqDIuu9bZHUs2mUO/bpPOnwY/VLeHoz/43khN8QAQgpZiIASVKYhgXQpNsKW73gWNAjiSDfuBduqKim215UIETADdhIzyKxfZMMm8ZxHgjUVuHqr1tUXf5M87vAlargHhWX8e/dl5Jfymi8jJOipEUsYxZ+26wVdvVJdL9W5PDiIJLKXWmqCWP6vs2kiik2gE89IcJl5+SJxP2/TMnT3zJ0obDmLI8DtsZiyGIUX6M=',
        'CBI_CHK': '"r5V0mf9uRUZHZ/vmLGy3ez7f4/k4aqWXL5o03eN68foRF6vr8SfxFvlI+85vYVcKrwZpps2gKHNQX+ataQrIUGTL2zldbvohC/hpCypF3S0+KnoaTuvQS9tMcQY/s7igj4tNv6a7GzHGEqjC3qphuDx/RBsETZ6WNwnRABx9NH8="',
        'NID_SES': 'AAABnVoWbDgu/2mHepDXz7M+tSAn3eKEfFsprFU3p4GCeDeHayZvOB7gDjRVPbURwZ5yK85OYixEL1Nq81ZK2AwvyQ1c062XF5FkpX6iZaMI13tHwNwlOlwW1P6pninBNDTikNqGViDcbQ4AxHQAMzsTzIioxwyMTw6WkMIDI01Aqdryw0hEjVmeUKYtsTE/77UlhHK9FWXVNLEPXo9SYFL9q8KnVZszwJTkmEfqVFC/MkR0ipA9DZ+KHt++/cuslUAhd4HuJJzt+M86ZVEsXlMvhLr/EQuCEPSjnC665TbSbT8OOCVm1QoEPU1kp35Lu9ARlXU62/HawMcXnn8kIxjFegLjl+bFbrdYAustTS3e7qSWpoVy7qcEaRY/sQNRWm45lSv5Pi1V0plhaZLkUdQ9c2I7wbAdP2SAhv7OTyorkgTg6i/00WUytMiKcWDww4WZhRgiPQxD7WrjcA28eXY1NCj1WCmAZCh0UbJrAPelIYwi6DEjBks7DKBfB90iNQzRwNw399dbsI/cC5neInrU0Tw/p8p4MK2bf9IjaWdqybOs',
        '_naver_usersession_': 'umoLsMqdQBb74mVsB5gTwEk9',
        'page_uid': 'ivzxHsp0YiRssP7fiyCssssstrd-415951',
    }

    headers = {
        'authority': 'search.naver.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'NNB=IZBJERH4DQMGI; nx_ssl=2; ASID=798f73fa0000018710b1765100000069; nid_inf=-1269953935; NID_AUT=Ln4gCD/r/3SWhqnjssZP71cxA/BWq9oIgHT+nSI8OLwl6Fr+wPuGuLD4qO44H2eA; NID_JKL=akhPL5feM2YpXPBpBZH05FCvhPP3AcHDTv5AeR4zWBE=; CBI_SES=x8YSZY6qMwQCYCXBEQApC9usDmXhg8ce5gtAy0S68TliHHUkJ6KKt3Srpk3IgIx6DRkgrj9VBrf3m/cJlZDv7ljOEYBBu7G3qNrHss01yZhH0BH4Fx3dp5GElOoKsGlU/dprTH0oN4fTp5x7vj5MsnheRxGja0kF+3+zTYAcRC4n+UjeDJ++qkYmx3YZwb/TkjZikWZ5ynZ2IH0ZW1gpteoZAzOqUdc8Tp3ykyLLXnVdrhp+WwboTOcQv0aWXZYFxWqDIuu9bZHUs2mUO/bpPOnwY/VLeHoz/43khN8QAQgpZiIASVKYhgXQpNsKW73gWNAjiSDfuBduqKim215UIETADdhIzyKxfZMMm8ZxHgjUVuHqr1tUXf5M87vAlargHhWX8e/dl5Jfymi8jJOipEUsYxZ+26wVdvVJdL9W5PDiIJLKXWmqCWP6vs2kiik2gE89IcJl5+SJxP2/TMnT3zJ0obDmLI8DtsZiyGIUX6M=; CBI_CHK="r5V0mf9uRUZHZ/vmLGy3ez7f4/k4aqWXL5o03eN68foRF6vr8SfxFvlI+85vYVcKrwZpps2gKHNQX+ataQrIUGTL2zldbvohC/hpCypF3S0+KnoaTuvQS9tMcQY/s7igj4tNv6a7GzHGEqjC3qphuDx/RBsETZ6WNwnRABx9NH8="; NID_SES=AAABnVoWbDgu/2mHepDXz7M+tSAn3eKEfFsprFU3p4GCeDeHayZvOB7gDjRVPbURwZ5yK85OYixEL1Nq81ZK2AwvyQ1c062XF5FkpX6iZaMI13tHwNwlOlwW1P6pninBNDTikNqGViDcbQ4AxHQAMzsTzIioxwyMTw6WkMIDI01Aqdryw0hEjVmeUKYtsTE/77UlhHK9FWXVNLEPXo9SYFL9q8KnVZszwJTkmEfqVFC/MkR0ipA9DZ+KHt++/cuslUAhd4HuJJzt+M86ZVEsXlMvhLr/EQuCEPSjnC665TbSbT8OOCVm1QoEPU1kp35Lu9ARlXU62/HawMcXnn8kIxjFegLjl+bFbrdYAustTS3e7qSWpoVy7qcEaRY/sQNRWm45lSv5Pi1V0plhaZLkUdQ9c2I7wbAdP2SAhv7OTyorkgTg6i/00WUytMiKcWDww4WZhRgiPQxD7WrjcA28eXY1NCj1WCmAZCh0UbJrAPelIYwi6DEjBks7DKBfB90iNQzRwNw399dbsI/cC5neInrU0Tw/p8p4MK2bf9IjaWdqybOs; _naver_usersession_=umoLsMqdQBb74mVsB5gTwEk9; page_uid=ivzxHsp0YiRssP7fiyCssssstrd-415951',
        'referer': 'https://search.naver.com/search.naver?where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90%7CARM%7CTSMC&sm=tab_opt&sort=0&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0',
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

    params = {
        'where': 'news',
        'query': str(keyword),
        'sm': 'tab_opt',
        'sort': '1',
        'photo': '0',
        'field': '0',
        'pd': '0',
        'ds': '',
        'de': '',
        'docid': '',
        'related': '0',
        'mynews': '0',
        'office_type': '0',
        'office_section_code': '0',
        'news_office_checked': '',
        'nso': 'so:dd,p:all',
        'is_sug_officeid': '0',
    }

    response = requests.get('https://search.naver.com/search.naver', params=params, cookies=cookies, headers=headers)
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
        date=news_list_elem.find_all('span',attrs={'class':'info'})[-1].get_text()
        print('title:',title,'url:',url,'date:',date)
        data_list.append({'title':title,'url':url,'date':date})
    return data_list

class Thread(QThread):
    cnt = 0
    user_signal = pyqtSignal(str)  # 사용자 정의 시그널 2 생성

    def __init__(self, parent,time_period,time_cycle):  # parent는 WndowClass에서 전달하는 self이다.(WidnowClass의 인스턴스)
        super().__init__(parent)
        self.parent = parent  # self.parent를 사용하여 WindowClass 위젯을 제어할 수 있다.
        self.time_period=time_period
        self.time_cycle=time_cycle
    def run(self):
        cred = credentials.Certificate({
          "type": "service_account",
          "project_id": "recentnews-455d9",
          "private_key_id": "47c6f96e62f97e60c1486d9504ff37c436340e0d",
          "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDiefCWYoBPpUu6\nae0TPMibzpU0UCEpd1GodOU+GbUaNHrcvqeE89emEkDBh0ENw0v3P9Krhoy9rqPG\ncD7fIjg4wTzLUhV0G0bOo3Q83ieMocWI1GvZlUGFsT+IFLxIIux0/tiV20SIMJdd\nxIDNaxBiNdSyzOwTKuF4icJBgJodwTvWavv19zgPI0lLxLuU5aoxaYDd1ArZg6lk\ncFSCrsBVqWEv4ulnyM88SOHbidpKncLD8aZb/U3/ggFLEs9bz72QmntQC5nWImbE\nRdLe8+UAShYRUPbP8ls6KThffb+2Oloe6rJI9wBcBwWuHxv8qU7OBf5vZayqUZ9U\niJZA4DPrAgMBAAECggEABdxh/YJPD8CXVRuopvbLujx+X/wy33/W/SUJSbIgnaz+\nAPhuHWKyEfom8tstM836CUv9h7LTsZTzaA8/kUaxbcaSbDCTnY2XJ4HTYD/fhiQp\nmIDmyZqzN2J+4mam+Lbup5hwwnAKNfwL7sFHFAnRQrlh576l3VkevJ/UBx3s3xg0\nm7t/pFdIm2kr/MrIQpIxdiRE1DUEKoDsBgg2RT+TUKlqW2i3m5ZrLfI2JNxEXgpD\n+RF48AQFvoZEc9wXMDCcH9dunH4/rctBXq3rPYEWB49dZSuZMV5NkQsQ0RKGV0FV\n8A2tw+H4VdWuGqTglT1qZzmaPDpKtWF5PWf4XYXvAQKBgQD5nkKEBNSPhwPeJBXa\nZaOe5t8ec4rIPO2n1bk1jEHxzsSRLonapjlaS6IShbang+w1WjXdTdC8GyBJc9Ao\n+go/F5DRe1oPyQYZXcZaVuI0by3KbkQwbwWlaGGE7Vt7vvG5QJldpWs2hTBgkQiA\nEpF7DVgIEfsCxlOmvt5Dy/lM3wKBgQDoRDeoRJ5J77QJpqlJbuM/KkeFXLmBegGz\nOYw1FPBYJsiVUJT6yRqCxZLfLGeKlC7VXNYMdBEiadBc9CjU1ITXw15s3GmqC3XJ\nfFdU/vaXHF8rjl8inCup17jt/bR3ny58bq1u+B1D1LkRvnMaYyZfIK298A3X06mm\no/kmJ+AudQKBgBLebbTBELhQwnAWVjiOGlI2rYMFxOXiBSz8sOVlVs7KjH1VAUKv\n8gHrWbMAvI/pHv/hc9TovvCZNFWZFZEjZYbjZyUOp/4tefKM7iOCEdNY3CNDNpBa\ntBiOzWBY+ONfybHxOiakDHiwlLmX/QaBYNHmblMd2NWa3FPsday2TIANAoGAXFyM\nOWiX/VTJpjDVDrN+wGaCrGC0D+3BcVDIFW+vJ468osu5goSn+yqv/fk9b1j/yq6x\nG6CoE6Q6TEx3VDLyZI53JRj9F7aY7zd3zv/YdTy+B6cE49Fwd4imLFWABzWQmcC1\nTPRzRr73nTu7r9mPr7JiBK7KAnJT+0UnVWnz9uUCgYB98d1tMoiyRuxoxXYPJpYF\nC9OnMQe5kbw4+tQrICmM5jN5XtOvuXfl3qJSkqUFLgAd9JBnQ/bb3CQ2dZqDercZ\n5HplOEaWYVgVhnrVQRX818GP/5hky93lZTPI/N/g1Tj3bBBZPNzXnjDQi63RTxJD\nSxEc36tk3EdIM2s6qUAcdA==\n-----END PRIVATE KEY-----\n",
          "client_email": "firebase-adminsdk-qxtod@recentnews-455d9.iam.gserviceaccount.com",
          "client_id": "109289319377062275600",
          "auth_uri": "https://accounts.google.com/o/oauth2/auth",
          "token_uri": "https://oauth2.googleapis.com/token",
          "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
          "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-qxtod%40recentnews-455d9.iam.gserviceaccount.com"
        })
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://recentnews-455d9-default-rtdb.asia-southeast1.firebasedatabase.app/'
            # 'databaseURL' : '데이터 베이스 url'
        })
        time_start=0
        while True:

            time_now=datetime.datetime.now().timestamp()
            if time_now-time_start>=self.time_cycle:
                time_start = datetime.datetime.now().timestamp()
                db = firestore.client()
                doc_ref = db.collection('subjects').document('subjects')
                doc = doc_ref.get()
                if doc.exists:
                    keyword_info_list = doc.to_dict()['data']
                    print('keyword_list: {}'.format(keyword_info_list))
                else:
                    print(u'No such document!')

                time_now=datetime.datetime.now().strftime("%Y년%m월%d일 %H시%M분%S초")
                db = firebase_admin.db
                ref = db.reference()  # db 위치 지정, 기본 가장 상단을 가르킴
                ref.update({'timeNow':time_now})

                for index, keyword_info in enumerate(keyword_info_list):
                    group_name = keyword_info['group']
                    print('group_name:', group_name)
                    group_letter = ['A', 'B', 'C', 'D', 'E']
                    time_now = datetime.datetime.now().strftime("%Y년%m월%d일 %H시%M분%S초")
                    text = "{}그룹 크롤링중...현재시각:{}".format(group_letter[index], time_now)
                    self.user_signal.emit(text)
                    for keyword in keyword_info['name']:
                        if keyword.find("|")>=0:
                            print("앤드표시있음")
                            keyword=keyword
                        else:
                            print("앤드표시없음")
                            keyword = '"{}"'.format(keyword)

                        print('★★★keyword★★★★:', keyword)
                        soup = get_news(keyword)
                        data_list = get_article(soup)
                        print('data_list:', data_list)
                        keyword=keyword.replace('"','')
                        db = firebase_admin.db
                        ref = db.reference()  # db 위치 지정, 기본 가장 상단을 가르킴
                        ref.update({keyword: data_list})
                        # ref.update({'이름' : '김철수'}) #해당 변수가 없으면 생성한다.
                        # [출처] [Python] 파이썬 Firebase Realtime DB 생성, 값 저장, 조회|작성자 넬티아
                        print("====================================================")
                        time.sleep(self.time_period)


            else:
                text = "주기만큼 대기 중...{}초 지남".format(int(time_now-time_start))
                self.user_signal.emit(text)

            time.sleep(1)

    def stop(self):
        pass

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.path = "C:"
        self.index = None
        self.setupUi(self)
        self.setSlot()
        self.show()
        QApplication.processEvents()
        self.time_period=float(self.lineEdit.text())
        self.time_cycle=float(self.lineEdit_2.text())

    def start(self):
        print('11')
        self.x = Thread(self,self.time_period,self.time_cycle)
        self.x.user_signal.connect(self.slot1)  # 사용자 정의 시그널2 슬롯 Connect
        self.x.start()

    def slot1(self, data1):  # 사용자 정의 시그널1에 connect된 function
        self.textEdit.append(str(data1))

    def setSlot(self):
        pass

    def setIndex(self, index):
        pass

    def quit(self):
        QCoreApplication.instance().quit()


app = QApplication([])
ex = Example()
sys.exit(app.exec_())




