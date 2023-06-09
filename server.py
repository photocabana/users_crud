from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models import user
from flask_app.controllers import users #controllers go here
from flask_app.config.mysqlconnection import connectToMySQL


@app.route('/')
def index():
    return render_template('read.html', user = user.User.get_all_users())


@app.route('/second')
def second_page():
    return render_template('create.html')

@app.route('/second/create', methods=['POST'])
def create_user():
    user.User.new_user(request.form)
    return redirect("/")


@app.route('/third/<int:id>')
def third_page(id):
    user.User.delete_user(id)
    return redirect("/")

@app.route('/show/<int:id>')
def show_user(id):
    return render_template('view.html', user = user.User.get_one_user(id))



@app.route('/fourth/<int:id>')
def fourth_page(id):
    return render_template('update.html', user = user.User.get_one_user(id))

@app.route('/fourth', methods=['POST'])
def update_page():
    user.User.update_user(request.form)
    return redirect ('/')


if __name__=="__main__":   
    app.run(debug=True) 

# debug needs to be set to False when deployed.
# We shared a video showing how the information leaked by this feature and help hackers.

