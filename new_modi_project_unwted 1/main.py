from nlp import preprocess as preproc
  # for no weight
from worddoc import wdfw as w   # for weight
from SVM import SVMProcess2 as svm
from sentiment import senti as sent
import os,sys,inspect
import glob
from collections import Counter

def Train():
    
    print("EnteredTrain")
    preprocessed = [] 
    wordcount = 0
    categoryId =0
    files = ['./dataset/input/sports.txt','./dataset/input/finance.txt','./dataset/input/politics.txt','./dataset/input/technology.txt','./dataset/input/entertainment.txt']
    #string =[ "Hello this is it;","Hi How are you","This is Congratulations:"]
    
    for filename in files:
      categoryId += 1
      with open(filename) as f:
           tweets = [x.strip() for x in f] 
           preprocessed = preproc.tweet_mains(tweets)
           wordcount = w.generatewordset(preprocessed,categoryId)
           svm.create_trainfile(1,str()) 
    
    '''for pre in preprocessed:
        print pre'''

    print("Leaving Train")


def Test(inp):
    print("Entered Test")
    wordcount = 0
    #inp = raw_input("Enter the name of the test file :  ")   # test
    #inp = raw_input("Enter the name of the test file (filename.txt) :  ")
    #path = ('./dataset/Test/input/raghuram.txt')
    import os
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "/dataset/Test/input/"+str(inp)
    #abs_file_path = os.path.join(script_dir, rel_path)
    #abs_file_path = os.path.abspath(os.path.dirname(__file__))
  
    
 
    path = os.getcwd()
    print path
    abs_file_path = str(path)+str(rel_path)
    #parentdir = os.path.dirname(path)
    #os.chdir(parentdir)
    #path = os.getcwd()
    print "\n\n\npath="
    print abs_file_path 
    print "\n\n\n\n"
    #paths = os.path.abspath('dataset/Test/input/'+str(inp))
    paths = abs_file_path
   
    #path = ('./dataset/Test/input/'+inp)
    #f = open(paths,'r')
    arra=[]
    with open(paths,'r+') as f:
           tweets = [x.strip() for x in f] 
           preprocessed = preproc.tweet_mains(tweets)
           wordcount = w.generatetestset(preprocessed,str(inp))
           svm.create_trainfile(2,str(inp))
           arra=svm.testSVM(str(inp))
    print("Leaving Test")
    return arra


             
 
       

'''if __name__=='__main__':
    
    inpu = input("1.User's Interest \t2.Sentiment")
    if(inpu ==1):
       case = input("1.Train\t 2.Test")

       if(case==1):

           Train()
       else:

           Test()
    else:
      #sent.main()
      pass
'''
