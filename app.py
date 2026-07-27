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
            "name": "Hair Clutcher Bouquet ",
            "price": "₹999",
            "image": "https://i.pinimg.com/736x/ff/64/d6/ff64d664b72b73a5d882983ffde95b4f.jpg"
        },
        {
          "name": "Personalized Photo Magazine",
          "price": "₹1500",
          "image": "https://i.pinimg.com/1200x/34/6c/89/346c896935db88c10de250fe2a8763c0.jpg"
        },
        {
            "name": "Chocolate Bouquet",
            "price": "₹699",
            "image": "https://i.pinimg.com/736x/df/85/a5/df85a58d70bd8e6252d21af403b05e01.jpg"
        },
        {
            "name": "Custom Bracelet",
            "price": "₹499",
            "image": "https://i.pinimg.com/1200x/f0/2e/0c/f02e0c6ecdad3d8490d53ad72ddc44d4.jpg"
        },
        {
            "name": "DIY Gift Box",
            "price": "₹699",
            "image": "https://i.pinimg.com/736x/ca/ba/b2/cabab209af59895b2e0e9ae1d6fde60a.jpg"
        },
        {
            "name": "Flower Bouquet",
            "price": "₹899",
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
            "price": "₹999",
            "image": "https://i.pinimg.com/736x/2d/45/a0/2d45a0d2786f5b699409bf1c4f16d036.jpg"
        },
        {
            "name": "Crochet Keychains",
            "price": "₹249",
            "image": "https://i.pinimg.com/736x/12/f6/04/12f604a1a4dde2597aa52dedf19277ef.jpg"
        },
        {
            "name": "Crochet Toys",
            "price": "₹899",
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
@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form.get('name')
        product = request.form.get('product')

        return render_template('order.html', name=name, product=product)

    return render_template('order.html')


# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)
