import os

#renames all classes to same class (0), deletes empty annotation files

if __name__ == "__main__":
    d = os.listdir();
    empty = 0 #number of empty images
    no_fish = 0 #number of fish
    
    for f in d:
        if f.endswith('.txt'): # if text file (annotation)
            new_lines = [] #lines to overwrite file
            ann_im = open(f, 'r')
            lines = ann_im.readlines() # read txt file
            ann_im.close()
            if lines:
                for l in lines:
                    li = l.split(" ") #split by space
                    if li[0] != '0': # or l[0] == '4' or l[0] == '0': # if fish (0's should have been removed by previous py file. Keeping here as to not delete if ran twice (reassigned fish value))
                        li[0] = '0'
                        li = " ".join(li)
                        new_lines.append(li) #add to new text file
                        no_fish += 1
            
                ann_im = open(f, 'w') #overwrite file with new lines
                ann_im.writelines(new_lines)
                ann_im.close()

            else:
                empty += 1
                os.remove(f) # remove empty file

    print("amnt_empty =",empty)
    print("no_fish =", no_fish)


 