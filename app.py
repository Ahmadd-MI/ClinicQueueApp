from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

patients = []  # stores patients in queue
# home page route
@app.route("/")
def home():
    return render_template("home.html", patients=patients, total=len(patients))
# add patient route
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        complaint = request.form["complaint"]

        patient = f"{name} - Age {age} - {complaint}"
        patients.append(patient)

        return redirect(url_for("home"))

    return render_template("add.html")
# serve first patient in queue
@app.route("/serve")
def serve():
    if patients:
        patients.pop(0)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)