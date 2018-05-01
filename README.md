# final_project
user intrest analysis and lexicon based sentiment analysis

Sentiment Analysis and Topic Modelling Options are Provided in this project.

RUN the newmain.py in the terminal and open the link that appears.
FLASK is used to integrate the webpages. 


Training
first convert the tweets downloaaded into word-set(wid , word) and doc-set(catid,wordid,tweetid,weight)
now produce the liblinear file(each line consissts of the unique words in the tweet ) using the above 2;

Testing
we can use the same word set,but if we get a new unique word via co-occurence we add that to the word set.
but we must use a new document set as none of the words after prreprocessing the test data arent assigned to any category and he we must first categorise 
Each word in the docset is initially assigned catid-1,. Now we use the docset and word set to create the liblinear format.


 Creating the Liblinear format is necessary because the SVM accepts only the Liblinear format of the words.
