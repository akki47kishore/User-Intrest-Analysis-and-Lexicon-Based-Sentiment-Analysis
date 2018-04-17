from flask import render_template
from flask import Flask,request, url_for, redirect
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from sentiment import senti as sent

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sentimentform', methods=['GET', 'POST'])
def sentimentform():
    if request.method == 'POST':
        # do stuff when the form is submitted

          
        result = request.form
        sent.main(result)
        print (result)
               
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        #return redirect(url_for('aftersenti.html'))
        return render_template('sentiment.html')
   
    # show the form, it wasn't submitted
    return render_template('sentimentform.html')

@app.route('/topicmodelform', methods=['GET', 'POST'])
def topicmodelform():
    if request.method == 'POST':
        # do stuff when the form is submitted

          
               
        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        #return redirect(url_for('aftersenti.html'))
        return render_template('index.html')
   
    # show the form, it wasn't submitted
    return render_template('topicmodelform.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
