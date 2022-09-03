def group_by_owners(files):
    inv_map = {}
    for k, v in files.items():
        inv_map[v] = inv_map.get(v, []) + [k]
    return inv_map

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))