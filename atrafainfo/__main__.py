import os
import sys

from pprint import pformat

import anvil
from jinja2 import Environment, PackageLoader, select_autoescape

server_path = '/var/opt/minecraft/server'
data_path = os.path.join(server_path, 'world', 'region')

print('atrafainfo')


def eprint(s):
    print(s, file=sys.stderr)


def coord_to_chunk(x, z):
    return x >> 4, z >> 4


def chunk_to_region(x, z):
    return x >> 5, z >> 5


def coord_to_region(x, z):
    return chunk_to_region(*coord_to_chunk(x, z))


def dict_range(start, end):
    sx, sz = start
    ex, ez = end
    if sx > ex:
        sx, ex = ex, sx
    if sz > ez:
        sz, ez = ez, sz
    xd = ex - sx
    zd = ez - sz

    xr = range(xd + 1)
    if not xr:
        xr = [0]

    zr = range(zd + 1)
    if not zr:
        zr = [0]
    for x in xr:
        for z in zr:
            yield sx + x, sz + z


def region_fn(start, end):
    for d in dict_range(start, end):
        yield "r.{0}.{1}.mca".format(*d)


def lp(d):
    return d.value.split(':')[1]


def chuck_map(startx, endx, startz, endz):
    rd = dict()
    xd = endx - startx
    zd = endz - startz

    xr = range(xd + 1)
    if not xr:
        xr = [0]

    zr = range(zd + 1)
    if not zr:
        zr = [0]
    for rx in xr:
        for rz in zr:
            x = startx + rx
            z = startz + rz

            c = coord_to_chunk(x, z)
            r = chunk_to_region(*c)
            if r not in rd:
                rd[r] = dict()
            if c not in rd[r]:
                rd[r][c] = list()
            rd[r][c].append((x, z))

    return rd


jenv = Environment(
    loader=PackageLoader('atrafainfo'),
    autoescape=select_autoescape(['html'])
)
x = (258, 311)
z = (-50, 50)
#start_r = coord_to_region(*start)
#end_r = coord_to_region(*end)

cm = chuck_map(*x, *z)
eprint(pformat(cm))

data = dict(
    villagers=list()
)


for rk, rv in cm.items():
    fp = "r.{0}.{1}.mca".format(*rk)
    region_path = os.path.join(data_path, fp)
    eprint(region_path)
    if os.path.exists(region_path):
        r = anvil.Region.from_file(region_path)
        for ck, cv in rv.items():
            c = r.chunk_data(*ck)
            entities = c['Level']['Entities']
            if entities:
                for e in entities:
                    if e['id'].value == 'minecraft:villager':
                        v = dict(
                            profession=lp(e['VillagerData']['profession']),
                            level=e['VillagerData']['level'].value,
                            xp=e['Xp'].value
                        )
                        v['offers'] = list()
                        for o in e['Offers']['Recipes']:
                            v['offers'].append(dict(o))
                            #print("  {} {} -> {} {}".format(o['buy']['Count'], lp(o['buy']['id']).capitalize(), o['sell']['Count'], lp(o['sell']['id']).capitalize()))
                        data['villagers'].append(v)
eprint(pformat(data))
t = jenv.get_template('index.html')
print(t.render(data=data))
