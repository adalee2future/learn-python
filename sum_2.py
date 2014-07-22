# input: sorted and distinct array OC, 
#dictionary of OC, with key in OC, length of OC next
#output distinct sum between -10000 and 10000 count
def sum_2(OC, dict, n):
	count = 0;
	sums = range(-10000, 10001);
	i_s = range(0, n);
	for sum in sums:
		print sum;
		print count;
		for i in i_s:
			x = OC[i];
			find_y = dict.has_key(sum - x);
			if find_y:
				count += 1;
				break;
	return count;

# import data	
filename = 'E:\data\sum_2.txt';
res=[]
with open(filename,'r') as f:
    for line in f:
        res.append(int(line))

# get distinct values		
res_set = set(res);
# back to list
res_list = list(res_set);
# get length of list
n = len(res_list);
#construct dictionary
dict = {};
i_s = range(0, n);
for i in i_s:
	dict[res_list[i]] = i;
# call function sum_2		
count = sum_2(res_list, dict, n);		