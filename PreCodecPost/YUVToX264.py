# coding=gbk
import os
from pathlib import Path
from glob import glob

# ����ffmpeg·��
EXE_PATH = "D:\\x264.exe"

## ��������

path = "D:\\PrePostData\\vimeo_yuv"  ##����Ŀ¼�ĸ�Ŀ¼
files = os.listdir(path)
lenn=len(files)
n=1
for file in files:  # ����һ��Ŀ¼
    f = path + "\\" + file
    for filesend in f:
        filetemp=f+"\\"+filesend
        filename=Path(filetemp).stem
    filename=Path(f).stem
    print('[ {} | {}] : '.format(n,lenn),filename)
    n=n+1
    input_dir=f
    h265_dir="E:\\data\\vimeo_264\QP15"+"\\"+filename+".h264"
    # outyuv_dir="D:\\YUVView\\decoder_yuv"+"\\"+"encoder"+filename+".yuv"
    # print(h265_dir)
    # print(outyuv_dir)
    # cmd_line='%s --preset medium --input-res 448x256 --input-depth 8 --fps 30 --frames 7 "%s" --qp 35 -o "%s" -r "%s"' %(EXE_PATH,input_dir,h265_dir,outyuv_dir)
    cmd_line = '%s --preset medium --input-res 448x256 --input-depth 8 --fps 30 --frames 7 "%s" --qp 15 -o "%s" --log-level quiet' % (
    EXE_PATH, input_dir, h265_dir)
    ret=os.system(cmd_line)
    # if ret==0:
    #     print("ת���ɹ�")
    # else:
    #     print("ת��ʧ��")