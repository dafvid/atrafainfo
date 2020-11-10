import os

from atrafadata import export

dir_path = os.path.dirname(os.path.realpath(__file__))

server_path = os.path.join(dir_path, 'test')


with open('web/index.html', 'w') as f:
    f.writelines(export(server_path, test=True))
