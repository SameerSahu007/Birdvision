from app.models import Product
import json

# test for getting all the products
def test_getAllProducts(client, app):
    
    # adding three products
    post1 = client.post("/products", json={"title": "Product 1", "description": "Description 1", "price":10})
    post2 = client.post("/products", json={"title": "Product 2", "description": "Description 2", "price":20})
    post3 = client.post("/products", json={"title": "Product 3", "description": "Description 3", "price":30})
    
    response = client.get("/products")
    products_data = json.loads(response.data)
    products_list = products_data['products']

    assert len(products_list) == 3
    assert products_list[0]['title'] == "Product 1"
    assert products_list[1]['title'] == "Product 2"
    assert products_list[2]['title'] == "Product 3"
    
# test for getting a product with a given id
def test_getProductById(client, app):
    # adding two products
    post1 = client.post("/products", json={"title": "Product 1", "description": "Description 1", "price":10})
    post2 = client.post("/products", json={"title": "Product 2", "description": "Description 2", "price":20})
    
    # getting a product with the id 2
    response = client.get("/products/2")
    products_data = json.loads(response.data)

    #checking if we got the right product
    assert products_data['product']['id'] == 2
     
# test for adding products
def test_postProducts(client, app):
    response = client.post("/products", json={"title": "soap", "description": "This is a soap", "price":"50"})
    
    with app.app_context():
        # checking for posted data in database 
        assert Product.query.count() == 1
        assert Product.query.first().title == "soap"
        assert Product.query.first().description == "This is a soap"
        assert Product.query.first().price == 50
        
# test for update product 
def test_updateProduct(client, app):
    # send a PUT request to update the product with ID 2
    update_response = client.put("/products/2", json={"title": "Product 1", "description": "Description 1", "price":10})
    
    # parse the JSON response from the PUT request
    update_response_data = json.loads(update_response.data)
    
    # check if the response contains an error message
    assert 'error' in update_response_data
    
    # assert that the error message indicates a problem with updating the product
    assert update_response_data['error'] == "Product not found"
    
    #adding a product for test
    post1 = client.post("/products", json={"title": "Product 1", "description": "Description 1", "price":10})
    
    #updating the product added earlier by changing its title
    put_resquest = client.put("/products/1", json={"title": "Product One", "description": "Description 1", "price":10})
    
    with app.app_context():
        # checking for posted data in database 
        assert Product.query.count() == 1
        assert Product.query.first().title == "Product One"

# test for update product 
def test_deleteProduct(client, app):
    
    # send a DELETE request to update the product with ID 2
    delete_response = client.delete("/products/2")
    
    # parse the JSON response from the DELETE request
    delete_response_data = json.loads(delete_response.data)
    
    # check if the response contains an error message
    assert 'error' in delete_response_data
    
    # assert that the error message indicates a problem with updating the product
    assert delete_response_data['error'] == "Product not found"
    
    #adding a product for test
    post1 = client.post("/products", json={"title": "Product 1", "description": "Description 1", "price":10})
    
    # DELETE request for product with id 1
    delete_response_2 = client.delete("/products/1")
    delete_response_data_2 = json.loads(delete_response_2.data)
    
    assert 'message' in delete_response_data_2
    assert delete_response_data_2['message'] == "Product deleted successfully"
    
    
    