from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Name of Pet",
                       validators=[InputRequired()])
    species = StringField("Species of Pet",
                          validators=[InputRequired(),AnyOf(['dog','cat','porcupine'])])
    photo_url = StringField("URL for Photo",
                            validators=[Optional(),URL(require_tld=False)])
    age = IntegerField("Age of Dog",
                       validators=[Optional(),NumberRange(min=0,max=30, message="Must be between 0 and 30")])
    notes = StringField("Notes for dog",
                        validators=[Optional()])
    
class EditPetForm(FlaskForm):
    """Form to edit pet info"""
    photo_url = StringField("URL for Photo",
                            validators=[Optional(),URL(require_tld=False)])
    notes = StringField("notes for pet",
                       validators=[Optional()])
    available = BooleanField("Availability")
