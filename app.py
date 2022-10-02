from flask import Flask

app = Flask(__name__)

# use route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
def welcome():
    return "this is our home page. Welcome !!!"

@app.route("/intro")

def myintro():
    return "this is shaurya!!"

if(__name__ == "__main__"):
    app.run(debug = True)
    #app.run(debug=True , port = 8000)