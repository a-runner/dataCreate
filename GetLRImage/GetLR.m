%author:coplin  
%time:2016-10-10  
%function:change the size of Image.  
addpath('D:\DATA\RealSRSet+5images\HR');  
addpath('D:\DATA\RealSRSet+5images\LR_matlab\X4');  
ListName=dir('D:\DATA\RealSRSet+5images\HR\*.jpg');  
[Pm,Pn]=size(ListName);  
for iPm=1:1:Pm %��ȡ�ļ�������ͼƬѭ��      
oriImg=imread(ListName(iPm).name);    %readImg  
%cutImg=imcrop(oriImg,[50,50,255,255]);  
[m,n]=size(oriImg(:,:,1));
bi=imresize(oriImg,[floor(m/4),floor(n/4)],"bicubic");        %bi����Ϊai��0.6��  
%endImg=imresize(cutImg,[256,256]);         %��aiת��256x256�Ĵ�С  
iDealName=ListName(iPm).name;  
iDealAddress='D:\DATA\RealSRSet+5images\LR_matlab\X4\'; 
iDealAll=strcat(iDealAddress,iDealName(1:end-4),'x4.jpg');  
%ID=imresize(cutImg,1);  
imwrite(bi,iDealAll);  
end  