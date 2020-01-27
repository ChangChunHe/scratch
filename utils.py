
import re
import numpy as np

def gene_eig(outfile):
    with open("OUTCAR","r") as f:
        lines = f.read()
    res = re.search(r'occupation\s\n(\s+\d+\s*-?\d+\.\d+\s*\d\.\d*\n){1,}',lines).group().split("\n")[1:]
    eig = []
    for r in res:
        eig.append([float(i) for i in r.split()])
    eig.pop()
    np.savetxt("eig"+str(),np.array(eig),fmt="%.5f")


if __name__ == '__main__':
    main()
