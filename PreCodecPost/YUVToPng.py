
# coding=gbk
import os
from pathlib import Path

# ����ffmpeg·�������·�������ݵ���·��
EXE_PATH = "D:\\ffmpeg.exe"
out_pathroot="E:\\data\\vimeoImg\\QP35\\intra_inter_img\\all"

#ffmpeg -s 1920x1080 -i input.yuv output.png
#ffmpeg -pixel_format yuv420p -video_size 448x256 -framerate 30 -i 000010022out_30_448x256_420p.yuv out%2d.png

## ��������
num=[]

path = "E:\\data\\vimeo_yuv_decode"  #����Ŀ¼�ĸ�Ŀ¼

files = os.listdir(path)
lenn=len(files)
n=1
for file in files:  # ����һ��Ŀ¼
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
    #     print("ת���ɹ�")
    # else:
    #     print("ת��ʧ��")
    #     num.append(filename)



