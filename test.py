from urllib.parse import urlparse

parsed = urlparse('http://user:pass@Netloc:80/path;parameters?query=argument&query2=argument2#fragment')

print ('scheme  : '+ parsed.scheme)   #网络协议

print ('netloc  : '+ parsed.netloc )  #服务器位置（也可呢能有用户信息）

print ('path    : '+ parsed.path)     #网页文件在服务器中存放的位置

print ('params  : '+ parsed.params)   #可选参数

print ('query   : '+ str(parsed.query.split('&')))    #连接符（&）连接键值对

print ('fragment: '+ parsed.fragment) #拆分文档中的特殊猫

print ('username: '+ parsed.username) #用户名

print ('password: '+ parsed.password) #密码

print ('hostname: '+ parsed.hostname )#服务器名称或者地址

print ('port    : ', parsed.port )
