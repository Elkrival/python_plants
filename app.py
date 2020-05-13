from flask import Flask, request, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, json

#init app with flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello World'})


@app.route('/plant', methods=['GET'])
def plantGet():
    # one = requests.get('https://trefle.io/api/kingdoms/1?token=Tm8wcmJQMDNWemMrZnVRYmxWbllFQT09').json()
    two = []
    one = requests.get('https://trefle.io/api/plants?token=Tm8wcmJQMDNWemMrZnVRYmxWbllFQT09').json()
    for x in one:
        if x['common_name'] is None:
           x.pop('common_name')
           two.append(x)


    # return requests.get('https://trefle.io/api/plants?token=Tm8wcmJQMDNWemMrZnVRYmxWbllFQT09').content
    return jsonify({"plantList": two })

#Run server
if __name__ == '__main__':
    app.run(debug=True)