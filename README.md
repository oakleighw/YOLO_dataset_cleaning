
# YOLO dataset cleaning and test set creation scripts

Contains scripts for cleaning YOLO datasets, pooling frames with certain classes, and creating a test set with uniform empty frames (to assess for false positives).

Contains "fish" terminology as used with fish detection

+ **pool_vidConvert_frames_natural.m**: Creates frames from a folder of videos in format videoname_n.jpg. Note this is in natural order ('_n' not '_00n').

+ **count_instances**: 
    Contains files to count dataset objects.
    - **POOLEDALLTEXT** counts annotated frames, empty frames, and "fish" instances in a yolo label folder "all_txt".
    - **YOLO1CVAT** counts annotated frames, empty frames, and "fish" instances in a directory of extracted YOLO1 CVAT label exports.

+ **custom_dataset_clean**: 
    Contains files to move empty frame label files, class files, and remove equivalent frame images from a custom binary annotated dataset.

+ **remove_other_classes_transfer_Dataset**: 
    Files to clean YOLO datasets downloaded from other sources. E.g. for a sealife dataset, remove all crabs, pool all images with only fish.

+ **uniform_test_set_creation**: 
    Files to organise annotated test set labels and frames. Includes code to add uniformly distributed empty frames to test dataset to assess models robustness to false positives.
    
+ **csv_to_yolo.py**:
    Converts annotations in CSV format to YOLO format (Assumes one class '0').




