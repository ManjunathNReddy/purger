import sys
import os
import shutil

from pathlib import Path

if __name__ == '__main__':
    print('\nPURGER: Use with Caution!\n')

    extension = input('Please enter the extension of the files you wish to remove: ')
    extension = '*.{}'.format(extension)

    sys_root_dir = None
    if os.name == 'nt':
        # On windows, the drive letter can be separated
        sys_root_dir = os.path.splitdrive(sys.executable)[0]
    else:
        sys_root_dir = os.path.splitdrive(sys.executable)[1][0]

    print('\nINFO: System root is {}\n'.format(sys_root_dir))

    print('Search results\n')
    # Search through all the directories in the root and save the list
    search_results = {}
    for result_num,filename in enumerate(Path(sys_root_dir).rglob(extension),start=1):
        search_results[result_num]=filename
        print('{}) {}'.format(result_num,filename))
    
    exclude_range = input('\n Please enter the range of files(example: 1 or 1-3) you wish to exclude from deletion(X to exit and 0 to delete all): ')
    
    if exclude_range.lower() == 'x':
        sys.exit()
    
    if exclude_range != str(0):
        # Expand the range
        range_list = exclude_range.split('-')
        first = int(range_list[0])
        last = int(range_list[-1])+1

        # Remove from the search results
        for result in range(first,last):          
            try:
                del search_results[result]
            except KeyError:
                pass

    # Remove all items in search results
    for file_path in search_results.values():
        os.remove(file_path)