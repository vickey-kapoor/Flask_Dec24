from flask import Flask, request
import pickle

app = Flask(__name__)

# Model loading
with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "<h1> Loan Approval Application </h1>"

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return "I will make the predictions."
    else:
        # Post request along with the data
        # then i will make the prediction.
        loan_req = request.get_json()

        if loan_req['Gender'] == "Male":
            Gender = 0
        else:
            Gender = 1

        if loan_req['Married'] == "No":
            Married = 0
        else:
            Married = 1

        ApplicantIncome = loan_req['ApplicantIncome']
        LoanAmount = loan_req['LoanAmount']
        Credit_History = loan_req['CreditHistory']

        input_data =[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]

        result = model.predict([input_data])

        if result == 0:
            pred = "Rejected"
        else:
            pred = "Approved"

        return {"Loan Approval Status":pred}