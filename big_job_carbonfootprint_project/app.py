from flask import Flask, render_template
from db_connection import fetch_all

def created_app():
# appli Flask
    app = Flask(__name__)

    #Routes
    @app.route("/")
    def index():
        query="""
                SELECT * FROM (
                            SELECT *
                            FROM original_raw
                            LIMIT 5
                        )
                UNION ALL
                SELECT * FROM (
                    SELECT *
                    FROM original_raw
                    LIMIT 7 OFFSET (SELECT COUNT(*) -10 FROM original_raw)
                )
            """

        data = fetch_all(query)
        return render_template("index.html", data=data)

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