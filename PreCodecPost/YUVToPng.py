
# coding=gbk
import os
from pathlib import Path

# 设置ffmpeg路径，输出路径、数据导入路径
EXE_PATH = "D:\\ffmpeg.exe"
out_pathroot="E:\\data\\vimeoImg\\QP35\\intra_inter_img\\all"

#ffmpeg -s 1920x1080 -i input.yuv output.png
#ffmpeg -pixel_format yuv420p -video_size 448x256 -framerate 30 -i 000010022out_30_448x256_420p.yuv out%2d.png

## 批量处理
num=[]

path = "E:\\data\\vimeo_yuv_decode"  #数据目录的根目录

files = os.listdir(path)
lenn=len(files)
n=1
for file in files:  # 读第一层目录
    f = path + "\\" + file
    filename = Path(f).stem
    # print(filename)

    input_path=f
    print('[ {} | {}] : '.format(n, lenn), filename)
    n = n + 1

    out_path=out_pathroot+"\\"+filename+"%2d.png"

    cmd_line='%s -pixel_format yuv420p -video_size 448x256 -framerate 30 -i "%s" "%s" -loglevel quiet' %(EXE_PATH,input_path,out_path)
    ret=os.system(cmd_line)
    # if ret==0:
    #     print("转换成功")
    # else:
    #     print("转换失败")
    #     num.append(filename)



