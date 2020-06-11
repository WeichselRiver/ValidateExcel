from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
import pandas as pd

class FileUploadForm(FlaskForm):
    upload = FileField('xlsx-file', validators=[FileRequired(), FileAllowed(["xlsx"], 'Only upload xlsx-files')])
 

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret'


@app.route("/", methods=("GET", "POST",))
def index():

    form = FileUploadForm()

    if request.method == 'POST':
        f = request.files['upload']
        dta_xls = pd.read_excel(f)
        return dta_xls.to_html()
        
    if request.method == 'GET':
        return render_template("index.html", form=form)


@app.route("/report")
def report():
    return render_template("report.html")

if __name__ == "__main__":
    app.run(debug=True)