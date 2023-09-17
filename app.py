from flask import Flask, request, redirect, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'HelloWorld'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    """List of all pets"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods = ['GET','POST'])
def pet_form():
    """Pet add form; handle adding"""
    form = AddPetForm()

    if form.validate_on_submit():
        # Adds the values to the database
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    else:
        # renders the form page
        return render_template('pet_form.html', form=form)
    
@app.route('/<int:pet_id>', methods = ['GET','POST'])
def pet_info(pet_id):
    """Shows information and the ability to update some fields"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        # updates values in the database
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet.html',pet=pet, form=form)