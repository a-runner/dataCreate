# coding=gbk

import os
from pathlib import Path
from glob import glob

# 设置ffmpeg路径
EXE_PATH = "D:\\ffmpeg.exe"

## 批量处理

path = "E:\\data\\vimeo_264\\QP20"  ##数据目录的根目录
files = os.listdir(path)
lenn=len(files)
n=1
for file in files:  # 读第一层目录
    f = path + "\\" + file
    for filesend in f:
        filetemp=f+"\\"+filesend
        filename=Path(filetemp).stem
    filename=Path(f).stem
    print('[ {} | {}] : '.format(n,lenn),filename)
    n=n+1
    input_dir=f
    h265_dir="E:\\data\\vimeo_yuv_de\\QP20"+"\\"+filename+".yuv"
    # outyuv_dir="D:\\YUVView\\decoder_yuv"+"\\"+"encoder"+filename+".yuv"
    # print(h265_dir)
    # print(outyuv_dir)
    # cmd_line='%s --preset medium --input-res 448x256 --input-depth 8 --fps 30 --frames 7 "%s" --qp 35 -o "%s" -r "%s"' %(EXE_PATH,input_dir,h265_dir,outyuv_dir)
    cmd_line = '%s  -i "%s" -vcodec rawvideo -an "%s" -loglevel quiet' % (
    EXE_PATH, input_dir, h265_dir)
    ret=os.system(cmd_line)