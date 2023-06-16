import os
import pandas as pd

#CONVERT CSV TO YOLO (ASSUMES ALL CLASS '0')

dest = "DEST PATH" #Destination Folder for yolo annotations

df_antt = pd.read_csv("CSV FILE") #OG csv file
fname = df_antt["filename"].values
xmin = df_antt["xmin"].values
ymin = df_antt["ymin"].values
xmax = df_antt["xmax"].values
ymax = df_antt["ymax"].values
width = df_antt["width"].values #width and height of IMAGES
height = df_antt["height"].values

for i, name in enumerate(fname): # for filename (image name) in csv
    xcen = float((xmin[i] + xmax[i])) / 2 / width[i] #normalise bboxes for yolo according to image size (YOLO is in format <class> <x centroid> <y centroid> <bb width> <bb height>)
    ycen = float((ymin[i] + ymax[i])) / 2 / height[i]

    w = float((xmax[i] - xmin[i])) / width[i]
    h = float((ymax[i] - ymin[i])) / height[i]

    im_name = name.split('.')[:-1]
    im_name.append('txt') #get image name from text name
    ann_Txt = ".".join(im_name)
    dest_save = os.path.join(dest,ann_Txt) #save txt file as image name with extension change
    with open(dest_save, 'a+') as f:
        f.write(f"0 {xcen} {ycen} {w} {h}\n")

