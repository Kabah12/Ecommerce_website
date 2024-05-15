from flask import Flask, render_template, url_for, request, redirect, make_response
from Models.routes import app_blueprint

app = Flask(__name__)
app.debug = True

app.template_folder = 'Templates'

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(app_blueprint)

if __name__ == "__main__":
    app.run()