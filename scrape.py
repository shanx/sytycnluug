import lxml.html
import urllib

url = 'https://www.nluug.nl/events/nj12/programma.html'

html = urllib.urlopen(url).read()

root = lxml.html.fromstring(html)
for entry in root.xpath('//table[@id="schedule"]//td[a]'):
    anchor = entry.xpath('a')[0]
    print anchor.get('href')
