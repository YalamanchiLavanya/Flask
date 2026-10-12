from flask import Flask,redirect,render_template,url_for,request
#create a flask application instance
app=Flask(__name__)
@app.route('/')
def home():
    #return f'Flask Server is Running'
    return render_template('index.html')
#GET
#name=Lavanya,email=lavanya@codegna.com
@app.route('/getdata',methods=['GET'])
def getdata():
    name = request.args.get('name')
    email = request.args.get('email')
    return f'the name is {name} and email is {email}'

#POST
'''@app.route('/getdatafromPost',methods=['POST'])
def getDatafromPOST():
    data=request.get_json()
    name = data['name']
    email=data['email']
    return f'The name is {name},email is {email}'
'''
@app.route('/postData',methods=['POST'])
def postData():
    name=request.form['name']
    email=request.form['Email']
    password=request.form['Password']

    if name is None or len(name)<5:
        return render_template('index.html',
                               err="Invalid Name")

    if email is None:
        return render_template('index.html',
                               err="Invalid Email")

    if password is None or len(password)<4:
        return render_template('index.html',
                               err="Invalid Password")

    return render_template('index.html',
                           err="Successful")

if __name__=="__main__":
    app.run(host='0.0.0.0',
            port=5001,debug=True)
