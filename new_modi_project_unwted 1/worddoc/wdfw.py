import os
import subprocess

def generatewordset(preprocess,catid):
   
    print("Entered word set\n\n")
    #f = open("wordset.txt",'a+')
    wordset = []
    #wordCount = {} 
    #catid = 1
   
    tweetid = 0
    eachwordcount ={} 
    os.getcwd() 
    files1 = os.path.abspath('dataset/Trained/wordset.txt')
    #files2 = os.path.abspath('dataset/Trained/wordsetpluscount.txt')
    files3 = os.path.abspath('dataset/Trained/docset.txt')
    wf = open(files1,'a+')
    df = open(files3,'a+')
    #cf = open(files2,'a+') 
    col_num = 0
    
    delimiter = " "
    with open(files1,'r') as f:
        f.seek(0)                      #ensure you're at the start of the file..
        first_char = f.read(1)   #get the first character
        if not first_char:
           f.seek(0)   #first character is the empty string..
           maxwordcount = 0
        else:
           
            wordset.append(f.readline().split(delimiter)[col_num])
            line = (subprocess.check_output(['tail', '-1', files1]).split())
            maxwordcount = int(line[1])
            f.seek(0)
            wordset.append(f.readline().split(delimiter)[col_num])

    for tweet in preprocess:
           
           #[wordCount.__setitem__(w,1+wordCount.get(w,0)) for w in tweet]
           #print("wordCount=",wordCount)
           for word in tweet:
                  
           
                  if(word not in wordset):              # wordset is the set of preprocessed words
                    									#  if word not in wordset
                    maxwordcount +=1					# word count
                    wordset.append(word) 
                    wordId=wordset.index(word)          # to get the index of the word in the array word set
                    wf.write(str(word)+"\t"+str(wordId+1)+'\n')  
                   
                    eachwordcount[wordId] = 1           # if new word initialise the word count to 1
                  
                 
                  else:
  
                     wordId=wordset.index(word)       	# to retrive the index of the word in the wordset( array of words)
                     eachwordcount[wordId]+=1
                  #df. write(str(catid) + "\t" + str(tweetid)+ "\t" +str(wordId+1) + "\t" + str(1) + "\n") 
                     

    print("wordset\twordcount\n\n\n")
    '''with open(files2 ,'a+') as f:
       
                  for i in range (1,maxwordcount,1):
  
                     print(wordset[i],i, eachwordcount[i]) 
                     f.write(str(wordset[i])+"\t\t"+str(i)+"\t\t"+str(eachwordcount[i])+"\n")''' 


   
    for tweet in preprocess:
        tweetid+=1
        for word in tweet:
           wordId=wordset.index(word)
           count = eachwordcount[wordId]
           df. write(str(catid) + "\t" + str(tweetid)+ "\t" +str(wordId+1) + "\t" + str(count) + "\n") 





    
    print "\nword set generated:\n"
    return maxwordcount         

def generatetestset(testpreprocess,inp):


    #f = open("wordset.txt",'r+')
    wordset = []
    #wordCount = {} 
    #catid = 1
   
    tweetid = 0
    eachwordcount ={} 
    os.getcwd() 
    files1 = os.path.abspath('dataset/Trained/wordset.txt')
    files2 = os.path.abspath('dataset/Trained/wordsettestcount.txt')
    files3 = os.path.abspath('dataset/Test/docsets/'+inp)
    wf = open(files1,'a+')
    df = open(files3,'w')
    cf = open(files2,'a+') 
    col_num = 0
    catid = 0
    delimiter = " "
    with open(files1,'r') as f:
        f.seek(0)                      #ensure you're at the start of the file..
        first_char = f.read(1)   #get the first character
        if not first_char:
           f.seek(0)   #first character is the empty string..
           maxwordcount = initial =0
        else:
           
            wordset.append(f.readline().split(delimiter)[col_num])
            line = (subprocess.check_output(['tail', '-1', files1]).split())
            maxwordcount = int(line[1])
            initial = maxwordcount
            f.seek(0)
            wordset.append(f.readline().split(delimiter)[col_num])
    
        for tweet in testpreprocess:
           tweetid+=1
           #[wordCount.__setitem__(w,1+wordCount.get(w,0)) for w in tweet]
           #print("wordCount=",wordCount)
           for word in tweet:
                  
           
                  if(word not in wordset):              # wordset is the set of preprocessed words
                    									#  if word not in wordset
                    maxwordcount +=1					# word count
                    wordset.append(word) 
                    wordId=wordset.index(word)          # to get the index of the word in the array word set
                    wf.write(str(word)+"\t"+str(wordId+1)+'\n')  
                   
                    eachwordcount[wordId] = 1           # if new word initialise the word count to 1
                  
                 
                  else:
  
                     wordId=wordset.index(word)       	# to retrive the index of the word in the wordset( array of words)
                     eachwordcount[wordId]+=1
                  df. write(str(catid) + "\t" + str(tweetid)+ "\t" +str(wordId+1) + "\t" + str(1) + "\n") 
                     

    '''print("wordset\twordcount\n\n\n")
    print wordset[1]
    print maxwordcount
    print initial
    print wordset[initial+1]
    with open(files2 ,'a+') as f:
       
                  for i in range (initial,maxwordcount,1):
  
                     print(wordset[i],i, eachwordcount[i]) 
                     cf.write(str(wordset[i])+"\t\t"+str(i)+"\t\t"+str(eachwordcount[i])+"\n")'''         
    print "\nset generated:\n"
    return maxwordcount         

 
                      
