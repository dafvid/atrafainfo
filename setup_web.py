import os
import shutil
import sys
import zipfile

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

if not os.path.exists('www'):
    sys.exit('Can\'t find www directory')

os.system('cp -rf web/* www')

print(os.getcwd())

with zipfile.ZipFile('assets/items.zip', 'r') as zf:
    zf.extractall('www/img')
