import os
import sys

from atrafadata import export

if len(sys.argv) != 2:
    sys.exit("Pass path to minecraft data as argument")
server_path = sys.argv[1]
x = (258, 311)
z = (-50, 50)


if not os.path.exists(server_path):
    sys.exit("Can't find minecraft data folder ({})".format(server_path))

print(export(server_path))



