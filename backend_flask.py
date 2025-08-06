from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Connect to DB
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Query
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        return f"✅ Welcome, {username}!"
    else:
        return "❌ Invalid username or password."

if __name__ == '__main__':
    app.run(debug=True)
