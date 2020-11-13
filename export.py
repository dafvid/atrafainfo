import os
import sys

from atrafadata import export, eprint

args = sys.argv

as_json = False
if 'json' in args:
    args.pop(args.index('json'))
    as_json = True


if len(args) != 2:
    sys.exit("Pass path to minecraft data as argument")
server_path = sys.argv[1]

if not os.path.exists(server_path):
    sys.exit("Can't find minecraft data folder ({})".format(server_path))

with open('www/index.html', 'w') as f:
    f.writelines(export(server_path, test=True))
    eprint("Created new www/index.html")

with open('www/data.json', 'w') as f:
    f.writelines(export(server_path, test=False, as_json=True))
    eprint("Created new www/data.json")



