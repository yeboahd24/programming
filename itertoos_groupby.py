from itertools import groupby

'''Normal grouping using dictionary.'''

s = 'AAAABBBCCDAABBB'

s_dict = {}

for i in s:
	if i not in s_dict.keys():
		s_dict[i] = [i]
	s_dict[i].append(i)
# print(s_dict)     # Not this can not be used for larger data



# The best way

data = groupby(sorted(s)) # sorting s to archive the final results  
dic = {}

for k, v in data:
	dic[k] = list(v) # without the sorted function this will not work well
print(dic)

