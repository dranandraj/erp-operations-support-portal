from flask import Flask, render_template
from modules.db import get_connection

app = Flask(__name__)

@app.route("/")
def home():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM customers")
    customers_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM materials")
    materials_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM sales_orders")
    sales_orders_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM support_requests")
    support_requests_count = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return render_template(
        "index.html",
        customers_count=customers_count,
        materials_count=materials_count,
        sales_orders_count=sales_orders_count,
        support_requests_count=support_requests_count
    )

@app.route("/customers")
def customers():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
                   SELECT customer_id, customer_name, country, status 
                   FROM customers
                   ORDER BY customer_id
                   """)
    customers = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("customers.html", customers=customers)

if __name__ == "__main__":
    app.run(debug=True)