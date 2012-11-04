import lxml.html
import urllib
import re

url = 'https://www.nluug.nl/events/nj12/programma.html'

html = urllib.urlopen(url).read()

root = lxml.html.fromstring(html)
for entry in root.xpath('//table[@id="schedule"]//td[a]'):
    anchor = entry.xpath('a')[0]
    url = anchor.get('href')
    talk_title = ' '.join(anchor.text.split())

    # The rest of the information in the node is the speaker name.
    entry.remove(anchor)
    speaker = ''.join(entry.xpath('text()'))
    speaker = re.sub('\([0-9]+ minuten\)', '', speaker)
    speaker = speaker.strip()
    print url, talk_title, speaker
