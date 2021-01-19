from bs4 import BeautifulSoup
import requests

url="https://lifehacker.com/should-you-preorder-a-329-nvidia-geforce-rtx-3060-1846043773"
res=requests.get(url)
link=res.text
soup = BeautifulSoup(link, 'html5lib')

print(soup.get_text())
test = soup("script")
print(soup.get_text())