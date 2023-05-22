import os
from tqdm import tqdm

#Get all dataset frames, empty frames, frames with annotations, frames with fish, and instances of fish
#Works in already pooled txt files in folder "all_txt"
if __name__ == "__main__":
    cwd = os.getcwd()
    print(cwd)
    d = os.path.join(cwd,"all_txt")
    txt_fs = os.listdir(d)
    frame_count= len(txt_fs)
    empty_frame_count = 0
    fish_frame_count = 0
    fish_instances_count = 0

    for f in tqdm(txt_fs):
        if f.endswith('.txt'): # if text file (annotation)
            ann_txt = open(os.path.join(d,f), 'r')
            lines = ann_txt.readlines() # read txt file
            ann_txt.close()

            if lines: # if lines, theres annotations AKA fish present
                fish_frame_count += 1
                for l in lines:
                    fish_instances_count +=1 #count lines AKA fish

            else:
                empty_frame_count += 1 #otherwise count as empty frame

    print("Frame Count:",frame_count)
    print("Empty Frame Count:",empty_frame_count)
    print("Fish Frame Count:",fish_frame_count)
    print("Fish Instances Count:",fish_instances_count)


