# shopify-frontend-clone

This is part of the technical interview for backend developer candidates for Coop Commerce.

## Setup

1. Clone this repo and `cd` into it
2. Create the virtual environment: `python3 -m venv venv`
3. Enter the virtual environment: `source venv/bin/activate`
4. Download the necessary packages: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Run the server: `python manage.py runserver`
7. Run `curl 'http://127.0.0.1:8000/api/ping/' | python -mjson.tool`. If it works, you should see `{
    "status": "pong"`
8. Create a test user: `python manage.py createsuperuser --username test --email test@test.com`
9. Create a token for this user: `python manage.py drf_create_token test`. Write this down for use below.
10. Seed your database with some categories e.g.: `curl -H 'Authorization: Token <token>' -H 'Content-Type: application/json' -X POST -d '{"name": "Toys"}' 'http://127.0.0.1:8000/api/categories/'`
}
`

## Exercise

We want to understand your proficiency with React.

Please write a basic shopify clone:

1. Create a login page that takes the credentials set above.
2. Create a product list page. One should be able to filter by category, search by name, and sort by price. Please us 'AND' logic here when multiple filters are applied. Use this endpoint: `curl -H 'Authorization: Token <token>' 'http://127.0.0.1:8000/api/products/'`
3. Create product creation page. Use this endpoint: `curl -H 'Authorization: Token <token>' -H 'Content-Type: application/json' -X POST -d '{"name": "Shampoo", "price": 5.99, "category": "1"}' 'http://127.0.0.1:8000/api/products/'`
4. There should be a product detail page. Use this endpoint: `curl -H 'Authorization: Token <token>' -H 'Content-Type: application/json' 'http://127.0.0.1:8000/api/products/<product id>/'`
5. Use functional components as much as possible. 
6. Use modern, ES6 syntax.
7. Use your best judgement on including frontend validation where needed.
8. Use your favorite UI toolkit (Semantic UI, Bootstrap, Material, etc).
9. Use `create-react-app` and add a folder called `client` to the root with its contents.
9. The layout is up to you. The only requirement is that a search bar be always present at top (like amazon). Using it should take the user to product list page.

## Test cases

1. Login
2. Create a product
3. List all products
4. Filter list of all products by category, sort by price, search by name
5. Product detail page

## Procedure

Fork this repo, create a branch, write your code, and submit a PR with a screencast of all the test cases above.
