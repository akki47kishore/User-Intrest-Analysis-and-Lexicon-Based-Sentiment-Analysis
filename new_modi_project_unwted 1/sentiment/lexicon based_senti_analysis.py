import os
import collections
from neg_intensifiers import negators_process as neg_process

#word_dict = {}
word_dict = collections.defaultdict(lambda : 0)   # if word not present return 0
negator = collections.defaultdict(lambda : 0)

neg = 0                 # initialise negator to 0

def convert_to_dict():
	word_file = open('common_dict.txt','r')    # word dictionary single word dictionary
	for entry in word_file:
		word_set = entry.split()
		#word_dict['word'] = int(word_set[0])
		#word_dict['polarity'] = int(word_set[1])
		print(word_set[0]+str("   ")+str(word_set[1]))
		print("\n")
		'''if(word_dict[word_set[0]] == 0):
			word_dict.update({word_set[0] : int(word_set[1])})   # dictionary
			
	for entry in word_set:
		print(str(entry)+str("   ")+str(word_set[i]))   '''


'''def get_sentiment(search_word):
	senti = 0
	for word_val in word_dict:
		if(word_val['word'] = search_word):       # if search word
			senti_pol = word_val['polarity']
			break
	return senti_pol '''
	

def get_sentiment_polarity(search_word):        # using word dictionary
	return word_dict[search_word]	
	
	
#def intensification(search_word):                 # under construction





def sentiment_main(sentence) :
	val = sentence.split()              				# to split the sentence into words
	arr = []
	neg_flag = 0
	intesifier_flag = 0
	curr_pol = 0
	prev_pol = 0
	for v in val:
		arr.append(v.lower())           				# lower to convert to lowercase
		
	for wd in arr:
		prev_pol = curr_pol
		curr_pol = get_sentiment_polarity(wd)
		
	# intensification		
		prev_intensifier = intensifier_flag
		if(intensifier_flag != 0):                       # the previous word is an intensifier
			if(curr_pol != 0):							 # if current word is a sentimnet word
				curr_pol = curr_pol*((100 + intensifier_flag) / 100)
			else:
				#intensifier_flag = is_intensifier(wd)        # test
				if(intensifier_flag != 0): 			 # intensifier, previous and current words are intensifiers
					prev_intensifier = prev_intensifier*((100 - intensifier_flag) / 100)
					intensifier_flag = prev_intensifier
					continue
			
	# negation	
		if(neg_flag == 1):             				 	# previous word was negator
			if(curr_pol != 0):           				# it is a sentiment word
				curr_pol = -1*curr_pol 					# reverse the polarity	
				neg_flag = 0
			
			
			
		curr_pol = curr_pol + prev_pol	
		neg_flag = neg_process.is_negator(wd)       				# is the word negator
		
		return curr_pol


if __name__ == '__main__':
	convert_to_dict()
















		
