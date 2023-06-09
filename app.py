from flask import Flask, jsonify, render_template
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['codes']

@app.route('/code', methods=['GET'])
def get_code():
    latest_code = collection.find_one(sort=[("date", pymongo.DESCENDING)])
    return render_template('index.html',code=latest_code['code'])
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

