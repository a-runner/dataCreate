%author:coplin  
%time:2016-10-10  
%function:change the size of Image.  
addpath('D:\DATA\RealSRSet+5images\HR');  
addpath('D:\DATA\RealSRSet+5images\LR_matlab\X4');  
ListName=dir('D:\DATA\RealSRSet+5images\HR\*.jpg');  
[Pm,Pn]=size(ListName);  
for iPm=1:1:Pm %读取文件夹所有图片循环      
oriImg=imread(ListName(iPm).name);    %readImg  
%cutImg=imcrop(oriImg,[50,50,255,255]);  
[m,n]=size(oriImg(:,:,1));
bi=imresize(oriImg,[floor(m/4),floor(n/4)],"bicubic");        %bi缩放为ai的0.6倍  
%endImg=imresize(cutImg,[256,256]);         %把ai转成256x256的大小  
iDealName=ListName(iPm).name;  
iDealAddress='D:\DATA\RealSRSet+5images\LR_matlab\X4\'; 
iDealAll=strcat(iDealAddress,iDealName(1:end-4),'x4.jpg');  
%ID=imresize(cutImg,1);  
imwrite(bi,iDealAll);  
end  