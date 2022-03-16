# coding=gbk
import copy
from glob import glob
import os
from tqdm import tqdm
import shutil



def dive_train_test(input_path, out_path):
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

    out_path2 = None
    out_path1=None
    # ��������ͼƬ ����ǰ׺ѡ���Ƶ�����
    for img_name in tqdm(glob(input_path+'\\*')):
        imgname=os.path.basename(img_name)

        # ���������ж��Ƿ񻮷ֵ�intra ����inter
        if imgname[-6:-4].strip()=='01':
            # ��Ҫ����Ϊ֡�����ݼ�
            out_path1=out_path+'\\intra_img'

            # �ж���train����test���ݼ�
            # ����ͼƬ�����ж��Ƿ񻮷ֵ�train���ݼ�
            for ddd in dd2:
                # �����ͼƬ��test list��
                if ddd[:9].strip() == imgname[:9]:
                    out_path2 = out_path1 + '\\test\\' + imgname
                    break
            if out_path2 is None:
                out_path2 = out_path1 + '\\train\\' + imgname
            # ��ʼ����ͼƬ
            shutil.copy(img_name, out_path2)
            out_path2=None
            out_path1=None

        else:
            # ��Ҫ����Ϊ֡�����ݼ�
            out_path1=out_path+'\\inter_img'

            # �ж���train����test���ݼ�
            # ����ͼƬ�����ж��Ƿ񻮷ֵ�train���ݼ�
            for ddd in dd2:
                # �����ͼƬ��test list��
                if ddd[:9].strip() == imgname[:9]:
                    out_path2 = out_path1 + '\\test\\' + imgname
                    break
            if out_path2 is None:
                out_path2 = out_path1 + '\\train\\' + imgname
            # ��ʼ����ͼƬ
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