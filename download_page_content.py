
=>> Modo 1 <<=

from lxml import html
import requests


page = requests.get('page-url')
tree = html.fromstring(page.content)

print(page.content)

---------------------------------------------------------------------------------------------------------

=>> Modo 2 <<=

import urllib.request as ur
s = ur.urlopen(page_url)
sl = s.read()
print(s.table)

---------------------------------------------------------------------------------------------------------

=>> Modo 3 <<=

import urllib.request

url = "url"

request = urllib.request.Request(url, headers = {'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})

response = urllib.request.urlopen(request)

text_file = open("Output.txt", "w")
text_file.write(str(response.read().decode("UTF-8")))
text_file.close()

print ("Done...")
