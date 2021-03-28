from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def get_domain(url):
    return urlparse(url).netloc


# intro
print(color.PURPLE + "\n============= GoSearch =============\n" + color.END)
# to search
query = input(color.BLUE + "search query: " + color.END)
print("\n")

results = []

for link in search(query, tld="co.in", num=4, stop=4, pause=2):
    reqs = requests.get(link)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    title = get_domain(link) + " link:"
    for title in soup.find_all('title'):
        title = title.get_text()
    results.append((title, link))


for result in results:
    title, link = result

    print(color.BOLD + color.PURPLE + title + color.END)
    print(color.BLUE + link + color.END)

print("\n")
