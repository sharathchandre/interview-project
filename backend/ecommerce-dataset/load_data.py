# load_data.py
import pandas as pd
from database import SessionLocal, engine
from models import Product, Order
from database import Base

# Create tables
Base.metadata.create_all(bind=engine)

# Load CSVs
products_df = pd.read_csv("products.csv")
orders_df = pd.read_csv("orders.csv")

# Start DB session
db = SessionLocal()

# Insert products
for _, row in products_df.iterrows():
    product = Product(
        id=row["id"],
        name=row["name"],
        category=row["category"],
        price=row["price"],
        stock=row["stock"]
    )
    db.add(product)

# Insert orders
for _, row in orders_df.iterrows():
    order = Order(
        id=row["id"],
        product_id=row["product_id"],
        quantity=row["quantity"],
        customer_name=row["customer_name"]
    )
    db.add(order)

db.commit()
db.close()
