import os
from tqdm import tqdm
import shutil

#Get all dataset frames, empty frames, frames with annotations, frames with fish, and instances of fish
if __name__ == "__main__":
    cwd = os.getcwd()
    print(cwd)
    d = os.path.join(cwd,"all_txt")
    txt_fs = os.listdir(d)
    frame_count= len(txt_fs)
    transferred_txts = 0
    left_txts = 0
    #make directory for fish only dataset
    fish_txt_d = os.path.join(cwd,"fish_only_txt")
    if not os.path.exists(fish_txt_d):
        os.makedirs(fish_txt_d)

    if len(os.listdir(fish_txt_d)) != 0:
        print("Fish file contains contents! Remove before transfer please.")
        quit()

    for f in tqdm(txt_fs):
        if f.endswith('.txt'): # if text file (annotation)
            f_path = os.path.join(d,f)
            ann_txt = open(f_path, 'r')
            lines = ann_txt.readlines() # read txt file
            ann_txt.close()

            if lines: # if lines, theres annotations AKA fish present
                transferred_txts += 1
                shutil.copyfile(f_path, os.path.join(fish_txt_d,f))

            else:
                left_txts += 1 #otherwise count as empty frame

    print(f"Transferred {transferred_txts} annotation files and left {left_txts}.")





