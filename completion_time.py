# def function sum_of_completion_times
# input: list job weight w and list job length l
# output: sum of completion times
def sum_of_completion_times(w, l):
    n = len(l)
    c = range(n)
    
    c[0] = l[0]
    for i in range(1,n):
        c[i] = c[i - 1] + l[i]
        
    total_time = 0
    
    for i in range(n):
        total_time += c[i] * w[i]
    return total_time
    
# def function result_of_method1
# run the greedy algorithm that schedules jobs 
# in decreasing order 
# of the difference (weight - length)
def result_of_method1(w, l):
    n = len(l)
    job2index = dict()
    
    for i in range(n):
        job2index[(w[i] - l[i], w[i], i)] = i
    
    tuple_list = list()
    for key in job2index:
        tuple_list.append(key)
    
    tuple_list.sort(reverse = True)
    
    tl = list()
    tw = list()
    for tuple_value in tuple_list:
        tw.append(tuple_value[1])
        tl.append(l[job2index[tuple_value]])
    
    return sum_of_completion_times(tw, tl)
    
# def function result_of_method2
# run the greedy algorithm that schedules jobs
# (optimally) in decreasing order of the ratio (weight/length)
def result_of_method2(w, l):
    
    n = len(l)
    job2index = dict()
    
    for i in range(n):
        w[i] = float(w[i])
    
    for i in range(n):
        job2index[(w[i] / l[i], i)] = i
    
    tuple_list = list()
    for ratio in job2index:
        tuple_list.append(ratio)
        
    tuple_list.sort(reverse = True)
    tl = list()
    tw = list()
    
    for ratio in tuple_list:
        tl.append(l[job2index[ratio]])
        tw.append(w[job2index[ratio]])
        
    return sum_of_completion_times(tw, tl)
    
# import data
filename = 'jobs.txt'
w = []
l = []
with open(filename,'r') as f:
    for line in f:
        s = line.split()
        w.append(float(s[0]))
        l.append(float(s[1]))
# call function result_of_method1 and result_of_method2
print result_of_method1(w, l) 
print result_of_method2(w, l) 

    
        
        
        
        
    
    
    
