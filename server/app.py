from flask import Flask, request, jsonify, render_template
import util
# import util

app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")

@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("app.html")

@app.route('/predict_loan', methods=['POST'])
def predict_loan():

    gend = request.form['gend']
    dependent = int(request.form['dependent'])
    edu = request.form['edu']
    self_emp = request.form['self_emp']
    prop_area = request.form['prop_area']
    marry = request.form['marry']
    income = float(request.form['income'])
    com_income = float(request.form['com_income'])
    loan_am = float(request.form['loan_am'])
    loan_term = float(request.form['loan_term'])
    credit_hist = float(request.form['credit_hist'])

    response = jsonify({
        'loan_prediction': util.get_estimated_loan(gend, dependent, edu, self_emp, prop_area, marry, income, com_income, loan_am, loan_term, credit_hist)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()