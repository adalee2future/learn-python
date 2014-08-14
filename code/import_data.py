res=[]
with open(filename,'r') as f:
    for line in f:
        res.append(int(line))