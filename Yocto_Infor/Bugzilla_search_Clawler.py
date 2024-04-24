import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random

url = 'https://bugzilla.yoctoproject.org/buglist.cgi?bug_status=__all__&limit=0&no_redirect=1&order=priority%2Cbug_severity&query_format=specific'
url_content = ''
folder_path = ''

num1 = input("txt输入0，json输入1：")
while num1 not in ['0', '1']:
    print("输入无效，请输入0或1。")
    num1 = input("txt输入0，json输入1：")

if(num1 == '0'):
    folder_path = 'bugzilla_search_TXT'
else:
    folder_path = 'bugzilla_search_JSON'
os.makedirs(folder_path, exist_ok=True)

response = requests.get(url, verify=False)

#sleep_time = random.randint(0, 2) + random.random()
#time.sleep(sleep_time)

soup = BeautifulSoup(response.text, 'html.parser')

bugzilla_body = soup.find('div', id='bugzilla-body')
buglist_menu = bugzilla_body.find('div', class_='buglist_menu')
bz_query_links = buglist_menu.find('div', class_='bz_query_links')
bz_query_links = bz_query_links.find('a')['href']
download_url = 'https://bugzilla.yoctoproject.org/' + bz_query_links

save_folder = 'bugzilla_search'
os.makedirs(save_folder, exist_ok=True)
file_name = os.path.join(save_folder, 'bugzilla_search.csv')

response = requests.get(download_url, stream=True)
with open(file_name, 'wb') as file:
    for chunk in response.iter_content(chunk_size=128):
        file.write(chunk)
print(f'File downloaded and saved to: {file_name}')