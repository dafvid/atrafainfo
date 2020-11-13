import os
import sys

from atrafadata import export

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

print(export(server_path, as_json=as_json))



