import logging

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
except ValueError as e:
    print('ValueError', e)
finally:
    print('finally...')
print('end')


def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
main()

def main1():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main1()
print('END')

