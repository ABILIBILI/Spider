'''
��һ��ʾ�����򵥵���ҳ����

��ȡ������ҳ
'''

import urllib.request

#��ַ
url = "http://www.douban.com/"

#����
request = urllib.request.Request(url)

#��ȡ���
response = urllib.request.urlopen(request)

data = response.read()

#���ý��뷽ʽ
data = data.decode('utf-8')

#��ӡ���
print(data)

#��ӡ��ȡ��ҳ�ĸ�����Ϣ

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())