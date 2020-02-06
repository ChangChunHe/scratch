import numpy as np

with open("dump.gap","r") as f:
    lines = f.read()

lines = lines.split("ITEM: TIMESTEP")
pos = []
for idx in range(1,len(lines)):
    step_str = lines[idx].split("ITEM")[-1].split("\n")
    step_pos = []
    for _idx in range(1,len(step_str)-1):
        step_pos.append([i for i in step_str[_idx].split()])
    pos.append(step_pos)

for idx,_pos in enumerate(pos):
    with open("POSCAR"+str(idx),"w") as f:
        f.writelines("STEP"+str(idx)+"\n")
        f.writelines("1\n")
        f.writelines("30 0 0 \n0 30 0 \n0 0 130\n")
        f.writelines("C\n1600\nCart\n")
        for p in _pos:
            p = p[1:]
            f.writelines(" ".join(p)+"\n")
