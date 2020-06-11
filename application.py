from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
import pandas as pd

class FileUploadForm(FlaskForm):
    upload = FileField('xlsx-file', validators=[FileRequired(), FileAllowed(["xlsx"], 'Only upload xlsx-files')])
 

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret'
tbl = "Test"

@app.route("/", methods=("GET", "POST",))
def index(tbl = tbl):

    form = FileUploadForm()

    if request.method == 'POST':
        f = request.files['upload']
        dta_xls = pd.read_excel(f)
        tbl = dta_xls.to_html()
        return render_template("index.html", form=form, tbl = tbl)
        
    if request.method == 'GET':
        return render_template("index.html", form=form, tbl = tbl)



if __name__ == "__main__":
    app.run(debug=True)