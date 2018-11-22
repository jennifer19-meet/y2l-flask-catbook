from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name, pic, votes):
    cat_object = Cat(name=name, pic=pic,votes=votes)
    session.add(cat_object)
    session.commit()

def get_all_cats():
    cats = session.query(Cat).all()
    return cats

def get_one_cat(id):
	cat  = session.query(Cat).filter_by(id = id).first()
	return cat
def update_votes_db(id):
	cat  = session.query(Cat).filter_by(id = id).first()
	v = cat.votes
	cat.votes =v +1
	session.commit()
	return cat
