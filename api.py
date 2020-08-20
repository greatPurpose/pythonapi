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

    res = requests.post(url, data=postData, headers={'referer': 'https://finder.vtinfo.com/finder/web/v2/iframe?custID=HOF&theme=bs-journal'})
    if res.text.find("You are over your daily allowed usage limit") > -1 :
        postData = {'lat': request.args.get('lat'), 'long': request.args.get('long'),  'zip': request.args.get('zip'),  'custID': request.args.get('custID'), 'category1':'Brandfinder', 'miles': request.args.get('miles'), 'storeType': storeType, 'brand': brand, 'pkgtype': pkgtype}
        res = requests.post(url, data=postData, headers={'referer': 'https://finder.vtinfo.com/finder/web/v2/iframe?custID=HOF&category1=Brandfinder'})
        
    return res.text

if  __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)