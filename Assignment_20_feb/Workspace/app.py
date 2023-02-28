from flask import Flask, request , render_template , jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/cube",methods=['POST'])
def cube():
    if (request.method=='POST'):
        num=request.form['num1']
        result = str(int(num)**3)
    return render_template('results.html', result = result)

@app.route("/postman_action",methods=['POST'])
def cube1():
    if (request.method=='POST'):
        num=request.json['num1']
        result = str(int(num)**3)
    return jsonify(result)


if __name__=="__main__":
    app.run(host="0.0.0.0")
