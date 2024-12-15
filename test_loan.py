import pytest

from loan_app import app

# Proxy to a live server
@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200
    resp.text = "<h1>Loan Approval Application</h1>"

def test_predict(client):
    test_data = {
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 5000,
        "LoanAmount": 500,
        "CreditHistory": 1
        }
    resp = client.post("/predict", json=test_data)
    assert resp.status_code == 200
    assert resp.json == {'Loan Approval Status': "Approved"}