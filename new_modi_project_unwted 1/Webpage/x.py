import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
 
from tweet_collect import *

from main import *  
if __name__ =="__main__":
        
	#get_all_tweets("@narendramodi")
        Test("@narendramodi.txt")
