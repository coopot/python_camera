# -*- coding: utf-8 -*-
from __future__ import division
import cv2

#��ȡ����ͼƬ
img = cv2.imread("fisheye.jpg")
#���ûҶ���ֵ 
T = 40

#ת��Ϊ�Ҷ�ͼƬ
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#��ȡԭͼ��С
rows,cols = img.shape[:2]
print rows,cols

#��������ɨ��
for i in range(0,rows,1):
    for j in range(0,cols,1):
        if img_gray[i,j] >= T:
            if img_gray[i + 1,j] >= T:
                top = i
                break
    else:
        continue
    break
print 'top =',top

#��������ɨ��
for i in range(rows-1,-1,-1):
    for j in range(0,cols,1):
        if img_gray[i,j] >= T:
            if img_gray[i - 1,j] >= T:
                bottom = i
                break
    else:
        continue
    break
print 'bottom =',bottom

#��������ɨ��
for j in range(0,cols,1):
    for i in range(top,bottom,1):
        if img_gray[i,j] >= T:
            if img_gray[i,j + 1] >= T:
                left = j
                break
    else:
        continue
    break
print 'left =',left

#��������ɨ��
for j in range(cols-1,-1,-1):
    for i in range(top,bottom,1):
        if img_gray[i,j] >= T:
            if img_gray[i,j - 1] >= T:
                right = j
                break
    else:
        continue
    break
print 'right =',right

#������Ч����뾶
R = max((bottom - top) / 2,(right - left) / 2)
print 'R =',R

#��ȡ��Ч����
img_valid = img[top:top + 2 * R,left:left + 2 * R]
cv2.imwrite('fisheye_valid.jpg',img_valid)

#��ʾͼƬ
cv2.imshow('fisheye',img)
cv2.imshow("fisheye_valid",img_valid)
cv2.waitKey(0)
cv2.destroyAllWindows()