import cv2 as cv
import numpy as np

def main(path1, path2):
    im1, im2 = cv.imread(path1), cv.imread(path2)
    dif_path = 'difference.png'
    gray1, gray2 = cv.cvtColor(im1, cv.COLOR_BGR2GRAY), cv.cvtColor(im2, cv.COLOR_BGR2GRAY)
    norm1 = (gray1 - gray1.min()) / (gray1.max() - gray1.min())
    norm2 = (gray2 - gray2.min()) / (gray2.max() - gray2.min())
    dif = np.abs(norm2 - norm1)
    abs_dif = dif.sum()
    abs_dif_pixel = dif.sum() / dif.shape[0] / dif.shape[1]
    print('Based on on L1 absolute difference, the difference between images equals to %2f, and the mean pixel difference equals to %2f' %(abs_dif, abs_dif_pixel))
    print('Image %s is the visualization of the difference' %dif_path)
    cv.imwrite(dif_path, (dif*255).astype(np.uint8))

if __name__ == "__main__":
    # path1 = input('Insert the path to image 1    ')
    # path2 = input('Insert the path to image 2    ')
    path1 = 'test_data/diff_test/test_image_1.png'
    path2 = 'test_data/diff_test/test_image_2.png'
    main(path1, path2)