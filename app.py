from flask import Flask
from flask import render_template, request, redirect
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/', methods=["POST","GET"])
def catbook_home():
	if request.method == "POST":
		name = request.form['name']
		pic = request.form["pic"]
		votes = 0

		create_cat(name, pic, votes)
		cats = get_all_cats()
	else:
		cats = get_all_cats()
	return render_template("home.html", cats=cats)

@app.route("/cats/<int:id>", methods=["POST","GET"])
def profile_page(id):
	cat =get_one_cat(id)

	
	return render_template("cat.html", cat=cat )

@app.route("/cats/<int:id>/updatev")
def update_votes(id):
	cat =get_one_cat(id)
	update_votes_db(id)
	return render_template("cat.html", cat=cat)


@app.route("/newcat")
def new_cat_page():
	return render_template("new_cat.html")
if __name__ == '__main__':
   app.run(debug = True)
