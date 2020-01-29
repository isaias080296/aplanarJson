import pandas as pd

import json

from pandas.io.json import json_normalize

with open('C:\\Users\\AFIRMA - ISAIAS\\Desktop\\Codigo\\prueba.json') as myfile:
    data=myfile.read()

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

flat = flatten_json(data)
json_normalize(flat)

#data_string = json.dumps(data)

#df = json_normalize(data_string, ["1.0",])

print(flat)


with open('data.json', 'w') as file:
    json.dump(flat, file)
