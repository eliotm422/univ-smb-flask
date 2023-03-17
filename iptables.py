# save this as app.py
from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route('/home_form', methods=['GET', 'POST'])
def home_form():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('home.html')

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


if __name__ == "__main__":
    app.run(debug=False)

