

#测试一下第三方库

from PIL import Image
#注意转义
im =Image.open("C:\\Users\\Administrator\\Desktop\\test.jpg")


print(im.format,im.size,im.mode)

print(im)

im.thumbnail((100,200))
im.save('C:\\Users\\Administrator\\Desktop\\thumb.jpg', 'JPEG')