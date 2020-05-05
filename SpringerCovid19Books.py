#%%
import os
from random import randint
from time import sleep

import requests
import wget 
import pandas as pd

from tqdm import tqdm 
tqdm.pandas()

#%%
cwd = os.getcwd()                                                   # set current working directory 
booklist = pd.read_excel('Free+English+textbooks.xlsx')             # read in the booklist

manualdownload = pd.DataFrame(columns=['OpenURL', 'Book Title', 'Edition', 'Electronic ISBN', 'English Package Name'])
print("\nBooklist extraction starting ...")
for url, title, edition, isbn, pk_name in tqdm(booklist[['OpenURL', 'Book Title', 'Edition', 'Electronic ISBN', 'English Package Name']].values):
    ### initiating the download
    file_name = f"{title.replace(':', '')}, {edition} - ISBN {isbn}.pdf"
    print(f"\ndownloading {file_name} ...")

    ### create category folder
    dir = os.path.join(cwd, pk_name)
    if not os.path.exists(dir):
        os.mkdir(dir)

    ### download and saving the file
    r = requests.get(url)
    new_url = r.url                                                 # get the actual URL of the ebook page
    download_url = new_url.replace('/book/', '/content/pdf/')   
    download_url = f"{download_url}.pdf"                            # set up the download url
    try:                                                            # downloading
        wget.download(download_url, f"{os.path.join(dir,file_name)}")
        print(f"downloading {file_name} COMPLETED ...\n")
        sleep(randint(1,5))                                         # random sleep time between 1-5s
    except:                                                         # when download fails
        manualdownload.loc[len(manualdownload)] = ([url, title, edition, isbn, pk_name])
        print(f"downloading {file_name} FAILED ...\n")

print("\n\nBooklist extraction completed")



# %%
