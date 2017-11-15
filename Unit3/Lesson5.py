

#struct 处理直接文件

"""struct.unpack('<ccIIIIIIHH', s)
(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。

请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。"""

import  struct ,logging
def  check(path):
  try:
      with open(path, "rb") as f:
          info = struct.unpack('<ccIIIIIIHH', f.read(30))
          if info[0] == b"B" and info[1] == b"M":
              print("是BMP图像")
              print(info)
              print("宽", info[-4], "高", info[-3])
              print("颜色数", info[-1])
          else:
              print("不是BMP图像")
              #捕获异常
  except FileNotFoundError as e:
      logging.exception(e)





path ="C:\\Users\\Administrator\\Desktop\\test.bmp"

check(path)