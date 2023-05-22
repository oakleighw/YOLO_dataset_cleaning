import os
import numpy
from tqdm  import tqdm 

#removes images without USEFUL annotations (assumes delete_non_fish.py then pool_fish_class.py)
#Put this in directory containing /images and /labels (e.g. 'train' in a YOLO file)


if __name__ == "__main__":
    cwd = os.getcwd()
    d = cwd+ '/fish_only_txt' #labels directory
    dL = os.listdir(d); 

    empty = 0 #number of empty images
    no_fish = 0 #number of fish
    no_misc = 0 #number non-fish

    ann_ims = [] # image names of annotations

    for f in dL:
        if f.endswith('.txt'): # if text file (annotation)
            fd = d + '/'+ f
            im_name = f.split('.')[:-1]
            im_name.append('jpg') #get image name from text name
            im_name = ".".join(im_name)
            ann_ims.append(im_name)

 
    print("Amount anno images=", len(ann_ims))
    im_d = cwd+ '/just_fish_01'
    im_dL = os.listdir(im_d)
    print("Amount dir ims=", len(im_dL))

    kept_ims = 0 
    del_ims = 0

    for f in tqdm(im_dL):
        if f in ann_ims:
            kept_ims += 1 #keep images with annotations
        else:
            im_p = im_d + '/' + f
            del_ims += 1
            os.remove(im_p) #else remove

    print("Kept ims =", kept_ims)
    print("deleted ims =", del_ims)