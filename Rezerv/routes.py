from flask import request,render_template
import openai

from Rezerv.model import *
from Rezerv import app

token = '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'
openai.api_key = token

@app.route('/',methods =['GET','POST'])
def index():  
      return render_template("index.html")

@app.route('/chatgpt',methods =['GET','POST'])
def chatgpt():  
      if request.method == "POST":
            question = request.form['question']
            if not question=="":
                  allowed_tags = ['h1']
                  return render_template("chatgpt.html",answer = openai_davinci(question))
            return render_template("chatgpt.html")
      return render_template("chatgpt.html")

@app.route('/test',methods =['GET','POST'])
def test():  
      status = Statuses.query.first()
      return status.NAME

@app.route('/login',methods =['GET','POST'])
def login():  
     return render_template("login.html")

            

def openai_davinci(question):
    print(question)
    openai.api_key = token
    response = openai.Completion.create(engine="text-davinci-003", prompt=question, max_tokens=256)
    return response.choices[0].text