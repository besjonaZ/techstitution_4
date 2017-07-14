from flask import Flask, render_template, request
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'techsitution4'

mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        #Query to retrieve data from DB
        assign = mongo.db.audit.find()
        print assign
        return render_template('index.html')
    elif request.method == 'POST':
        data=request.form
        audit_name = data['audit_name']#Getting audit name
        audit_ref = data['ref_num']#Getting audit ref num value
        #Query for inserting into DB
        mongo.db.audit.insert({
        "audit_name": audit_name,
        "audit_ref": audit_ref
        })

        return "POST METHOD"
if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0', debug=True)
