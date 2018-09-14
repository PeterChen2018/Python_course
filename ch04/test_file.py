'''
Hello world!
歡迎使用 Python 存取檔案。
檔案的編碼是 UTF-8。
'''

f=open('file1.txt','r', encoding = 'UTF-8')
print(f.readline())
print(f.readline())

f.seek(0)
for line in f:
    print(line.strip())
    
f.close()