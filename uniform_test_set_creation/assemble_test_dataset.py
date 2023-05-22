import os
from tqdm import tqdm
import shutil
 
 
#creates test dataset using all frames (txt files) from "only_fish" and every 10th from "only_empty" directories
#this version works in format: directory of unzipped yolov1 CVAT exports


if __name__ == "__main__":
    d = os.getcwd()
    #get annotated batches
    ann_batches = [x for x in os.listdir(d) if x.startswith("fishlabelled")]

    empty_d = os.path.join(d,"only_empty")
    fish_d = os.path.join(d,"only_fish")
    #establish counts

    #create test directory
    if not os.path.exists('test'):
        os.makedirs('test')
    
    if len(os.listdir("test"))!= 0:
        print("Test directory not empty, please remove items.")
        quit()
    
    trans_fish_frame_count = 0
    trans_empty_frame_count = 0
    total_test_count = 0

    allocator = 0 #numeric flag that allocates every 10th empty image to test set

    #transfer every 10th empty frame to test
    for empty_frame in tqdm(os.listdir(empty_d)):
        txt_f = os.path.join(empty_d,empty_frame)
        allocator+=1
        if allocator == 10:
           trans_empty_frame_count +=1
           total_test_count +=1
           shutil.copy(txt_f, "test") 
           allocator = 0
    
    #transfer every fish frame to test
    for fish_frame in tqdm(os.listdir(fish_d)):
        txt_f = os.path.join(fish_d,fish_frame)
        trans_fish_frame_count +=1
        total_test_count +=1
        shutil.copy(txt_f, "test") 


    print("Total test frames:", total_test_count)
    print("Total fish test frames:",trans_fish_frame_count)
    print("Total empty test frames:",trans_empty_frame_count)


