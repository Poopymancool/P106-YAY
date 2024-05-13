# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "BARTHOLEMEW" # write your name
    age = "201" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage@
@app.route("/father")
def a():

    name = "fatherr100" # write your name
    age = "5" # write your age

    return render_template('father.html' , name = name , age = age)
# define the route to mother webpage
@app.route("/mother")
def c():

    name = "motherrrr100" # write your name
    age = "6" # write your age

    return render_template('mother.html' , name = name , age = age)
# define the route to friends webpage
@app.route("/friends")
def b():

    name = "firned of bartholemw" # write your name
    age = "200" # write your age

    return render_template('friend.html' , name = name , age = age)
# add other routes, if you want
@app.route("/bampow")
def d():


    return render_template('bam.html')


# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
