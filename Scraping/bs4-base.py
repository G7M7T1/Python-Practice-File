from bs4 import BeautifulSoup

text = """
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <h1 class="title-main">Title Main</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
"""

soup = BeautifulSoup(text, "lxml")

print("\n")

print("---------find first p -----------------")
print(soup.find("p"))
print("---------find first p -----------------")

print("\n")

print("---------find all p -----------------")
print(soup.find_all("p"))
print("---------find all p -----------------")

print("\n")

print("---------find class_ -----------------")
print(soup.find(class_="title-main").text)
print("---------find class_ -----------------")

print("\n")

print("---------get text -----------------")
first_p_tag = soup.find("h1")
print(first_p_tag.getText())
print("---------get text -----------------")

print("\n")

print("---------CSS Selector -----------------")
text_result = soup.select(".title-main")
print(text_result[0].getText())
print("---------CSS Selector -----------------")