import flask
from flask import request
import requests
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
cors=CORS(app)
app.config["CORS_HEADERS"] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    storeType = brand = pkgtype = ""

    try:
        storeType = request.args.get('storeType', default='', type=str)
    except:
        pass
        
    try:
        brand = request.args.get('brand', default='', type=str)
    except:
        pass
    
    try:
        pkgtype = request.args.get('pkgtype', default='', type=str)
    except:
        pass
    
    postData = {'lat': request.args.get('lat'), 'long': request.args.get('long'),  'zip': request.args.get('zip'),  'custID': request.args.get('custID'), 'miles': request.args.get('miles'), 'storeType': storeType, 'brand': brand, 'pkgtype': pkgtype}   
    url = 'https://finder.vtinfo.com/finder/web/v2/iframe/search'

    res = requests.post(url, data=postData)
    return res.text

app.run()