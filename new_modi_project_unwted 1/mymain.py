from nlp import preprocess as preproc
import os
import glob
from gensim.models import Word2Vec

def Train():
    
	print("EnteredTrain")
	preprocessed = [] 
	wordcount = 0
	categoryId =0
    
	#string =[ "Hello this is it;","Hi How are you","This is Congratulations:"]
	path = ('./dataset/input/')
	#string =[ "Hello this is it;","Hi How are you","This is Congratulations:"]
    
	for filename in glob.glob(os.path.join(path, '*.txt')):
                print categoryId
                categoryId+=1
		with open(filename,'r+') as f:
			tweets = [x.strip() for x in f] 
			preprocessed.append(preproc.tweet_mains(tweets))
	for tweet in preprocessed:
 		for word in tweet:
			print word
                print '\n'
	'''m = Word2Vec(preprocessed)
	print m
	print(m.most_similar('stock'))'''
   
    
   
if __name__=='__main__':
  
    Train()
