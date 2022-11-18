from glob import escape
from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
 

#conn=ibm_db.connect("DATABASE=bludb; HOSTNAME=824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30119;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=prg16100;PWD=3Tdg3EFQTg7f08bD",' ',' ')
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/login',methods = ['POST'])
def getUser():
    if request.method == 'POST':
        user = request.form['uname']
        password = request.form['upwd']
        sql = "SELECT * FROM data where username = ?"
        stmt = ibm_db.prepare(conn, sql)
        email = user
        # Explicitly bind parameters
        ibm_db.bind_param(stmt, 1,user)
        ibm_db.execute(stmt)
        dictionary = ibm_db.fetch_assoc(stmt)
        pwd = dictionary["PASSWORD"]
        if password != pwd:
            return render_template('error.html')

        return  render_template('home.html')
    
@app.route('/signup',methods = ['POST'])
def storedUser():
    if request.method == 'POST':
        username = request.form['username']
        mail = request.form['mail']
        npwd = request.form['npwd']
        cpwd = request.form['cpwd']

        res = username + mail + npwd +cpwd

        if npwd != cpwd:
            return render_template('index.html')

        sql = "INSERT INTO data (UserName,Email,password,confirmpassword) VALUES(?,?,?,?);"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, username)
        ibm_db.bind_param(stmt, 2, mail)
        ibm_db.bind_param(stmt, 3, npwd)
        ibm_db.bind_param(stmt, 4, cpwd)
        ibm_db.execute(stmt)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)