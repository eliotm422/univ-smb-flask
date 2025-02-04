# save this as app.py
from flask import Flask, request, url_for, redirect, render_template, flash, jsonify, session

app = Flask(__name__)
app.secret_key = 'username:password'

@app.route("/")
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'Napoleon' and password == 'Bonapart':
            session['key']="Napoleon"
            return render_template('home.html', login=username)
            
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect, rentrez Napoleon / Bonapart')
            return render_template('login.html')
            

@app.route('/home_form', methods=['GET', 'POST'])
def home_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('home.html')

@app.route('/alias_JSON', methods=['GET', 'POST'])
def alias_JSON():
    data1 = { 
    '1' : {'ip1': '10.0.0.2', 'port1' : "22", 'server1': 'Webserver1'},  
    '2' : {'ip2': '10.0.0.3', 'port2' : "22", 'server2': 'Webserver1'},  
    }
    return jsonify(data1)

@app.route('/alias_form', methods=['GET', 'POST'])
def alias_form():  
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('alias'))

    # show the form, it wasn't submitted
    return render_template('alias.html')

#@app.route('/create_nat_form', methods=['GET', 'POST'])
#def create():



@app.route('/formulaire_nat_form', methods=['GET', 'POST'])
def formulaire_nat_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        srcIP=request.form['srcIP']
        srcPort=request.form['srcPort']
        destIP=request.form['destIP'] 
        destPort=request.form['destPort']
        return render_template('regle_nat.html', variable1=srcIP, variable2=srcPort, variable3=destIP, variable4=destPort )
        #if not srcIP:s
         #   flash('srcIP is required!')
        #elif not srcPort:
        #    flash('srcPort is required!')
        #elif not destIP:
        #    flash('destIP is required!')
        #elif not destPort:
        #    flash('destPort is required!')
        #messages.append({'srcIP': srcIP, 'srcPort': srcPort, 'destIP': destIP, 'destPort': destPort,}) 
       
    return render_template('formulaire_nat.html')



@app.route('/regle_nat_form', methods=['GET', 'POST'])
def regle_nat_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('regle_nat_form'))
    
    #if request.method == 'GET':
        
    # show the form, it wasn't submitted
    return render_template('regle_nat.html')

@app.route('/logout')
def logout():
    session.pop('key', None)
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=False)

