import requests
from bs4 import BeautifulSoup

url_path = "https://code-gym.github.io/spider_demo/"
resp = requests.get(url_path)
soup = BeautifulSoup(resp.text, "html5lib")

# Get Nav
nav = soup.find(id="nav")
# Get Nav's Parent (Header)
header = nav.parent

javascript = soup.find("li", "cat-2")
# cat-2
print(javascript)
# cat-1 GO Previous
print(javascript.previous_sibling)
# cat-3 Go Next
print(javascript.next_sibling)


# ---------------------------
print("children---------------------")

ul = soup.find("ul")
for li in ul.children:
    print(li.find("a").text)