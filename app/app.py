from flask import Flask, render_template,jsonify
from model import dbWrapper
app = Flask(__name__)
app._static_folder = 'static'





@app.route('/changelog/<int:version>', methods=["GET"])
def returnReleaseDetails():



    return jsonify(
        date="tuesday",
        body="asdf",
        version="1.1",
        file = "google.ca"
    )
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()




# initial launch, check if db exists
# if db not exist, get all changelog data
#else, check if up to date

#connect webhook. if get post request from github, get new release data and update database

#in / route, get stored changelog data and store in a datastructure (dictionary)