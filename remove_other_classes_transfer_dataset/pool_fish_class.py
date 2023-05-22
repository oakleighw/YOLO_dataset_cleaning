import os

#renames both class 1(fish) and class 4(small fish) to same class (0), deletes empty annotation files

if __name__ == "__main__":
    d = os.listdir();
    empty = 0 #number of empty images
    no_fish = 0 #number of fish
    no_misc = 0 #number non-fish
    for f in d:
        if f.endswith('.txt'): # if text file (annotation)
            new_lines = [] #lines to overwrite file
            ann_im = open(f, 'r')
            lines = ann_im.readlines() # read txt file
            ann_im.close()
            if lines:
                for l in lines:
                    if l[0] == '1' or l[0] == '4' or l[0] == '0': # if fish (0's should have been removed by previous py file. Keeping here as to not delete if ran twice (reassigned fish value))
                        li = list(l)
                        li[0] = '0'
                        li = "".join(li)
                        new_lines.append(li) #add to new text file
                        no_fish += 1
                    else:
                        no_misc +=1
                #print(new_lines)
            
                ann_im = open(f, 'w') #overwrite file with new lines
                ann_im.writelines(new_lines)
                ann_im.close()

                #print(lines[0], 'next \n')
            else:
                empty += 1
                os.remove(f) # remove empty file

    print("amnt_empty =",empty)
    print("no_fish =", no_fish)
    print("no_misc =", no_misc)

 