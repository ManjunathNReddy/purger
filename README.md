# Usage guide

    purger.py

Remove all files in the system with the given extension

***

**Sample runs**: 

    python ./purger.py 

    PURGER: Use with Caution!

    Please enter the extension of the files you wish to remove: R

    INFO: System root is /

    Search results

    1) /home/manjunath/tryout.R
    2) /home/manjunath/R/Assignment 1/initial.R
    3) /home/manjunath/R/Assignment 1/final/submission.R

    Please enter the range of files(example: 1 or 1-3) you wish to exclude from deletion(X to exit and 0 to delete all): 2
After the above run, files 1 and 3 were PURGED.

    python ./purger.py 

    PURGER: Use with Caution!
    
    Please enter the extension of the files you wish to remove: txt

    INFO: System root is /

    Search results

    1) /home/manjunath/tryout.txt
    2) /home/manjunath/R/Assignment 1/initial.txt
    3) /home/manjunath/R/Assignment 2/final/submission.txt

    Please enter the range of files(example: 1 or 1-3) you wish to exclude from deletion(X to exit and 0 to delete all): 1-3
After this run, no files were purged.
