import os

from atrafadata import export, eprint

dir_path = os.path.dirname(os.path.realpath(__file__))

server_path = os.path.join(dir_path, 'test')


with open('web/index.html', 'w') as f:
    f.writelines(export(server_path, test=True))
    eprint("Created new web/index.html")

with open('web/data.json', 'w') as f:
    f.writelines(export(server_path, test=False, as_json=True))
    eprint("Created new web/data.json")
