import os
from os import getenv
from random import randint
from time import sleep
from tqdm import tqdm
from flask import Flask, request
from flask_cors import cross_origin
from pathlib import Path
from sys import platform
import json
import requests
import wget
import pandas as pd


app = Flask(__name__)


@app.route('/', methods=['POST'])
@cross_origin(['http://localhost:8080/'])
def download():

    params = request.json

    downloadlist = pd.DataFrame.from_dict(params, orient='index')

    for url, label in tqdm(downloadlist[['downloadUrl', 'label']].values):

        # initiating the download
        path_to_download_folder = get_download_path()
        file_name = label + '.pdf'
        path = os.path.join(path_to_download_folder,
                            file_name)                                  # file path

        print(f"\ndownloading {file_name} ...")

        try:                                                            # downloading
            wget.download(url, f"{path}")
            print(f"downloading {file_name} COMPLETED ...\n")
            # random sleep time between 1-5s
            sleep(randint(1, 5))
        except:                                                         # when download fails
            print(f"downloading {file_name} FAILED ...\n")

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/')
def index():
    return ''


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if platform == 'darwin':
        return str(os.path.join(Path.home(), "Downloads"))
    elif os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')
