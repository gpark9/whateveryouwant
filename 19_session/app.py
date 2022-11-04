from flask import Flask
from flask import session
from flask import render_template
from flask import request

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_9#y2L"F4Q8z\n\xec]/'

temp_username = "brianna"
temp_password = "bt"

@app.route('/')
def index():
    return render_template( 'login.html' )
    '''
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'
    '''

@app.route('/auth', methods=['GET', 'POST'])
def authenticate():
    #if request.args['username'] == temp_username and request.args['password'] == temp_password :
    #    return render_template('signup.html', user=request.form['username'], method = request.method)

    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return
        '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
        '''



@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run()
