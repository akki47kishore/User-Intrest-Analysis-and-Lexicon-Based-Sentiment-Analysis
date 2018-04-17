import collections

neg_dict = collections.defaultdict(lambda : 0)

neg_dict = {"not":1, "no":1, "n't":1, "neither":1, "nor":1, "nothing":1, "never":1, "none":1, "lack":1, "lacked":1, "lacking":1, "lacks":1, "missing":1, "without":1, "absence":1, "devoid":1, "didn't":1}

def is_negator(word):
	flag = word in neg_dict
	if(flag == True):
		return neg_dict[word]
	else:
		return 0
		
