clear,clc,close all;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Pools frame names in natural numbering (not lexicographical)%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


initDir = "INITIAL DIR";
saveLoc = "SAVE LOCATION";

%list of files in dir
listing = dir(initDir);


%make sure directory is empty
if isempty(listing)
    disp("Directory not empty, please remove images before frame pooling.");
    quit;
end


f = waitbar(0,"Converting frames");
for i = 1:length(listing)
    if regexp(listing(i).name, "s?\.mp4") %Change .mp4 if not in that format
        disp(listing(i).name);
        vidTitle = listing(i).name;
        data = initDir + "\" + vidTitle;
        videoSource = VideoReader(data);
        fno = 0;%frame number
        while hasFrame(videoSource)
            saveName = vidTitle + "_" + string(fno) + ".jpg"; %saves as jpg
            %get frame
            frame = readFrame(videoSource);
            saveNameLoc = saveLoc + "\" + saveName;
            imwrite(frame, saveNameLoc);
            fno = fno + 1;
        end        
    end
    waitbar((i/length(listing)),f);
end
close(f);


