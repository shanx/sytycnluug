import lxml.etree
import urllib

url = 'https://www.nluug.nl/events/nj12/programma.html'

html = urllib.urlopen(url).read()

xml = lxml.etree.fromstring(html)
