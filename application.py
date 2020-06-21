from flask import Flask, render_template, request, url_for, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
import pandas as pd
from datetime import datetime
import json
from pydantic import BaseModel

class FileUploadForm(FlaskForm):
    upload = FileField('xlsx-file', validators=[FileRequired(), FileAllowed(["xlsx"], 'Only upload xlsx-files')])
 

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret'

ext_data = {
    'MichNr' : 1,
    'Beschreibung' : 'kreuzer'
}

def validate():
     
    class Marke(BaseModel):
        MichNr: int
        Beschreibung : str

    return Marke(**ext_data)

@app.route("/", methods=("GET", "POST",))
def index():

    form = FileUploadForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            f = request.files['upload']
            print(f.filename)
            dta_xls = pd.read_excel(f)
            result = {
                "Filename: " : f.filename,
                "Date and time: " : str(datetime.utcnow()),
                "Number of rows: " : dta_xls.shape[0],
                "Number of columns: " : dta_xls.shape[1],
                "Validation: " : str(validate_df(dta_xls))
            }
            print(json.dumps(result))

            tbl = dta_xls.to_html()
            return render_template("index.html", form=form, tbl = result)
        
    if request.method == 'GET':
        return render_template("index.html", form=form, tbl = "")



if __name__ == "__main__":
    app.run(debug=True)

