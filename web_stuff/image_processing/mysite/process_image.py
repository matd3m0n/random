from image import Image
from math import radians
from os.path import splitext

from scipy.ndimage import gaussian_filter

def process_image(fp):
    # given filepath saves rotated image and returns new fp
    # load image
    img = Image(fp)
    # rotate image
    if 1==1: # rotate
        img_rot = img.rotate(radians(45))
        img_rot.ar = gaussian_filter(img_rot.ar,
                sigma=100, radius=(3,3,1))

        # save image
        new_fp = '%s_rot%s'%(splitext(fp)[0], splitext(fp)[1])
        img_rot.save(new_fp)
        # return new fp
        return new_fp

    else: # debug
        # save image
        new_fp = '%s_rot%s'%(splitext(fp)[0], splitext(fp)[1])
        img.save(new_fp)
        # return new fp
        return new_fp


