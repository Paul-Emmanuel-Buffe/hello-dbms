from flask import Flask, render_template

def created_app():
# appli Flask
    app = Flask(__name__)

    #Routes
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/observations")
    def observations():
        return render_template("observations.html")

    @app.route("/analyse")
    def analyse():
        return render_template("analyse.html")

    @app.route("/methodologie")
    def methodologie():
        return render_template("methodologie.html")
    
    
    return app