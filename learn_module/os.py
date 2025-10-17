import urllib.request

import os

os.makedirs('download1', exist_ok=True)

myurl = 'https://gist.githubusercontent.com/kiranzaman/79bac8e2ca947c7db5f25598ce85fc9d/raw/bf7c14aeaa68d644fda770896928bfa9b9b159e9/myfamily.csv'

urllib.request.urlretrieve(myurl, 'download1/myfamily.csv')

print("Download Completed")