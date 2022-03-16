import cv2
import numpy
import copy
from glob import glob
import os


def ImageMarker(path,savepath):

    for imname in glob(path+'/*'):
        # 提取文件名
        jpgName=os.path.basename(imname)
        (imgpre, imgext) = os.path.splitext(os.path.basename(imname))

        # 代表用户是否满意
        saty=0
        c_w=0
        c_h=0

        img = cv2.imread(imname)
        h, w, c = img.shape
        if (h<1080)|(w<1920):
            mode=2
        else:
            mode=1
        # 首先判断图片大小，决定采用1920*1080（模式一）还是1080*720（模式二）
        if mode==1:
            ww = 1920
            hh = 1080
            if hh/h>ww/w:
                # height将缩放到为1080大小
                s=1
                new_w=int(hh/h*w)
                new_h=hh
            else:
                # width将缩放到1920大小 s=0用来标记width刚好1920
                s=0
                new_w=ww
                new_h=int(ww/w*h)
                new_w=ww
            print('采用模式一: 1920*1080')
            savepath=savepath+'/H/'+imgpre+'.png'
        else:
            ww = 1080
            hh = 720
            if hh / h > ww / w:
                # height将缩放到为1080大小
                s = 1
                new_w = int(hh / h * w)
                new_h = hh
            else:
                # width将缩放到1920大小 s=0用来标记width刚好1920
                s = 0
                new_w = ww
                new_h = int(ww / w * h)
                new_w = ww
            print('采用模式二: 1080*720')
            savepath = savepath + '/L/'+imgpre+'.png'
        # 得到新图像大小  （需要考虑因小数而引起的一像素差距）
        img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
        pic=copy.deepcopy(img)
        pic2=copy.deepcopy(img)
        print(new_h)
        print(new_w)
        # 添加横纵坐标格  一格代表10像素
        window_size=100
        for i in range(new_h//window_size):
            cv2.line(img, (0,(i+1)*window_size), (new_w-1, (i+1)*window_size), color=(255, 0, 0), thickness=3)
        for j in range(w//window_size):
            cv2.line(img,((j+1)*window_size,0),((j+1)*window_size,new_h-1),color=(255,0,0),thickness=3)

        cv2.rectangle(img, (0,0), (new_w-ww,new_h-hh), color=(0, 0, 255), thickness=9)
        # 选择截取的范围
        print("该图像可以选择的截取点（矩形左上点）：")
        print('X: [{}-{}]'.format(new_w-ww,new_h-hh))
        cv2.namedWindow('animal',0)
        cv2.resizeWindow('animal',600,800)
        cv2.imshow('animal',img)
        cv2.waitKey(0)
        while saty!=1:
            c_w=input("请输入矩形左上角x坐标：")
            c_h=input("请输入矩形左上角y坐标：")
            c_w=int(c_w)
            c_h=int(c_h)
            cv2.namedWindow('crop-animal',0)
            cv2.resizeWindow('crop-animal', 600, 800)
            cv2.rectangle(pic,(c_w,c_h),(c_w+ww,c_h+hh),color=(0,255,0),thickness=4)
            cv2.imshow('crop-animal',pic)
            cv2.waitKey(5000)
            # cv2.destroyWindow(imgname)
            saty=int(input("是否满意？1为满意0为不满意"))
            cv2.destroyWindow('crop-animal')

        cv2.destroyAllWindows()

        # 保存图片
        crop=pic2[c_h:c_h+hh,c_w:c_w+ww]
        cv2.imwrite(savepath,crop)


if __name__ == '__main__':
    ImageMarker('D:/DA/food','D:/DA/foodCrop')