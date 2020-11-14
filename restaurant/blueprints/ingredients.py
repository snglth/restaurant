from flask import Blueprint, flash, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, DecimalField, SubmitField, validators
from wtforms.validators import DataRequired, NumberRange

from restaurant.models.schema import Ingredient

from restaurant.app import db
from restaurant.const import MEASUREMENT_UNITS

ingredients = Blueprint("ingredients", __name__, url_prefix="/ingredients")


class IngredientForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[DataRequired()],
    )
    unit = SelectField(
        "Measurement Unit",
        choices=MEASUREMENT_UNITS,
        validators=[validators.DataRequired()],
    )
    calorific = DecimalField(
        "Calorific Value",
        validators=[DataRequired(), NumberRange(0)],
    )
    fats = DecimalField(
        "Fats Value", validators=[DataRequired(), NumberRange(0)],
    )
    proteins = DecimalField(
        "Proteins Value",
        validators=[DataRequired(), NumberRange(0)],
    )
    carbohydrates = DecimalField(
        "Carbohydrates Value",
        validators=[DataRequired(), NumberRange(0)],
    )
    submit = SubmitField("Submit")


@ingredients.route("/", methods=["GET"])
def index():
    ingredients = Ingredient.query.all()
    return render_template("ingredients/index.html", ingredients=ingredients)


@ingredients.route("/new", methods=["GET", "POST"])
def new_ingredient():
    form = IngredientForm()
    if form.validate_on_submit():
        ingredient = Ingredient(
            title=form.title.data,
            unit=form.unit.data,
            calorific=form.calorific.data,
            fats=form.fats.data,
            proteins=form.proteins.data,
            carbohydrates=form.carbohydrates.data,
        )
        db.session.add(ingredient)
        db.session.commit()
        flash("Ingredient added")
        return redirect(url_for(".index"))
    return render_template("ingredients/new.html", form=form)
