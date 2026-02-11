import urllib.error
import urllib.request
import urllib

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    print('Deu ruim')
else:
    print('Tudo ok')
