import time
# INPUTS TIME - time_quantum , number of processes , process dictionary
tq = int(input())
p = int(input())
pb = dict(enumerate(map(int,input().rstrip().split()),1))
# Extracting out the keys
keys = [k for k in pb.keys()]
values = [v for v in pb.values()]
# Maintaing track of round_robin execution
log = []
start = time.time()

# Function to output subsets from the log list corresponding to the execution of  
#  a particular process.
def subsets(log,k):
    # -------------
    # Attributes
    # log = list having info of execution of processes
    # k = list of process-id's
    # -------------
    temp = []
    for each in k:
        u = []
        for x,e in enumerate(log):
            if e == each:
                u.append(x)
        t_index = max(u)
        temp.append(log[:t_index+1])
    return temp

# Function for outputting the waiting time of the processes during the execution 
def waiting_time(log):
    # ----------------
    # Attributes
    #  log = list of subsets of processes execution  
    # ----------------
    wtime = []
    for x ,each in enumerate(log,1):
            wtime_ = 0
            for e in each:
                if e==x:
                    pass
                else:
                    wtime_+=tq
            wtime.append(wtime_)
    return wtime

# Function to perform the execution of the processes . 
def execute():
    while sum(pb.values())>0:
            for k in keys:
                if pb[k]>0:
                    log.append(k)
                pb[k] = pb[k]-tq if pb[k]>tq else pb[k]-pb[k] if pb[k]>0  else 0
            
            
# Funcion to output the analysis of the process execution
def analysis():
    print("Process\tWaiting_Time\tTurn Around Time")
    for k,w,t in zip(keys,wtime,turn_around_time):
        print(f"P{k}\t{w}\t\t{t}")

# Function for calculating the average of wtime and TAT
def average():
    w_avg = sum(wtime)/len(wtime)
    t_avg = sum(turn_around_time)/len(turn_around_time)
    print(f"Average Waiting Time : {round(w_avg,2)} \n\
Average Turn Around Time :{round(t_avg,2)}")

execute()
new_log = subsets(log,keys)
wtime = waiting_time(new_log)
turn_around_time = [w+v for w,v in zip(wtime,values)]
analysis()
average()

end = time.time()
print("Time :",round((end-start)*1000,2),"secs")

