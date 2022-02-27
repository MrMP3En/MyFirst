import requests

print(requests.get('http://soft98.ir').content)

f=open('file1.txt', 'w+')
f.write('ali')
f.close()