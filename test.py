from atrafadata import export

server_path = 'test'


with open('web/index.html', 'w') as f:
    f.writelines(export(server_path, test=True))
