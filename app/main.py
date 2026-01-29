from fastapi import FastAPI
from db_init import init_database
import dal

app = FastAPI()

init_database()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/q1/customers-credit-limit-outliers")
def customers_credit_limit_outliers():
    try:
        result = dal.get_customers_by_credit_limit_range()
        return {"status" : "ok", "result" : result}
    except Exception as e:
        return {"error": str(e)}


@app.get("/q2/orders-null-comments")
def orders_null_comments():
    try:
        result = dal.get_orders_with_null_comments()
        return {"status" : "ok", "result" : result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/q3/customers-first-5")
def customers_first_5():
    try:
        result = dal.get_first_5_customers()
        return {"status" : "ok", "result" : result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/q4/payments-total-average")
def payments_total_average():
    try:
        result = dal.get_payments_total_and_average()
        return {"status" : "ok", "result" : result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/q5/employees-office-phone")
def employees_office_phone():
    try:
        result = dal.get_employees_with_office_phone()
        return {"status" : "ok", "result" : result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/q6/customers-shipping-dates")
def customers_shipping_dates():
    try:
        result = dal.get_customers_with_shipping_dates()
        return {"status" : "ok", "result" : result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/q7/customer-quantity-per-order")
def customer_quantity_per_order():
    try:
        result = dal.get_customer_quantity_per_order()
        return {"status" : "ok", "result" : result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/q8/customers-payments-by-lastname-pattern")
def customers_payments_by_lastname_pattern(pattern: str = "son"):
    try:
        result = dal.get_customers_payments_by_lastname_pattern()
        return {"status" : "ok", "result" : result}
    except Exception as e:
        return {"error": str(e)}
