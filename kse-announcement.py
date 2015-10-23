import urllib2
from bs4 import BeautifulSoup
import datetime

def getHTML(ticker):
    response = urllib2 \
        .urlopen('http://dps.kse.com.pk/includes/SL_main_announce_inc.php?r=REG&pageid=ann&symbolCode=' + ticker)
    html = response.read()
    return html

def getVal(dom):
    if (len(dom.contents) == 0):
        return ""
    val = dom.contents[0]
    val = val.replace(",", "")
    if val == None:
        return ""
    return val.strip()


html = getHTML('DGKC')
soup = BeautifulSoup(html, "html.parser")
rows = soup.find_all('tr')

for row in rows:
    tds = row.find_all('td')
    if (len(tds) < 2):
        continue
    a = tds[1].find('a')
    date = getVal(tds[0].find('div'))
    date = datetime.datetime.strptime(date, '%B %d %Y').strftime('%Y-%m-%d')
    title = getVal(a)
    pdf_id = a['href'].split(',')[1].replace('\'', '').replace(')', '').strip()
    print date
    print title
    print pdf_id
    print '-------'
