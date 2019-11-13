from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://find-sec-bugs.github.io/bugs.htm')
bs = BeautifulSoup(html.read(),'html.parser')

bug_pattern_list=bs.find_all('h2',{'class':'page-header'})
for pattern in bug_pattern_list:
    print(pattern.get_text().strip())

