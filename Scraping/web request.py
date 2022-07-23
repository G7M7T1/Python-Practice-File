import requests

result = requests.get("https://example.com/")
print(result.url)
print(result.encoding)
print(result.cookies)
print(result.status_code)
print("--------Headers--------")
print(result.headers)
print("--------Headers--------")

print("--------Text--------")
print(result.text)
print("--------Text--------")