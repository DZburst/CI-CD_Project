import sys
from urllib.parse import quote, unquote
from flask import Flask, jsonify, request
from markupsafe import escape
# import time

app = Flask(__name__)

cal = {"Holidays" : ("23/12/2023", "1 382 400", "Everyone")}

@app.route('/')
def main_menu():
    return "This is the main page of our project, at the root of the other endpoints. Please choose amongst the following endpoints : \n"

@app.route('/viewCalendar', methods = ["GET", "POST"])
def calendar():
    return jsonify(cal)

@app.route('/viewCalendar/addEvent/<T1>/<t>/<p>/<n>', methods = ["GET", "POST"])
def add_event(T1, t, p, n):
    
    cal[n.strip('\"')] = (quote(unquote((T1))).strip('\"'), t.strip('\"'), p.strip('\"'))
    return jsonify(cal)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build OK")
            exit(0)
        else:
            print("Passed argument not supported ! Supported arguments : check_syntax")
            exit(1)
    app.run(debug = True)