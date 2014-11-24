import lxml.html
import requests
import socket

url = "http://www.coding2learn.org"
urls = [url]
visited = [url]
domains=[]


while len (domains) < 1000:
    try:
        site_open = requests.get(urls[0])
        print('NOW LOOKING AT '+urls[0])
        soup = lxml.html.fromstring(site_open.text)
        urls.pop(0)
        
        for href in soup.xpath('//a/@href'):
            if 'http' in href:
                site = href
            elif href.startswith('/'):
                site = str(url+href)
            else:
                site = str(url+'/'+href)

            domain = site.split('/')[2]
            domain = domain.split('?')[0]
            url = 'http://'+domain
            if url not in visited:
                urls.append(url)
                visited.append(url)
                print('STORING '+url)
           
                domains.append(domain)
                print(len(domains))
            if len(domains) > 1000:
                break


    except:
        print ('DANGER')
        urls.pop(0)
        print (urls[0])

with open('domains.txt', mode='wt', encoding='utf-8') as myfile:
    for domain in domains:
        myfile.write(domain+'\n')
    myfile.close()
            
with open('ips.txt', mode='wt', encoding='utf-8') as myfile:
    for domain in domains:
        try:
            myfile.write(socket.gethostbyname(domain)+'\n')
        except:
            myfile.write('No IP Supplied\n')
    myfile.close()
