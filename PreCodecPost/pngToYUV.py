# 将图片转化为YUV序列
import os
from tqdm import tqdm

# 设置ffmpeg路径
EXE_PATH = "D:\\ffmpeg.exe"

## 批量处理

path="D:\\PrePostData\\vimeo_septuplet\sequences"              ##数据目录的根目录
files=os.listdir(path)
for file in tqdm(files):                                #读第一层目录
    f=path+"\\"+file
    files1=os.listdir(f)
    
    for filesend in files1:                             #读第二层目录
        # print(filesend)
        src_dir=f+"\\"+filesend+"\\"+"im%1d.png"
        dst_dir="D:\\PrePostData\\vimeo_yuv"+"\\"+file+filesend+"out_30_448x256_420p"+".yuv"  ##保存到路径并命名
        cmd_line = '%s -r 30 -i "%s" -pix_fmt yuv420p -s 448x256 "%s" -loglevel quiet' % (EXE_PATH, src_dir,dst_dir)
        ret = os.system(cmd_line)
        # if ret == 0:
        #     print("-转换成功.",filesend)
        # else:
        #     print("-转换失败:", filesend)












