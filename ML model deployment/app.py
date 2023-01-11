import numpy as np
import sklearn
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [x for x in request.form.values()]
    tenure = float_features[0]
    whth = float_features[1]
    hsoap = float_features[2]
    oahfly = float_features[3]
    cpnusd = float_features[4]
    ordrcnt = float_features[5]
    dslo = float_features[6]
    cbamnt = float_features[7]
    cttr = float_features[8]
    ppm = float_features[9]
    gndr = float_features[10]
    poc = float_features[11]
    stsfscr = float_features[12]
    mrtlsts = float_features[13]
    cmpln = float_features[14]

    cttr1 = 0
    cttr2 = 0
    cttr3 = 0
    ppm_cod = 0
    ppm_cc = 0
    ppm_dc = 0
    ppm_ew = 0
    ppm_upi = 0
    gndr_m = 0
    gndr_f = 0
    poc_f = 0
    poc_g = 0
    poc_la = 0
    poc_mp = 0
    poc_ot = 0
    ss1 = 0
    ss2 = 0
    ss3 = 0
    ss4 = 0
    ss5 = 0
    ms_s = 0
    ms_d = 0
    ms_m = 0
    c1 = 0
    c0 = 0

    if cttr == 1:
        cttr1 = 1


    if cttr == 2:
        cttr2 = 1


    if cttr == 3:
        cttr3 = 1

    if ppm == "Cash_On_Delivery":
        ppm_cod = 1

    if ppm == "Credit_Card":
        ppm_cc = 1

    if ppm == "Debit_Card":
        ppm_dc = 1

    if ppm == "E_Wallet":
        ppm_ew = 1

    if ppm == "UPI":
        ppm_upi = 1

    if gndr == "Male":
        gndr_m = 1

    if gndr == "Female":
        gndr_f = 1

    if poc == "Fashion":
        poc_f = 1

    if poc == "Grocery":
        poc_g = 1

    if poc == "Laptop&Accessory":
        poc_la = 1

    if poc == "Mobile_Phone":
        poc_mp = 1


    if poc == "Others":
        poc_ot = 1

    if stsfscr == 1:
        ss1 = 1

    if stsfscr == 2:
        ss2 = 1

    if stsfscr == 3:
        ss3 = 1

    if stsfscr == 4:
        ss4 = 1


    if stsfscr == 5:
        ss5 = 1

    if mrtlsts == "Single":
        ms_s = 1

    if mrtlsts == "Divorced":
        ms_d = 1


    if mrtlsts == "Married":
        ms_m = 1

    if cmpln == "Yes":
        c1 = 1

    if cmpln == "No":
        c0 = 1

    final_features = [tenure, whth, hsoap, oahfly, cpnusd, ordrcnt, dslo, cbamnt, cttr1, cttr2, cttr3, ppm_cc, ppm_cod, ppm_dc, ppm_ew, ppm_upi, gndr_f, gndr_m, poc_f, poc_g, poc_la, poc_mp, poc_ot, ss1, ss2, ss3, ss4,
                      ss5, ms_d, ms_m, ms_s, c0, c1]
    features = [np.array(final_features)]
    prediction = model.predict(features)
    output = ""
    if format(prediction) == "[0]":
        output = "Not Churn"
    if format(prediction) == "[1]":
        output = "Churn"
    return render_template("after.html", prediction_text="The customer status is: "+output)


if __name__ == "__main__":
    flask_app.run(debug=True)