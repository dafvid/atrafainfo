import os
import sys

from atrafadata import export

server_path = '/var/opt/minecraft/server'
x = (258, 311)
z = (-50, 50)


if not os.path.exists(server_path):
    sys.exit("Can't find minecraft data folder ({})".format(server_path))

print(export(server_path))



