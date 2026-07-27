from flask import Flask, render_template

app = Flask(__name__)

# ---------------- HOME PAGE ----------------
@app.route('/')
def home():
    return render_template('index.html')


# ---------------- PRODUCTS PAGE ----------------
@app.route('/products')
def products():
    gift_items = [
        {
            "name": "Hair Clutcher Set",
            "price": "₹299",
            "image": "https://i.pinimg.com/736x/ff/64/d6/ff64d664b72b73a5d882983ffde95b4f.jpg"
        },
        {
            "name": "Chocolate Bouquet",
            "price": "₹599",
            "image": "https://i.pinimg.com/736x/df/85/a5/df85a58d70bd8e6252d21af403b05e01.jpg"
        },
        {
            "name": "Custom Bracelet",
            "price": "₹199",
            "image": "https://i.pinimg.com/1200x/f0/2e/0c/f02e0c6ecdad3d8490d53ad72ddc44d4.jpg"
        },
        {
            "name": "DIY Gift Box",
            "price": "₹499",
            "image": "https://i.pinimg.com/736x/ca/ba/b2/cabab209af59895b2e0e9ae1d6fde60a.jpg"
        },
        {
            "name": "Flower Bouquet",
            "price": "₹399",
            "image": "https://i.pinimg.com/736x/19/43/74/194374a135260fe5acbb0f185cc43680.jpg"
        },
        {
            "name": "Birthday Hamper",
            "price": "₹999",
            "image": "https://i.pinimg.com/1200x/13/5a/83/135a8332f4b7136fae146e603204c2f4.jpg"
        },
        {
            "name": "Anniversary Gift Box",
            "price": "₹1199",
            "image": "https://i.pinimg.com/736x/3e/b2/35/3eb23511d7280ee3a2b7d594fcb53f90.jpg"
        },
        {
            "name": "Festival Hamper",
            "price": "₹899",
            "image": "https://i.pinimg.com/736x/7b/da/65/7bda65c2a7b9e18a1ff4e62d6683d0c2.jpg"
        },
        {
            "name": "Crochet Flower Bouquet",
            "price": "₹699",
            "image": "https://i.pinimg.com/736x/03/56/9c/03569ce36df312c57ead80adc0ff8675.jpg"
        },
        {
            "name": "Crochet Keychains",
            "price": "₹149",
            "image": "https://i.pinimg.com/736x/12/f6/04/12f604a1a4dde2597aa52dedf19277ef.jpg"
        },
        {
            "name": "Crochet Toys",
            "price": "₹499",
            "image": "https://i.pinimg.com/736x/9e/12/5e/9e125e32bcbdeae07cec10947fdc6b63.jpg"
        }
    ]

    return render_template('products.html', products=gift_items)


# ---------------- CUSTOMIZE PAGE ----------------
@app.route('/customize')
def customize():
    return render_template('customize.html')


# ---------------- CART PAGE ----------------
@app.route('/cart')
def cart():
    return render_template('cart.html')


# ---------------- ORDER PAGE ----------------
@app.route('/order')
def order():
    return render_template('order.html')


# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)
