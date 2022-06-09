from flask import Flask, redirect,render_template,request
import os
from data import contacts,getAllData,updateData
import pandas as pd

app=Flask(__name__)

assetsFolder=os.path.join('static','assets')

app.config['UPLOAD_FOLDER']=assetsFolder

app.secret_key = "superKey"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home",methods=['POST','GET'])
def home():
    _temp1=getAllData()

    if request.method == 'POST':
        if(request.form['search_input']==''):
            _temp1=getAllData()
        else:
            if(request.form['search_input'].isdigit()):
                _temp1=_temp1[request.form['search_input'] == _temp1['Phone']]
            else:
                _temp1=_temp1[request.form['search_input'] == _temp1['Name']]



    pic1=os.path.join(app.config["UPLOAD_FOLDER"],'profile_avatar.png')
    pic2=os.path.join(app.config["UPLOAD_FOLDER"],'share_icon.png')
    pic3=os.path.join(app.config["UPLOAD_FOLDER"],'search_icon.png')
    return render_template("home.html",profilePic=pic1,sharePic=pic2,searchIcon=pic3,contacts=_temp1)

@app.route("/add",methods=['POST','GET'])
def addContacts():
    if request.method == 'POST':
        # print(request.form['name_input'])
        _temp2=getAllData()
        _data = {
        "Name": [request.form['name_input']],
        "Phone": [request.form['phone_input']]
        }
        updateData(_data)
        
        return redirect('home')
    else:
        return render_template("addContacts.html")


if(__name__=="__main__"):
    app.run(debug=True,host='0.0.0.0',port=3000)