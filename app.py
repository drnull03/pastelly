from flask import *
from secrets import *


#setting up the flask app
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')




if __name__ == '__main__':
    app.run()