import lxml.html
import requests

url = "http://www.bbc.co.uk"
#url_check = "frontiercouriers.com"
urls = [url]
visited = [url]

while len (urls) >0:
    try:
        site_open = requests.get(urls[0])
        soup = lxml.html.fromstring(site_open.text)

        urls.pop(0)

        for href in soup.xpath('//a/@href'):
            if 'http' in href:
                site = href
            elif href.startswith('/'):
                site = str(url+href)
            else:
                site = str(url+'/'+href)

            if site in visited:
                pass
            else:
                urls.append(site)
                visited.append(site)
                frags = site.split('/')
                print(frags)
#                print (site.split('/',1))

            
    except Exception as e:
          print ("\n"+str(e))
          print (urls[0])
          urls.pop(0)
