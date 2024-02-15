from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the model
with open('best_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        return redirect(url_for('result'))
    return render_template('predict.html')
@app.route('/result', methods=['POST'])
def result():
    if request.method == "POST":
        Company_Name = request.form['Company_Name']
        Job_Title = request.form['Job_Title']
        Location = request.form['Location']
        Job_Roles = request.form['Job_Roles']
        salaries_report = request.form['salaries_report']
        Employment_Status = request.form['Employment_Status']
        Rating = request.form['Rating']

        # Make sure to convert the inputs to the correct types before creating the prediction input
        pred = [[int(Company_Name), int(Job_Title), int(Location), int(Job_Roles), int(Employment_Status), float(Rating),int(salaries_report)]]

        output = model.predict(pred)

        return render_template('result.html', predict="The Predicted Salary of an Employer is: " + str(output[0]))

if __name__ == '__main__':
    app.run(debug=True)
