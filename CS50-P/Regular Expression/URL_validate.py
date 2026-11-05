import re

url = input("What's your URL? ").strip()

if re.fullmatch(
    r"(https://)?[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+(\/[^.][^\s]*)?",
    url
):
    print("Valid!")
else:
    print("Invalid!")