from __future__ import with_statement
import os
import yaml
import re

def find_fullpath(item):
    if not os.path.isfile(item):
        temp = str(item).split(os.sep)
        temp = filter(lambda x: x not in ['.', '..'], temp)
        dir_ = None
        file_ = temp[-1]
        if len(temp) > 1:
            dir_ = temp[-2]
        root_ = os.sep.join(os.getcwd().split(os.sep)[:-1])
        for root, dirs, files in os.walk(root_):
            if dir_ and os.path.split(root)[-1] != dir_:
                continue
            if file_ in files:
                return os.path.join(root, file_)
        raise IOError(item + ' not found')
    return item

def conda_to_vars(iterable):
    data = []
    for item in iterable:
        if item.__class__.__name__ == 'AnsibleUnicode':
            item = find_fullpath(item)
            with open(item, 'r') as f:
                item = yaml.load(f)

        datum = {}
        datum['__name'] = item['name']
        if item.has_key('python'):
            datum['__python'] = item['python']
        pkgs = filter(lambda x: not isinstance(x, dict), item['dependencies'])
        datum['__pkgs'] = ' '.join(pkgs)
        datum['__update_pkgs'] = ' '.join([re.split('[=><]', x)[0] for x in pkgs])

        pip = filter(lambda x: isinstance(x, dict), item['dependencies'])
        if pip != []:
            datum['__pip_pkgs'] = ' '.join(pip[0]['pip'])
            if len( filter(lambda x: re.search('^pip$|^pip[^a-z-0-9]', x, re.I), pkgs ) ) == 0:
                datum['__pkgs'] += ' pip'

        data.append(datum)
    return data

class FilterModule(object):
     def filters(self):
         return {'conda_to_vars': conda_to_vars}
