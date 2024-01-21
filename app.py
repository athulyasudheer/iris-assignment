from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction', methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        value_1 = request.form["prediction_value_1"]
        value_2 = request.form["prediction_value_2"]
        value_3 = request.form["prediction_value_3"]
        value_4 = request.form["prediction_value_4"]
        model = pickle.load(open('model.pkl', 'rb'))
        res = model.predict([[float(value_1),float(value_2),float(value_3),float(value_4)]])
        print(res)
    return render_template('prediction.html', prediction=res)
if __name__ == '__main__':
    app.run()
