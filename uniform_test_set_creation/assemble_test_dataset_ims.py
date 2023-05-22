import os
from tqdm import tqdm
import shutil

#copies frame images corresponding to those in text annotation folder to diretory

#this version works in format: directory containing folder "test" of test annotation files

if __name__ == "__main__":

    #create test directory
    if not os.path.exists('test_ims'):
        os.makedirs('test_ims')
    
    if len(os.listdir("test_ims"))!= 0:
        print("Test frames directory not empty, please remove items.")
        quit()

    frame_p = r"INSERT DIRECTORY HERE" #path of directory contain ALL FRAMES
    cwd = os.getcwd()
    txt_test_dir = os.path.join(cwd,"test")

    transferred_ims = 0 #number of images transferred

    ann_ims = [] # image names of annotations

    for f in os.listdir(txt_test_dir):
        if f.endswith('.txt'): # if text file (annotation)
            im_name = f.split('.')[:-1]
            im_name.append('jpg') #get image name from text name
            im_name = ".".join(im_name)
            ann_ims.append(im_name)

    #if image in annotated, transfer
    for f in tqdm(os.listdir(frame_p)):
        if f.endswith('.jpg'): # if image file
            if f in ann_ims:
                f_p = os.path.join(frame_p,f)
                shutil.copy(f_p, "test_ims")
                transferred_ims += 1

    print("Transferred images =", transferred_ims)
