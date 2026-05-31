import requests
from behave import given

@given('the following products')
def step_impl(context):
    # Clear existing products
    res = requests.get(f"{context.base_url}/products")
    for row in res.json():
        requests.delete(f"{context.base_url}/products/{row['id']}")
    
    # Load new products from feature file table
    for row in context.table:
        payload = {
            "name": row['name'],
            "description": row['description'],
            "price": float(row['price']),
            "available": row['available'].lower() in ['true', '1', 't'],
            "category": row['category']
        }
        context.resp = requests.post(f"{context.base_url}/products", json=payload)
        assert context.resp.status_code == 201
