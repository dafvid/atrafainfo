import math
import os

import anvil

from atrafadata import chunk_map, box

cm = chunk_map(*box(410, -110, 1000))

for rk, rv in cm.items():
    fp = "r.{0}.{1}.mca".format(*rk)
    region_path = os.path.join('test', 'world', 'region', fp)
    if os.path.exists(region_path):
        print("Parsing {}".format(region_path))
        r = anvil.Region.from_file(region_path)
        for ck, cv in rv.items():
            c = r.chunk_data(*ck)
            entities = c['Level']['Entities']
            if entities:
                for e in entities:
                    if e['id'].value == 'minecraft:sheep':
                        print(e['Pos'])
