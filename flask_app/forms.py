from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class RecipesSearchForm(FlaskForm):
    ingredients_search = StringField('Ingredients Search(Separate multiple ingredients with commas)',
                         validators=[DataRequired(), Length(min=2, max=20)],
                                     render_kw={'style': 'font-size: 18px;'})
    search = SubmitField('Search')
