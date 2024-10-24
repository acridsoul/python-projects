import requests
import json
import sys
import colorama
from time import sleep

colorama.init()

def type(words: str):
    for char in words:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

url = r'https://www.virustotal.com/api/v3/files'

api = open('.env','r').read()

file_path = input(colorama.Fore.YELLOW + "Enter the path of the file >> ")
params = {'apikey': api}

file_to_upload = {'file': open(file_path,'rb')}

response = requests.post(url,files = file_to_upload, params=params)

if response.status_code == 200:
    sha1_hash = response.json()['sha1']
    file_url = f'https://www.virustotal.com/api/v3/files/{sha1_hash}'
    headers = {"accept": "application/json", "x-apikey": api}
    type(colorama.Fore.YELLOW + "Analysing....")

    response = requests.get(file_url,headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error fetching file analysis: {response.status_code} - {response.text}")
else:
    print(f"Error uploading file: {response.status_code} - {response.text}")


    




