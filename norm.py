import sys

def path_norm(path_o):
    # Handle absolute paths (beginning with '/') as a special case
    abs_path=False
    if (path_o[0] == '/'):
        abs_path=True
        # Remove initial slash (will add back in later)
        path_o = path_o[1:]
    path_n = []

    for el in path_o.split('/'):
        if (el == '..' and len(path_n)>0):
            # If there is a parent directory in the input path, remove it
            path_n.pop(-1)
        elif (el != '.' and el != '..'):
            # Never return normalized paths with '.' or '..'
            path_n.append(el)

    # If input was an absolute path, add the initial slash back in
    if (abs_path):
        path_n.insert(0,'')

    return '/'.join(path_n)

def main(argv):
    input = argv
    try:
        # Assert that there is an input (ie, the path to be normalized)
        if(len(argv)>2):
            raise RuntimeError("norm.py requires only one input")
        elif(len(argv)<2):
            raise RuntimeError("norm.py requires input path to normalize")
        path_o = argv[1]
        print path_norm(path_o)
        return 0
    except Exception, err:
        sys.stderr.write("ERROR: %s\n" % str(err))
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    
