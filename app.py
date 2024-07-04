
from flask import Flask,request,jsonify,session
import mysql.connector
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
import os
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
app=Flask(__name__)
CORS(app,supports_credentials=True)
con = mysql.connector.connect(host=DATABASE_HOST,
port=DATABASE_PORT,
database=DATABASE_NAME ,
user=DATABASE_USER,
password=DATABASE_PASSWORD )

cursor = con.cursor()
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route('/',methods=['GET'])
def index():
    return "hello"

@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute("SELECT username,password FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    if result :
        
        current_time = datetime.now()
        time_stamp = current_time.timestamp()
        date_time = datetime.fromtimestamp(time_stamp)
        str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
        cursor.execute("insert into timestamp(username,date_time) values(%s,%s)",(username,str_date_time))
        con.commit()
        return {'message': 'Login successful'}
    else:
        return {'message': 'Invalid Username or Password'}
@app.route('/question_answer', methods=['GET', 'POST'])
def answer():
    if request.method == 'POST':
        selected_option = request.form['Question']
        cur= con.cursor()
        #query="SELECT code FROM code WHERE Question_number = %s"
        cur.execute("SELECT code FROM code WHERE Question_number = %s",(selected_option,))
        code = cur.fetchone()
        if code:
           # return f'{ code }'
           return jsonify(code)

    #cursor.execute("select * from code where = %s", (Question_name))
@app.route("/signup",methods=["POST"])
@cross_origin
def signup():
    if request.method == 'POST':
        first_name = request.form.get("First Name")
        last_name = request.form["Last name"]
        username= request.form["username"]
        email = request.form["Email"]
        password=request.form["Password"]
        print(first_name)
        cur= con.cursor()
        try:
            cur.execute("insert into users(First_name,Last_name,Username,Email,Password)values(%s,%s,%s,%s,%s);",(first_name,last_name,username,email,password))
            con.commit()
        except mysql.connector.IntegrityError as err:
            if 'users.Email_UNIQUE' in str(err):
                print('Email already exists')
                return  {'message':'Email already exists'}
            elif 'users.Username_UNIQUE' in str(err):
                print('Username already exists')
                return  {'message':'Username already exists'}

    return {"message":"registered"}

if __name__ == '__main__':
    app.run(debug=True)