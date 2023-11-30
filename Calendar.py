import sys
from flask import Flask, jsonify
from markupsafe import escape
# import time

app = Flask(__name__)

cal = {"Holidays" : ("23/12/20023", "1 382 400", "Everyone")}

@app.route('/')
def main_menu():
    return "This is the main page of our project, at the root of the other endpoints. Please choose amongst the following endpoints : \n"

@app.route('/viewCalendar', methods = ["GET"])
def calendar():
    return jsonify(cal)

# Not working, need to check out how to use several parameters in the route.
@app.route('/viewCalendar/addEvent/<(T1, t, p, n)>', methods = ["POST"])
def add_event(T1, t, p, n):
    calendar[n] = (f"{T1}", f"{t}", f"{p}")
    return "Event successfully added to the calendar."


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build OK")
            exit(0)
        else:
            print("Passed argument not supported ! Supported arguments : check_syntax")
            exit(1)
    app.run(debug = True)