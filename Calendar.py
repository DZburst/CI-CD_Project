from flask import Flask, jsonify
from markupsafe import escape
import time

app = Flask(__name__)

calendar = {"Holidays" : ("23/12/20023", "1 382 400", "Everyone")}

@app.route('/')
def main_menu():
    return "This is the main page of our project, at the root of the other endpoints. Please choose amongst the following endpoints : \n"

@app.route('/viewCalendar', methods = ["GET"])
def calendar():
    return jsonify(calendar)

@app.route('/viewCalendar/addEvent', methods = ["POST"])
def add_event(T1, t, p, n):
    calendar[n] = (f"{T1}", f"{p}", f"{n}")
    return "Event successfully added to the calendar."