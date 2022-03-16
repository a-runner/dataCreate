# coding=gbk
import copy
from glob import glob
import os
from tqdm import tqdm
import shutil



def dive_train_test(input_path, out_path):
    """
    input_path:  all文件里面的所有图片
    train_path:  将要被划的train数据集路径
    test_path:  将要被划分test数据集路径

    train_txt:  标记train数据集的名字索引
    test_txt:   标记为test数据集的名字索引
    """
    train_txt='D:\\PrePostData\\vimeo_septuplet\\sep_trainlist_out.txt'
    test_txt='D:\\PrePostData\\vimeo_septuplet\\sep_testlist_out.txt'

    # 读取train  test索引
    with open(train_txt,'r') as f1:
        dd1=f1.readlines()

    with open(test_txt,'r') as f2:
        dd2=f2.readlines()

    out_path2 = None
    out_path1=None
    # 遍历所有图片 根据前缀选择复制到哪里
    for img_name in tqdm(glob(input_path+'\\*')):
        imgname=os.path.basename(img_name)

        # 根据名字判断是否划分到intra 还是inter
        if imgname[-6:-4].strip()=='01':
            # 需要划分为帧内数据集
            out_path1=out_path+'\\intra_img'

            # 判断是train还是test数据集
            # 根据图片名字判断是否划分到train数据集
            for ddd in dd2:
                # 如果该图片在test list中
                if ddd[:9].strip() == imgname[:9]:
                    out_path2 = out_path1 + '\\test\\' + imgname
                    break
            if out_path2 is None:
                out_path2 = out_path1 + '\\train\\' + imgname
            # 开始复制图片
            shutil.copy(img_name, out_path2)
            out_path2=None
            out_path1=None

        else:
            # 需要划分为帧间数据集
            out_path1=out_path+'\\inter_img'

            # 判断是train还是test数据集
            # 根据图片名字判断是否划分到train数据集
            for ddd in dd2:
                # 如果该图片在test list中
                if ddd[:9].strip() == imgname[:9]:
                    out_path2 = out_path1 + '\\test\\' + imgname
                    break
            if out_path2 is None:
                out_path2 = out_path1 + '\\train\\' + imgname
            # 开始复制图片
            shutil.copy(img_name, out_path2)
            out_path2 = None
            out_path1=None




if __name__ == '__main__':
    dive_train_test('E:\\data\\vimeoImg\\QP25\\intra_inter_img\\all','E:\\data\\vimeoImg\\QP25')
    # train_txt = 'D:\\PrePostData\\vimeo_septuplet\\sep_trainlist_out.txt'
    # with open(train_txt,'r') as f:
    #     dd=f.readlines()
    #
    # print(dd[0])  # str
    # if dd[0].strip() == "000010001":
    #     print('444')

    # if '111'=='111':
    #     print(444555)