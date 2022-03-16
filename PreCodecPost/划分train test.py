# coding=gbk
import copy
from glob import glob
import os
from tqdm import tqdm
import shutil



def dive_train_test(input_path, train_path,test_path):
    """
    input_path:  all�ļ����������ͼƬ
    train_path:  ��Ҫ������train���ݼ�·��
    test_path:  ��Ҫ������test���ݼ�·��

    train_txt:  ���train���ݼ�����������
    test_txt:   ���Ϊtest���ݼ�����������
    """
    train_txt='D:\\PrePostData\\vimeo_septuplet\\sep_trainlist_out.txt'
    test_txt='D:\\PrePostData\\vimeo_septuplet\\sep_testlist_out.txt'

    # ��ȡtrain  test����
    with open(train_txt,'r') as f1:
        dd1=f1.readlines()

    with open(test_txt,'r') as f2:
        dd2=f2.readlines()

    out_path = None
    # ��������ͼƬ ����ǰ׺ѡ���Ƶ�����
    for img_name in tqdm(glob(input_path+'\\*')):
        imgname=os.path.basename(img_name)
        # ����ͼƬ�����ж��Ƿ񻮷ֵ�train���ݼ�
        for ddd in dd2:
            # �����ͼƬ��test list��
            if ddd[:9].strip() is imgname[:9]:
                out_path=test_path+'\\'+imgname
                break
        if out_path is None:
            out_path=train_path+'\\'+imgname
        # ��ʼ����ͼƬ
        shutil.copy(img_name,out_path)


        out_path = None




if __name__ == '__main__':
    dive_train_test('E:\\data\\vimeoImg\\QP35\\intra_inter_img\\all','E:\\data\\vimeoImg\\QP35\\intra_inter_img\\train','E:\\data\\vimeoImg\\QP35\\intra_inter_img\\test')
    # train_txt = 'D:\\PrePostData\\vimeo_septuplet\\sep_trainlist_out.txt'
    # with open(train_txt,'r') as f:
    #     dd=f.readlines()
    #
    # print(dd[0])  # str
    # if dd[0].strip() == "000010001":
    #     print('444')

    # if '111'=='111':
    #     print(444555)