import os

#deletes non-fish (FISH ID = 1 (fish) 4(small fish))

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
                    if l[0] == '1' or l[0] == '4': # if fish
                        no_fish += 1
                        new_lines.append(l) #add to new text file
                    else:
                        no_misc +=1
            
                ann_im = open(f, 'w') #overwrite file with new lines
                ann_im.writelines(new_lines)
                ann_im.close()

                #print(lines[0], 'next \n')
            else:
                empty += 1

    print("amnt_empty =",empty)
    print("no_fish =", no_fish)
    print("no_misc =", no_misc)

