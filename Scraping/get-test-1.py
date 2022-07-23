import requests
from bs4 import BeautifulSoup

url_path = "https://code-gym.github.io/spider_demo/"
resp = requests.get(url_path)
soup = BeautifulSoup(resp.text, "html5lib")

print(soup.find("h1").text)

for h3 in soup.find_all("h3", "post-title"):
    print(h3.a.text)

print("\n")
print("Key Value--------------------------------------")
print("\n")

for kv in soup.find_all("a", {"class": "post-category", "class": "cat-1"}):
    print(kv.text)

print("\n")
print("stripped strings--------------------------------------")
print("\n")

for posts in soup.find_all("div", "post-body"):
    for post in posts.stripped_strings:
        print(post)