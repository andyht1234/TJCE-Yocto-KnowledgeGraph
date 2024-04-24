import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random

url = 'https://lore.kernel.org/yocto-toaster/'
url_content = ''
previous_title = ''
num = 0
folder_path = ''

num1 = input("txt输入0，json输入1：")
while num1 not in ['0', '1']:
    print("输入无效，请输入0或1。")
    num1 = input("txt输入0，json输入1：")

if(num1 == '0'):
    folder_path = 'toaster_TXT'
else:
    folder_path = 'toaster_JSON'

while url:
    response = requests.get(url, verify=False)
    #休眠时间（防攻击机制）
    sleep_time = random.randint(0, 2) + random.random()
    time.sleep(sleep_time)
    soup = BeautifulSoup(response.text, 'html.parser')

    pre_tags = [pre for pre in soup.find_all('pre') if not pre.find_parent('form')]
    if pre_tags:
        for link in pre_tags[0].find_all('a'):
            href = link.get('href')
            if '#nav' not in href:
                url_content = 'https://lore.kernel.org/yocto-toaster/' + href
                response_content = requests.get(url_content, verify=False)
                soup_content = BeautifulSoup(response_content.text, 'html.parser')
                title = soup_content.title.string
                if title != previous_title:
                    previous_title = title
                    num = num + 1
                    pre_tags_content = [pre for pre in soup_content.find_all('pre') if not pre.find_parent('form')]
                    if pre_tags_content:
                        if num1 == '0':
                            file_path = os.path.join(folder_path, f'output_{num}.txt')
                            if not os.path.exists(file_path):
                                with open(file_path, 'a', encoding='utf-8') as f:
                                    for pre in pre_tags_content[:-1]:
                                        f.write(pre.text + '\n')
                        else:
                            file_path = os.path.join(folder_path, f'output_{num}.json')
                            if not os.path.exists(file_path):
                                data_content = [pre.text for pre in pre_tags_content[:-1]]
                                with open(file_path, 'a', encoding='utf-8') as f:
                                    json.dump(data_content, f, ensure_ascii=False, indent=4)

        if len(pre_tags) > 1:
            next_link = pre_tags[1].find('a', rel='next')
            if next_link:
                url = "https://lore.kernel.org/yocto-toaster/" + next_link.get('href')
            else:
                url = None
        else:
            url = None