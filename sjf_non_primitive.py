p = int(input())
pb = dict(enumerate(map(int,input().rstrip().split()),1))
pat = dict(enumerate(map(int,input().rstrip().split()),1))

keys = [k for k in pb.keys()]
values = [v for v in pb.values()]

execution = 0
arrived = []
wtime  = []
while sum(pb.values())>0:
    
    for k in pat.keys():
        if execution>=pat[k] and k not in arrived:
            arrived.append(k)
    temp = [pb[k] for k in arrived]
    temp = sorted(temp)
    for i in temp:
        for j in keys:
            if pb[j]==i and pb[j]>0:
                wtime.append(execution-pat[j])
                execution+=pb[j]
                pb[j]-=i
print(wtime)
tat = [w+v for w,v in zip(wtime,values)]
print("Process\tWaiting Time\t Turn Around Time")
for w,k,t in zip(wtime,keys,tat):
    print(f"P{k}\t{w}\t\t{t}")
            
        


        