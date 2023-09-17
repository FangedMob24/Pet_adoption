from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it 
Pet.query.delete()

# Add user
fred = Pet(name="Fred",photo_url="https://hips.hearstapps.com/hmg-prod/images/shih-tzu-little-dog-royalty-free-image-1652927214.jpg?crop=0.447xw:1.00xh;0.248xw,0&resize=980:*",species="Lab",age=6,available=False)

# Add new objects to session, so they'll persist
db.session.add(fred)

# Commit--otherwise, this never gets saved!
db.session.commit()