# requirements:
# Python 3.6
# apscheduler==3.5.1
# shutil
# os
# pathlib

import os
import shutil
from pathlib import Path
from apscheduler.schedulers.blocking import BlockingScheduler

save_file = 'save_file_name' # replace save_file_name with the name of the save file you want to copy

src_folder = 'path/to/folder/with/original/save/file' # replace with the path to the folder containing save file
src_file = Path(os.path.join(src_folder, save_file))

dest_folder = 'path/to/folder/you/want/to/copy/to' # replace with path to folder you want to copy the save file to
dest_file = Path(os.path.join(dest_folder, save_file))

def update_file(src_file, dest_folder, dest_file):
    if (dest_file.is_file()):
        os.remove(dest_file)
    shutil.copy2(src_file, dest_folder)
    
try:
    src = src_file.resolve()
except FileNotFoundError:
    print('File does not exist')
else:

    while True:
        scheduler = BlockingScheduler()
        scheduler.add_job(update_file, 'interval', args= [src_file, dest_folder, dest_file], hours=2) # can customize interval by changing number after hours=
        scheduler.start()

    
    
    

