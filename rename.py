import json
import os
import shutil

from pprint import pprint


assets_path = os.path.join(
        os.path.dirname(
            os.path.realpath(__file__)), 'assets')
with open(os.path.join(assets_path, 'items.json')) as f:
    item_data = {"{type}-{meta}".format(**x): x['text_type'] for x in json.load(f)}
pprint(item_data)
os.makedirs('output', exist_ok=True)
for f in os.listdir('www/img'):
    print(f)
    fn = f.split('.')[0]
    print(fn)
    nfn = "{}-{}.png".format(item_data[fn], fn.split('-')[1])
    print(nfn)
    shutil.copy(os.path.join('www/img', f), os.path.join('output', nfn))