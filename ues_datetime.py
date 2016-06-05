from datetime import datetime

now = datetime.now()
print(now)

print(type(now))

dt = datetime(2015, 4, 19, 23, 49)
print(dt)
print(dt.timestamp())

t = 1429458540.0
print(datetime.fromtimestamp(t))




from PIL import Image
im = Image.open('test.jpg')
w, h = im.size
print('Original image size: %sx%s' % (w, h))

im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
im.save('thumbnail.jpg', 'jpeg')