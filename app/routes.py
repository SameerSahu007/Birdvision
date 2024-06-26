from flask import request, jsonify, Blueprint
from . import db
from .models import Product


main = Blueprint("/", __name__)

@main.route('/')
def index():
    return 'User added successfully!'


# Get all products
@main.route('/products', methods = ['GET'])
def getAllProducts():
    products = Product.query.all()

    if products:
        product_list = []
        for product in products:
            product_data = {
                'id': product.id,
                'title': product.title,
                'description': product.description,
                'price': product.price
            }
            product_list.append(product_data)
        return jsonify({'products': product_list})
    else:
        return jsonify({'products': []})

# Get product with a particular id
@main.route('/products/<id>', methods = ['GET'])
def getProductById(id):

    product = db.session.get(Product, int(id))
    if product:
        product_data = {
            'id': product.id,
            'title': product.title,
            'description': product.description,
            'price': product.price
        }
        return jsonify({'product': product_data})
    else:
        return jsonify({'error': 'Product not found'}), 404


# Add new product
@main.route('/products', methods = ['POST'])
def postProducts():
    data = request.get_json()
    
    title = data.get('title')
    description = data.get('description')
    price = data.get('price')

    new_product = Product(title=title, description=description, price=price)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product added successfully!'})

# Update the product details 
@main.route('/products/<id>', methods=['PUT'])
def updateProduct(id):
    product =  db.session.get(Product, int(id))
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    data = request.get_json()
    if 'title' in data:
        product.title = data['title']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = data['price']

    db.session.commit()

    return jsonify({'message': 'Product updated successfully'})

#Delete a product
@main.route('/products/<int:id>', methods=['DELETE'])
def deleteProduct(id):
    product = db.session.get(Product, int(id))
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product deleted successfully'})


