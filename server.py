from flask import Flask, render_template, redirect
from flask import request
import csv 



app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/index")
def return_home():
    return render_template('index.html')


@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/works")
def works_page():
    return render_template('works.html')

@app.route("/contact")
def contact_page():
    return render_template('contact.html')

@app.route("/components")
def componets_page():
    return render_template('components.html')

@app.route("/work")
def work_page():
    return render_template('work.html')

@app.route("/thankyou")
def thankyou_page():
    return render_template('thankyou.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou")
        except:
            return print('not sent to database')
    else:
        return 'someting went wrong try again'


def write_to_file(data):
    with open('C:\\Users\\pauli\\OneDrive\\Pulpit\\WEB_SERVER\\database.txt', mode = "a") as database:
        email = data["email"]
        subject = data["subject"]   
        message = data["message"]
        file = database.write(f"\n email: {email}, subject: {subject}, message: {message}")

def write_to_csv(data):
    with open('C:\\Users\\pauli\\OneDrive\\Pulpit\\WEB_SERVER\\database.csv', newline='', mode = "a") as database2:
        email = data["email"]
        subject = data["subject"]   
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=';', dialect='excel', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
