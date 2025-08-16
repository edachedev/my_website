from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample items available for order
items = [
    {"id": 1, "name": "Laptop", "price": 250000},
    {"id": 2, "name": "Phone", "price": 120000},
    {"id": 3, "name": "Headphones", "price": 15000},
    {"id": 4, "name": "Watch", "price": 50000}
]

# Cart storage (for demo purposes; in real apps use a database)
cart = []


@app.route('/')
def index():
    return render_template('index.html', items=items)


@app.route('/add_to_cart/<int:item_id>')
def add_to_cart(item_id):
    for item in items:
        if item["id"] == item_id:
            cart.append(item)
            break
    return redirect(url_for('cart_page'))


@app.route('/cart')
def cart_page():
    total = sum(item["price"] for item in cart)
    return render_template('cart.html', cart=cart, total=total)


@app.route('/checkout', methods=['POST'])
def checkout():
    name = request.form.get("name")
    address = request.form.get("address")
    total = sum(item["price"] for item in cart)

    order_summary = {
        "customer": name,
        "address": address,
        "items": cart,
        "total": total
    }

    # Clear cart after checkout
    cart.clear()
    return render_template("success.html", order=order_summary)


if __name__ == "__main__":
    app.run(debug=True)
