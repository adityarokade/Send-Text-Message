from flask import Flask, render_template, request,jsonify

# from werkzeug.utils import redirect
import pandas as pd
from Email_Msg import Email_msg
from Mobile_Msg import Message_mobile

app = Flask(__name__)
# @app.route('/', methods=['GET', 'POST']) # To render Homepage
# def home_page():
#     return ("<h2>hi everyone</h2>")


@app.route('/',methods=['GET','POST'])
def Email_massage():
    api_key="9f81fddf27be1aa3e73a0619392cbc0c"
    df=pd.read_csv("Sample.csv")
    n=len(df)
    
    for i in range(n):
        email=df['Email'][i]
        Message=df['Message'][i]
        mobile=df['Phone'][i]
        Country=df['Country'][i]
        subject=f"{Country}Python Task - Screen Magic"
        body=f"Meaasage:- {Message}"
        to=f"{email}"
        E=Email_msg(subject,body,to)
        E.email_msg()
        M=Message_mobile(mobile,body,api_key)
        M.message_mobile()

       
  
    return ("<h1>Message Sended</h1>")







if __name__ == '__main__':
    app.run()