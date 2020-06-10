from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
import pandas as pd

class FileUploadForm(FlaskForm):
    upload = FileField()

DEBUG = True
SECRET_KEY = 'secret'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/", methods=("GET", "POST",))
def index():

    form = FileUploadForm()

    if request.method == 'POST':
        f = request.files['upload']
        dta_xls = pd.read_excel(f)
        return dta_xls.to_html()
        
    if request.method == 'GET':
        return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run()