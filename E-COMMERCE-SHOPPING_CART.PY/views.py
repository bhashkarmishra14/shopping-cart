from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Product, Cart

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@main_blueprint.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    quantity = request.form.get('quantity', type=int)
    cart_item = Cart(product_id=product_id, quantity=quantity)
    db.session.add(cart_item)
    db.session.commit()
    return redirect(url_for('main.cart'))

@main_blueprint.route('/cart')
def cart():
    cart_items = Cart.query.all()
    return render_template('cart.html', cart_items=cart_items)

@main_blueprint.route('/checkout')
def checkout():
    # Add checkout logic here
    return render_template('checkout.html')
