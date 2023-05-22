import os
from tqdm import tqdm
import shutil
 
 
#pools annotated text file data into empty frame directory and only_fish directory
#this version works in format: directory of unzipped yolov1 CVAT exports
###################

if __name__ == "__main__":
    d = os.getcwd()
    #get annotated batches
    ann_batches = [x for x in os.listdir(d) if x.startswith("fishlabelled")]

    #establish counts
    frame_count= 0
    empty_frame_count = 0
    fish_frame_count = 0
    fish_instances_count = 0

    #create empty directory
    if not os.path.exists('only_empty'):
        os.makedirs('only_empty')
    
    #create fish directroy
    if not os.path.exists('only_fish'):
        os.makedirs('only_fish')

    #check if directories are empty
    if len(os.listdir("only_empty"))!= 0 or len(os.listdir("only_fish"))!= 0:
        print("A directory not empty, please remove items.")
        quit()

    #file destinations
    empty_dest = os.path.join(d,'only_empty')
    fish_dest = os.path.join(d,'only_fish')

    #get text annotated files folder within batches
    for batch in ann_batches:
        txt_ann_dir = os.path.join(batch,"obj_train_data")

        for f in tqdm(os.listdir(txt_ann_dir)):
            txt_f = os.path.join(txt_ann_dir,f)
            if txt_f.endswith('.txt'): # text file validation
                ann_txt = open(txt_f, 'r')
                lines = ann_txt.readlines() # read txt file
                ann_txt.close()

                if lines: # if lines, theres annotations AKA fish present
                    # Source path
                    fish_source = txt_f
                    frame_count += 1
                    fish_frame_count += 1
                    for l in lines:
                        fish_instances_count +=1 #count lines AKA fish
                    shutil.copy(fish_source, fish_dest) #copy fish file
                    

                else:
                    frame_count += 1
                    empty_frame_count += 1 #otherwise count as empty frame
                    empty_source = txt_f
                    shutil.copy(empty_source, empty_dest) #copy empty file




    print("Frame Count:",frame_count)
    print("Empty Frame Count:",empty_frame_count)
    print("Fish Frame Count:",fish_frame_count)
    print("Fish Instances Count:",fish_instances_count)


