from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 🛒 Temporary cart
cart = []

# 🎁 PRODUCTS WITH YOUR IMAGE LINKS (₹ INR)
products = [

    {
        "id": 1,
        "name": "Hair Clutcher Set 🎀",
        "price": 299,
        "image": "https://i.pinimg.com/736x/ff/64/d6/ff64d664b72b73a5d882983ffde95b4f.jpg",
        "category": "accessories"
    },

    {
        "id": 2,
        "name": "Chocolate Bouquet 🍫💐",
        "price": 799,
        "image": "https://i.pinimg.com/736x/df/85/a5/df85a58d70bd8e6252d21af403b05e01.jpg",
        "category": "bouquet"
    },

    {
        "id": 3,
        "name": "Customized Bracelet ✨",
        "price": 399,
        "image": "https://i.pinimg.com/1200x/f0/2e/0c/f02e0c6ecdad3d8490d53ad72ddc44d4.jpg",
        "category": "accessories"
    },

    {
        "id": 4,
        "name": "DIY Gift Box 🎁",
        "price": 699,
        "image": "https://i.pinimg.com/736x/ca/ba/b2/cabab209af59895b2e0e9ae1d6fde60a.jpg",
        "category": "diy"
    },

    {
        "id": 5,
        "name": "Flower Bouquet 🌸",
        "price": 499,
        "image": "https://i.pinimg.com/736x/19/43/74/194374a135260fe5acbb0f185cc43680.jpg",
        "category": "bouquet"
    },

    {
        "id": 6,
        "name": "Birthday Hamper 🎂",
        "price": 999,
        "image": "https://i.pinimg.com/1200x/13/5a/83/135a8332f4b7136fae146e603204c2f4.jpg",
        "category": "birthday"
    },

    {
        "id": 7,
        "name": "Anniversary Gift Box 💍",
        "price": 1099,
        "image": "https://i.pinimg.com/736x/3e/b2/35/3eb23511d7280ee3a2b7d594fcb53f90.jpg",
        "category": "anniversary"
    },

    {
        "id": 8,
        "name": "Festival Hamper 🎉",
        "price": 899,
        "image": "https://i.pinimg.com/736x/7b/da/65/7bda65c2a7b9e18a1ff4e62d6683d0c2.jpg",
        "category": "festival"
    },

    {
        "id": 9,
        "name": "Crochet Flower Bouquet 🌷",
        "price": 599,
        "image": "https://i.pinimg.com/736x/03/56/9c/03569ce36df312c57ead80adc0ff8675.jpg",
        "category": "crochet"
    },

    {
        "id": 10,
        "name": "Crochet Keychains 🔑",
        "price": 199,
        "image": "https://i.pinimg.com/736x/12/f6/04/12f604a1a4dde2597aa52dedf19277ef.jpg",
        "category": "crochet"
    },

    {
        "id": 11,
        "name": "Crochet Toys 🧸",
        "price": 499,
        "image": "https://i.pinimg.com/736x/9e/12/5e/9e125e32bcbdeae07cec10947fdc6b63.jpg",
        "category": "toys"
    }

]

# 🏠 Home Page
@app.route('/')
def home():
    return render_template('index.html')


# 🛍️ Products Page
@app.route('/products')
def products_page():
    return render_template('products.html', products=products)


# ✏️ Customize Page
@app.route('/customize/<int:product_id>', methods=['GET', 'POST'])
def customize(product_id):
    product = next((p for p in products if p["id"] == product_id), None)

    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        cart.append({
            "product": product["name"],
            "price": product["price"],
            "name": name,
            "message": message
        })

        return redirect(url_for('cart_page'))

    return render_template('customize.html', product=product)


# 🛒 Cart Page
@app.route('/cart')
def cart_page():
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)


# 📦 Order Page
@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        customer = request.form['customer']
        address = request.form['address']

        return render_template('order.html', success=True, customer=customer)

    return render_template('order.html', success=False)


# ▶️ Run App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
