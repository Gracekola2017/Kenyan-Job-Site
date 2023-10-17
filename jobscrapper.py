import requests
import re
from bs4 import BeautifulSoup
import csv

url = "https://www.corporatestaffing.co.ke/"
response = requests.get(url)
print(response)
