from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    """
    Return users and display with table format according to
    the GET parameter from the client
    """
    # Get GET params from request
    args = request.args

    """
    You should write code to fetch data from database
    based according to the GET parameter.

    e.g. name = foo as GET parameter
    You may generate
        SELECT * FROM user WHERE name='foo'
    then get the users from DB.
    the result should pass to the users variable below.

    Your code is HERE!!!!
    """

    # example of users
    users = [
        {
            'name': 'foo',
            'bday': '1990/1/1',
            'age': 123,
            'state': 'WA'
        },
        {
            'name': 'bar',
            'bday': '1990/11/11',
            'age': 10,
            'state': 'CA'
        }
    ]
    return render_template("index.html", users=users)

if __name__ == '__main__':
    # You should change the port number.
    app.run(host='0.0.0.0', port=8080, debug=True)
