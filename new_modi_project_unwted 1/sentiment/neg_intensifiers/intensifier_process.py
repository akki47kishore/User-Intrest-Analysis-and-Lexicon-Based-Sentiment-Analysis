import collections

intensifier_dict = collections.defaultdict(lambda : 0)

intensifier_dict = {"slightly" : -50, "somewhat" : -30, "pretty" : -10, "really" : 15, "very" : 25, "extraordinarily" : 50, "most" : 100}

def get_intensification(word):
	flag = word in intensifier_dict
	if(flag == True):
		return intensifier_dict[word]
	else:
		return 0
	
	
	
	
	
	
	
	
