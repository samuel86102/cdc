change = [
            {'key':'C','type': '', 'indices': []},
            {'key':'D','type': '#', 'indices': [3,7]},
            {'key':'E','type': '#', 'indices': [2,3,6,7]},
            {'key':'F','type': 'b', 'indices': [4]},
            {'key':'G','type': '#', 'indices': [7]},
            {'key':'A','type': '#', 'indices': [3,6,7]},
            {'key':'B','type': '#', 'indices': [2,3,5,6,7]}
        ]


def get_scale(key):
    base_scale = ['C','D','E','F','G','A','B']
    start_index = base_scale.index(key)
    scale = []
    i = start_index
    for e in base_scale:
        scale.append(base_scale[i])
        i += 1
        if i > 6:
            i = 0
    change_ = change[start_index]
    for i in change_['indices']:
        scale[i-1] += change_['type']
    return scale


#scale = get_scale(key='C')


'''
with open('input') as f:
    lines = f.readlines()
    for line in lines:
        new_line = line
        for i in range(len(scale)):
            new_line = new_line.replace(str(i+1),scale[i])
        print(new_line)
'''
