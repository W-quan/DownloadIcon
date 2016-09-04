import requests 
print "downloading with requests"
n = 100

while n < 1000:
    ns = bytes(n)
    url = 'http://files.heweather.com/cond_icon/' + ns + '.png'
    r = requests.get(url) 
    if r.status_code == requests.codes.ok:
        print bytes(n) + ':ok'
        with open('icon/icon_' + ns + ".png", "wb") as code:
            code.write(r.content)
    n = n + 1
