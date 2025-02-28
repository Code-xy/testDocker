import os
import sys
import time
import requests
import json

resp = requests.get("https://www.baidu.com")
print(resp.text)

resp = requests.get("https://www.google.com")
print(resp.text)
