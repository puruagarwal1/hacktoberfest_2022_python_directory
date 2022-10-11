from __future__ import print_function
import cv2 as cv
import numpy as np

angle = 90                                                                                         # the angle at which we want to turn the image from the basleine 
scale = 0.7                                                                                        # the scale of the image from the reference image 
img = cv.imread(r"C:\Users\iamne\Desktop\assignment for DA\EL Project\Code\BlackAlder.png")
srcTM = np.array( [[0, 0], [img.shape[1] - 1, 0], [0, img.shape[0] - 1]] ).astype(np.float32)
print(srcTM)


i=1                                                                                            #right sheer transofrm 1
j=0                                                                                            #upper sheer transform  0
k=1                                                                                            #1


l=1.4                                                                                            #set image horizontal lenght 1
m=1.2                                                                                            #set the image vertical length 1
n=0.0              

dstTM = np.array( [[img.shape[1]*(1-i), img.shape[1]*j], [img.shape[1]*k, img.shape[0]*l], [img.shape[1]*(1-m), img.shape[0]*n]] ).astype(np.float32)
print(dstTM)
warp_mat = cv.getAffineTransform(srcTM, dstTM)                                                      # warping matrix
warp_dst = cv.warpAffine(img, warp_mat, (img.shape[1], img.shape[0]))                               # warping weights
                                                                                                    # Rotating the image after Warp
center = (warp_dst.shape[1]//2, warp_dst.shape[0]//2)

rot_mat = cv.getRotationMatrix2D( center, angle, scale )
warp_rotate_dst = cv.warpAffine(warp_dst, rot_mat, (warp_dst.shape[1], warp_dst.shape[0]))

cv.namedWindow("Output", cv.WINDOW_NORMAL)
cv.resizeWindow("Output",800,600)
cv.imshow('Output',warp_rotate_dst)                      # writing the final output image 
cv.waitKey(0)