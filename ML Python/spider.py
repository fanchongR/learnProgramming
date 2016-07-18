import urllib.request
import urllib.parse

response=urllib.request.urlopen('http://www.baidu.com/')    #发送请求，获取url
html=response.read()                 #读入
print(html)

或
req=urllib.request.Request('http://www.baidu.com/')
response=urllib.request.urlopen(req)
the_page=response.read()
print the_page

##

url = 'http://www.someserver.com/register.cgi'    
values = {'name' : 'WHY','location' : 'SDU', 'language' : 'Python' }
data=urllib.parse.urlencode(values)          #编码工作
data = data.encode('utf-8')
req=urllib.request.Request(url,data)          #发送请求同时传data表单
response=urllib.request.urlopen(req)          #接受反馈信息
the_page=response.read()

##

设置headers，把自身模拟成IE，浏览器确认自己身份是通过User-Agent头。
因为有一些站点不喜欢被程序（非人为访问）访问

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'    #IE
headers = { 'User-Agent' : user_agent }   

values = {'name' : 'WHY','location' : 'SDU', 'language' : 'Python' }
data=urllib.parse.urlencode(values)
data = data.encode('utf-8')
req=urllib.request.Request(url,data,headers)
response=urllib.request.urlopen(req)
the_page=response.read()

#####

URLError处理

req = urllib.request.Request('http://www.baibai.com')
urllib.request.urlopen(req)

错误防范代码  balabala

#####

urlopen 返回的对象response的geturl() #返回获取的真实url  和info() #页面抓取情况

old_url = 'http://rrurl.cn/b1UZuP'
req = urllib.request.Request(old_url)
response=urllib.request.urlopen(req)
response.geturl()
print(response.info())


######
使用个性化的opener去获取url

password_mgr=urllib.request.HTTPPasswordMgrWithDefaultRealm()  #创建一个密码管理者
top_level_url = "http://example.com/foo/"
password_mgr.add_password(None, top_level_url,'why', '1223')  #password_mgr.add_password(None, top_level_url, username, password)  ## 如果知道 realm, 我们可以使用他代替 ``None``  # 添加用户名和密码
handler=urllib.request.HTTPBasicAuthHandler(password_mgr)  #创建了一个新的handler
opener=urllib.request.build_opener(handler)  #创建 "opener" (OpenerDirector 实例)
opener.open('http://www.baidu.com/') # 使用 opener 获取一个URL
<http.client.HTTPResponse object at 0x02629790>

urllib.request.install_opener(opener)   #安装 opener 现在所有调用 urllib.request.urlopen 将用我们的 opener.


#####

设置Proxy
enable_proxy = True
proxy_handler = urllib.request.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib.request.ProxyHandler({})
if enable_proxy:
	opener = urllib.request.build_opener(proxy_handler)
else:
	opener = urllib.request.build_opener(null_proxy_handler)
urllib.request.install_opener(opener)          #全局改变opener，可以opener.open来打开


设置 timeout  即超时
response = urllib.request.urlopen('http://www.google.com', timeout=10)

加入 header
request = urllib.request.Request('http://www.baidu.com/')  
request.add_header('User-Agent', 'fake-client')  
response = urllib.request.urlopen(request)  
print(response.read())
#http://blog.csdn.net/pleasecallmewhy/article/details/8925978

检测和设置是否Redirect
需要得到cookie值
使用 HTTP 的 PUT 和 DELETE 方法
得到 HTTP 的返回码
Debug Log
表单的处理  Request里的data


伪装成浏览器
headers = {  
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
}  
req = urllib.request.Request(  
    url = 'http://secure.verycd.com/signin/*/http://www.verycd.com/',  
    data = postdata,  
    headers = headers  
)  


对付"反盗链"
headers = {'Referer':'http://www.cnbeta.com/articles'}   #把Referer改成要爬的网站


#################################################################################

简单的百度贴吧的小爬虫

def baidu_tieba(url,begin_page,end_page):     
    for i in range(begin_page, end_page+1):  
        sName = str(i) + '.html'                       #自动填充成六位的文件名  
        print('正在下载第' + str(i) + '个网页，并将其存储为' + sName)  
        f = open(sName,'wb')  
        m = urllib.request.urlopen(url + str(i)).read()  
        f.write(m)  
        f.close()


baidu_tieba(r"http://tieba.baidu.com/p/2296017831?pn=",1,5)



################################################################################

BeautifulSoup
#http://www.crifan.com/files/doc/docbook/python_topic_beautifulsoup/release/html/python_topic_beautifulsoup.html  教程
#http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html   包的文档

from bs4 import BeautifulSoup
soup=BeautifulSoup(m)
print(soup.prettify())     #HTML标准缩进输出

>>> soup.title
<title>你妹啊，死活找不到男朋友啊~~心凉啊~~_山东大学吧_百度贴吧</title>
>>> soup.title.name
'title'
>>> soup.title.string
'你妹啊，死活找不到男朋友啊~~心凉啊~~_山东大学吧_百度贴吧'
>>> soup.title.parent.name
'meta'

#找出第一个这种结构的
>>> soup.p
<p class="switch_radios" style="display:none;"><input c ...
>>> soup.a
<a class="search_logo" href="/" style="" title="到贴吧首页"></a>
>>> soup.a.get('class')     soup.a['class']
['search_logo']
>>> soup.td
<td>日</td>

soup.find_all('a')
soup.find(id="search_logo_small")   #<a class="" href="/" id="search_logo_small" title="到贴吧首页"></a>
P=re.compile("\w+_\w+_\w+")   soup.findAll(id=P)   #找出全部符合正则的

attrsList = soup.attrs   #得到元组列表
attrMap = soup.attrMap   #得到字典
