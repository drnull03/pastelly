from flask import *
from secrets import *


#setting up the flask app
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')



@app.route('/setcookie')
def setcookie():
    
      # Initializing response object
    resp = make_response('Setting the cookie') 
    resp.set_cookie('GFG','ComputerScience Portal')
    return resp

@app.route('/getcookie')
def getcookie():
    GFG = request.cookies.get('GFG')
    return 'GFG is a '+ GFG

if __name__ == '__main__':
    app.run()