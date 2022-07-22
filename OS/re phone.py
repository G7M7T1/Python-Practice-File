import re

text = "my phone number is 808-744-0010, and 64-514-5821"

result = re.findall(r"\d{2,3}-\d{3}-\d{4}", text)
print(result)
