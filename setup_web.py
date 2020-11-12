import os
import shutil
import sys
import zipfile

dir_path = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists('www'):
    sys.exit('Can\'t find www directory')

print("Copying web files")
command = 'cp -rf "{}/"* www'.format(os.path.normpath(os.path.join(dir_path, 'web')))
#print(command)
os.system(command)

print("Extracting item icons")
with zipfile.ZipFile(os.path.join(dir_path, 'assets/items.zip'), 'r') as zf:
    zf.extractall('www/img')

print("Extracting entities icons")
with zipfile.ZipFile(os.path.join(dir_path, 'assets/entities.zip'), 'r') as zf:
    zf.extractall('www/img')

print("Done!")
