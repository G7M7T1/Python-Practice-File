import bs4
import requests

web_result = requests.get("https://en.wikipedia.org/wiki/Iceland")
soup = bs4.BeautifulSoup(web_result.text, "lxml")

image = soup.select("img.thumbimage")

for i in range(len(image)):
    img_path = "https:" + image[i]["src"]
    img_get = requests.get(img_path)
    with open(f"output/wiki_{i}.jpg", "wb") as f:
        f.write(img_get.content)
