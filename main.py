from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
import calorie
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class FormPage(MethodView):

    def get(self):
        calorie_form = CalorieForm()
        return render_template('calorie_form_page.html', calorieForm=calorie_form)

    def post(self):
        calorieform = CalorieForm(request.form)
        calorie_form = CalorieForm()

        temperature = Temperature(city=calorieform.city.data, country=calorieform.country.data)
        calorie_need = calorie.CalorieCalculator(sex=calorieform.sex.data, age=float(calorieform.age.data),
                                                 weight=float(calorieform.weight.data), height=float(calorieform.height.data),
                                                 temperature=float(temperature.get()))
        return render_template('calorie_form_page.html',
                               result=True,
                               calorieForm=calorie_form,
                               calorieneed=calorie_need.calculate())


class CalorieForm(Form):
    sex = StringField("Sex: ", default="M")
    age = StringField("Age: ", default="26")
    weight = StringField("Weight: ", default="70")
    height = StringField("Height", default="181")

    country = StringField("Country: ", default="Romania")
    city = StringField("City: ", default="Bucharest")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie_form_page', view_func=FormPage.as_view('calorie_form_page'))

app.run(debug=True)
