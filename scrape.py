import lxml.html
import urllib

url = 'https://www.nluug.nl/events/nj12/programma.html'

html = urllib.urlopen(url).read()

root = lxml.html.fromstring(html)
tds = root.xpath('//table[@id="schedule"]//td')
print len(tds)
