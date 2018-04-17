from flask import render_template
from flask import Flask,request, url_for, redirect
import os,sys,inspect
import urllib
import time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
 
from tweet_collect import *

from main import * 

from sentiment import senti as sent
#from tweepy import tweet_collect as tweetcollect
app = Flask(__name__)
arr=[]

@app.route('/')
def landing():
    return render_template("landingpage.html")
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/sentimentform', methods=['GET', 'POST'])
def sentimentform():
    if request.method == 'POST':
        # do stuff when the form is submitted

          
        results = request.form
        #yo=request.form.getlist('t[0]')
        arr=sent.main(results)
        print (results)
        ''' img = io.BytesIO()  # create the buffer
	plt.savefig(img, format='png')  # save figure to the buffer
	img.seek(0)  # rewind your buffer
	plot_data = urllib.quote(base64.b64encode(img.read()).decode()) # base64 encode & URL-escape
	return render_template('plot.html', plot_url=plot_data)  '''     
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        #return redirect(url_for('aftersenti.html'))
	#time.sleep(10)
        return render_template('result.html',result =arr)
   	#print (yo)
    # show the form, it wasn't submitted
    return render_template('sentimentform.html')


'''@app.route('/result',methods = ['POST', 'GET'])
def res():
   if request.method == 'POST':
      return render_template("result.html",result = result)'''

@app.route('/topicmodelform', methods=['GET', 'POST'])
def topicmodelform():
    if request.method == 'POST':
        # do stuff when the form is submitted
        #results=request.form.getlist('t')
	results=request.form
	for key,val in results.iteritems():
		print key
		print val
       
        get_all_tweets(str(val))
	for root, dirs, files in os.walk("../dataset/Test/input/"):
    	 for file in files:
           if file.endswith(".txt"):
             print(os.path.join(root, file))
	     x = os.path.join(root, file)
        time.sleep( 5 )
        newresult=str(val)+".txt"
        arr=Test(newresult) 
	
        return render_template('result2.html',result =arr)       
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        #return redirect(url_for('aftersenti.html'))
        #return render_template('topresult.html')
   
    # show the form, it wasn't submitted
    return render_template('topicmodelform.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
