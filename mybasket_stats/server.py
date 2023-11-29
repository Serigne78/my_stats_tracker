from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, IntegerField, SelectField
from wtforms.validators import DataRequired
import csv



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)



class StasForm(FlaskForm):
    adversaire = StringField('Adversaire', validators=[DataRequired()])
    lieu = StringField("Domicile ou Exterieure", validators=[DataRequired()])
    heure = StringField("Heure", validators=[DataRequired()])
    points = IntegerField("Points marquées", validators=[DataRequired()])
    passd = IntegerField("Passe decisive", validators=[DataRequired()])
    rebonds = IntegerField("Rebonds", validators=[DataRequired()])
    intercp = IntegerField("Interceptions", validators=[DataRequired()])
    note= SelectField("Note:⭐",choices=["⭐","⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],validators=[DataRequired()])

    submit = SubmitField('Submit')


@app.route("/")
def home():
      return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_stats():
      form = StasForm() 
      if form.validate_on_submit():
            print("quoicoou")
            with open("stats-data.csv", mode="a", newline='', encoding="utf-8") as fichier_csv:
                  fichier_csv.write(f"\n{form.adversaire.data},"
                                    f"{form.lieu.data},"
                                    f"{form.heure.data},"
                                    f"{form.points.data},"
                                    f"{form.passd.data},"
                                    f"{form.rebonds.data},"
                                    f"{form.intercp.data},"
                                    f"{form.note.data}")
            return redirect(url_for('stats'))
      print(form.validate_on_submit())
      return render_template("add.html" ,form=form)

@app.route("/stats", methods=["GET", "POST"])
def stats():

      with open('stats-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
      return render_template('stats.html', cafes=list_of_rows, long=len(list_of_rows))


if __name__ == '__main__':
    app.run(debug=True, port=8080)