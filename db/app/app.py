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

    args = request.args
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
    app.run(debug=True)
