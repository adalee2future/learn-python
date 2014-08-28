def job_scheduling(jobs, num):
    # jobs: a list of jobs with load
    # num: number of machines
    # output:  Iterate through the jobs j=1,2,3,…,n one-by-one. When considering job j,
    #   assign it to the machine that currently has the smallest load
    #   (breaking ties arbitrarily)
    machines = []
    for i in range(num):
        machines.append(0)
    
    for job in jobs:
        index = machines.index(min(machines))
        machines[index] += job
    
    return max(machines)
    
    
# start here
res1 = 1
res2 = 1
from random import shuffle
from random import randint
jobs = []
for i in range(10000):
   jobs.append(randint(1,1000000))

#for i in range(90):
#    jobs.append(1)

#jobs.append(10)


jobs.sort(reverse = True)
reversed_sorted_jobs = jobs[:]
num = 100
current_best = sum(jobs)
current_worst = 0

for i in range(1000000):
    shuffle(jobs)
    load = job_scheduling(jobs, num)
    
    if load < current_best:
        current_best = load
    
    if load > current_worst:
        current_worst = load
        
reversed_sorted_res = job_scheduling(reversed_sorted_jobs, num)

print current_best, current_worst, reversed_sorted_res
print float(current_worst) / current_best
print float(reversed_sorted_res) / current_best

if float(current_worst) / current_best > res1:
    res1 = float(current_worst) / current_best

if float(reversed_sorted_res) / current_best > res2:
    res2 = float(reversed_sorted_res) / current_best





    

        