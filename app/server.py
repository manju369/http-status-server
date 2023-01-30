import logging
import prometheus_client
from prometheus_client import Summary, Counter, Histogram, Gauge, generate_latest
from flask import Flask, jsonify, request, Response

logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)

count = 0
count_update = 0
count_callbackend = 0

graphs = {}
graphs['c'] = Counter('response_count', 'Total number of reponses generated', ['response'] )


@app.route("/codes")
def code_for_200():
    """ Return 200 HTTP Status code """
    global count
    count+=1
    graphs['c'].labels(response="200").inc()
    
    return jsonify({"code": 200}), 200


@app.route("/codes/update")
def code_for_201():
    """ Return 201 HTTP Status code """
    global count_update 
    count_update+=1
    graphs['c'].labels(response="201").inc()
    return jsonify({"code": 201 }), 201


@app.route("/codes/callbackend")
def code_for_503():
    """ Return 503 HTTP Status code """
    global count_callbackend
    count_callbackend+=1
    graphs['c'].labels(response="503").inc()
    return jsonify({"code": 503 }), 503

@app.errorhandler(404) 
def invalid_route(e):
    """ Return 503 HTTP Status code """
    graphs['c'].labels(response="404").inc() 
    return jsonify({"code": 404}), 404

@app.route('/metrics')
def metrics_count():
    """ Returns metrics in prometheus format """
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)
