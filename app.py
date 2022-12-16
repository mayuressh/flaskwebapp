import flask
app = flask.Flask(__name__)

@app.route("/",methods=['GET'])
def func():
    return "<h1>Demo flask webapp</h1>"

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')