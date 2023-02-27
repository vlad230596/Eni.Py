import json
import numpy as np

class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NumpyArrayEncoder, self).default(obj)

def readJson(filename):
    f = open(filename)
    data = json.load(f)
    f.close()
    return data

def writeJson(filename, obj):
    f = open(filename, "w")
    f.write(json.dumps(obj, cls=NumpyArrayEncoder, indent=4))
    f.close()