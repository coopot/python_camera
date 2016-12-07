# -*- coding: utf-8 -*-
from __future__ import division
import cv2

#读取鱼眼图片
img = cv2.imread("fisheye.jpg")
#设置灰度阈值 
T = 40

#转换为灰度图片
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#提取原图大小
rows,cols = img.shape[:2]
print rows,cols

#从上向下扫描
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

#从下向上扫描
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

#从左向右扫描
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

#从右向左扫描
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

#计算有效区域半径
R = max((bottom - top) / 2,(right - left) / 2)
print 'R =',R

#提取有效区域
img_valid = img[top:top + 2 * R,left:left + 2 * R]
cv2.imwrite('fisheye_valid.jpg',img_valid)

#显示图片
cv2.imshow('fisheye',img)
cv2.imshow("fisheye_valid",img_valid)
cv2.waitKey(0)
cv2.destroyAllWindows()