try:
    f = open('/Users/fuwei/PycharmProjects/untitled/hello.py', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('/Users/fuwei/PycharmProjects/untitled/error.py', 'r') as f:
    print(f.read())

import os
print(os.name)
print(os.uname())
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.join(os.path.abspath('.'), 'testdir'))
#os.mkdir(os.path.join(os.path.abspath('.'), 'testdir'))
os.rmdir('/Users/fuwei/PycharmProjects/untitled/testdir')