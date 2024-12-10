from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    flowers = [
        {"id": 1, "name": "Rose", "price": "$10", "image": "/static/roses.jpeg"},
        {"id": 2, "name": "Lily", "price": "$12", "image": "/static/liles.jpeg"},
        {"id": 3, "name": "Tulip", "price": "$8", "image": "/static/tulips.jpeg"},
        {"id": 4, "name": "Sunflower", "price": "$15", "image": "/static/sunflower.jpeg"},
        {"id": 5, "name": "Orchid", "price": "$20", "image": "/static/orchid.jpeg"}
    ]
    return render_template('flowers.html', flowers=flowers)

if __name__ == '__main__':
    app.run(debug=True)
