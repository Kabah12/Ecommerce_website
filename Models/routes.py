from flask import Blueprint, render_template

app_blueprint = Blueprint('route', __name__, url_prefix='/api/v1/route')

@app_blueprint.route("/about")
def about():
    return render_template("about.html")

@app_blueprint.route("/blog")
def blog():
    return render_template("blog.html")

@app_blueprint.route("/cart")
def cart():
    return render_template("cart.html")

@app_blueprint.route("/contact")
def contact():
    return render_template("contact.html")

@app_blueprint.route("/shop")
def shop():
    return render_template("shop.html")

@app_blueprint.route("/sale_product")
def sale_product():
    return render_template("sproduct.html")