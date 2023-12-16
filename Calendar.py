import sys
from urllib.parse import quote, unquote
from flask import Flask, jsonify, request, url_for
from markupsafe import escape
from datetime import datetime, date
import json

app = Flask(__name__)

## Class representing the Events in the calendar.

class Event:
    name = None
    timestamp = None
    duration = None
    participants = None

    def __init__(self, name, timestamp, duration, participants):
        self.name = name
        self.timestamp = timestamp
        self.duration = duration
        self.participants = participants

test_event = Event("Holidays", "12/23/2023", 1382400, ["Everyone"])
cal = {test_event.name : (test_event.timestamp, test_event.duration, test_event.participants)}

@app.route('/')
def main_menu():
    current_url = request.headers.get('X-Forwarded-Proto', 'http') + '://' + request.headers.get('X-Forwarded-Host', 'localhost')
    if current_url.endswith('/'):
        current_url = current_url[:-1]
    text = "<h2 style = 'text-align : center;'>This is the main page of our project, at the root of the other endpoints. Please choose amongst the following endpoints. </h2><h2 style = 'text-align : center;'>(Beware when changing the values of T1 and n in the url, keep %25252F for '/' and %252520 for ' ', only change the values)</h2> <br>"
    
    # Since the application to implement shouldn't have too many endpoints, we can add manually 
    # the default values for endpoints which require parameters.
    # Otherwise, we should create a list and get all the endpoints, access their properties with their rules,
    # and then do the necessary operations.

    text += "<p><a href='{}{}'>/{}</a></p><br>".format(current_url, url_for('calendar'), 'calendar')
    text += "<p><a href='{}{}'>/{}</a></p><br>".format(current_url, url_for('sorted_events'), 'sorted_events')
    text += "<p><a href='{}{}'>/{}</a></p><br>".format(current_url, url_for('sorted_events_by_person', p = 'Everyone'), 'sorted_events_by_person')
    text += "<p><a href='{}{}'>/{}</a></p><br>".format(current_url, url_for('add_event', n = quote('Day%201'), T1 = quote('01%2F01%2F1970'), t = 86400, p = 'Everyone'), 'add_event')
    text += "<p><a href='{}{}'>/{}</a></p><br>".format(current_url, url_for('remove_event', n = quote('Day%201')), 'remove_event')
    return text

@app.route('/viewCalendar', methods = ["GET"])
def calendar():
    return jsonify(cal)

@app.route('/viewCalendar/addEvent/<n>/<T1>/<t>/<p>', methods = ["GET", "POST"])
def add_event(n, T1, t, p):
    new_event = Event(unquote(unquote(n)), unquote(unquote(T1)), int(unquote(unquote(t))), [unquote(unquote(p))])
    cal[new_event.name] = (new_event.timestamp, new_event.duration, new_event.participants)
    return jsonify(cal)

@app.route('/viewCalendar/removeEvent/<n>', methods = ["GET", "POST"])
def remove_event(n):
    unquoted_n = unquote(unquote(n))
    if unquoted_n in cal:
        cal.pop(unquoted_n)
    return jsonify(cal)
    
@app.route('/viewCalendar/sortEvents', methods=["GET", "POST"])
def sorted_events():
    global cal
    sorted_cal = sorted(cal.items(), key = lambda entry : datetime.strptime(entry[1][0], "%m/%d/%Y"))
    cal.clear()
    for name, (timestamp, duration, participants) in sorted_cal:
        cal[name] = (str(timestamp), duration, participants)
    return json.dumps(cal, sort_keys = False)

@app.route('/viewCalendar/sortedEventsByPerson/<p>', methods=["GET"])
def sorted_events_by_person(p):

    global cal
    sorted_cal = sorted(cal.items(), key = lambda entry : datetime.strptime(entry[1][0], "%m/%d/%Y"))
    p_sorted_cal = {}
    for name, (timestamp, duration, participants) in sorted_cal:
        if p in participants:
            p_sorted_cal[name] = (str(timestamp), duration, participants)

    #person_events = [(name, timestamp, time, participants) for name, (timestamp, time, participants) in cal.items() if person in participants]

    #sorted_events = sorted(person_events, key = lambda event : event[1][0])
    #formatted_events = [{"name": event[0], "timestamp": event[1], "time": event[2], "participants": event[3]} for event in sorted_events]

    return json.dumps(p_sorted_cal, sort_keys = False)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "check_syntax":
            print("Build OK")
            exit(0)
        else:
            print("Passed argument not supported ! Supported arguments : check_syntax")
            exit(1)
    app.run(debug = True)