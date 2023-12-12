import sys
from urllib.parse import quote, unquote
from flask import Flask, jsonify, request, url_for
from markupsafe import escape
from datetime import datetime
from operator import itemgetter

app = Flask(__name__)

cal = {"Holidays" : ("23/12/2023", "1 382 400", "Everyone")}

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
    text += "<p><a href='{}{}'>/{}</a></p><br>".format(current_url, url_for('add_event', T1 = quote('01%2F01%2F1970'), t = '86400', p = 'Everyone', n = quote('Day%201')), 'add_event')
    text += "<p><a href='{}{}'>/{}</a></p><br>".format(current_url, url_for('remove_event', n = 'Day 1'), 'remove_event')
   
    

    text += "<p><a href='{}{}'>/{}</a></p><br>".format(current_url, url_for('all_events'), 'all_events')
    
    return text

@app.route('/viewCalendar', methods = ["GET"])
def calendar():
    return jsonify(cal)

@app.route('/viewCalendar/addEvent/<T1>/<t>/<p>/<n>', methods = ["GET", "POST"])
def add_event(T1, t, p, n):
    cal[unquote(unquote(n))] = (unquote(unquote(T1)), t, p)
    return jsonify(cal)

@app.route('/viewCalendar/removeEvent/<n>', methods = ["GET", "POST"])
def remove_event(n):
    cal.pop(n)
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
    

@app.route('/viewCalendar/allEvents', methods=["GET"])
def all_events():
    sorted_events = sorted(cal.items(), key=lambda x: datetime.strptime(x[1][0], "%d/%m/%Y"))
    # Triez les événements par date en utilisant la bibliothèque datetime
    
    formatted_events = [{"name": event[0], "timestamp": event[1][0], "time": event[1][1], "participants": event[1][2]} for event in sorted_events]
    # Formatage des événements pour une sortie JSON
    
    return jsonify(formatted_events)
