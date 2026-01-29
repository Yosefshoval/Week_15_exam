from typing import List, Dict, Any
from db import get_db_connection

def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    cnx = get_db_connection()
    
    statement = """
                SELECT customerName, creditLimit FROM customers
                WHERE creditLimit NOT BETWEEN 10000 AND 100000
                ;"""
    
    with cnx.cursor(dictionary=True) as cursor:
        cursor.execute(statement)
        result = cursor.fetchall()

    return result

def get_orders_with_null_comments():
    """Return orders that have null comments."""
    cnx = get_db_connection()

    statement = """
                SELECT orderNumber, comments FROM orders
                WHERE comments IS NULL
                ORDER BY orderDate
                ;"""
    
    with cnx.cursor(dictionary=True) as cursor:
        cursor.execute(statement)
        result = cursor.fetchall()

    return result

def get_first_5_customers():
    """Return the first 5 customers."""
    cnx = get_db_connection()

    statement = """
                SELECT * FROM (SELECT customerName, contactLastName, contactFirstName FROM customers
                LIMIT 5
                ) 5_customers
                ORDER BY contactLastName;
                ;"""

    with cnx.cursor(dictionary=True) as cursor:
        cursor.execute(statement)
        result = cursor.fetchall()

    return result

def get_payments_total_and_average():
    """Return total and average payment amounts."""
    cnx = get_db_connection()

    statement = """
                SELECT SUM(amount) AS total, AVG(amount) AS average, 
                MIN(amount) AS minimum, MAX(amount) AS maximum FROM payments
                ;"""
    
    with cnx.cursor(dictionary=True) as cursor:
        cursor.execute(statement)
        result = cursor.fetchall()

    return result

def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    cnx = get_db_connection()

    statement = """
                SELECT employees.firstName, employees.lastName, offices.phone AS officePhone FROM employees
                JOIN offices ON employees.officeCode = offices.officeCode
                ;"""
    
    with cnx.cursor(dictionary=True) as cursor:
        cursor.execute(statement)
        result = cursor.fetchall()

    return result

def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    cnx = get_db_connection()

    statement = """
                SELECT customers.customerName, orders.orderDate FROM customers
                LEFT JOIN orders ON customers.customerNumber = orders.customerNumber
                ;"""
    
    with cnx.cursor(dictionary=True) as cursor:
        cursor.execute(statement)
        result = cursor.fetchall()

    return result

def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    cnx = get_db_connection()

    statement = """
                SELECT customers.customerName, COUNT(orders.orderNumber) FROM customers
                JOIN orders ON customers.customerNumber = orders.customerNumber
                GROUP BY customers.customerNumber
                ORDER BY customers.customerName
                ;"""
    
    with cnx.cursor(dictionary=True) as cursor:
        cursor.execute(statement)
        result = cursor.fetchall()

    return result


def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """Return customers and payments for last names matching pattern."""
    cnx = get_db_connection()
    
    statement = """
                SELECT customers.customerName, CONCAT(employees.firstName, ' ', employees.lastName) AS employeeName, SUM(payments.amount) AS total FROM customers
                JOIN employees ON customers.salesRepEmployeeNumber = employees.employeeNumber
                JOIN payments ON payments.customerNumber = customers.customerNumber
                GROUP BY customers.customerName, employeeName
                HAVING customers.customerName LIKE '%Mu%' OR customers.customerName LIKE '%ly%'
                ORDER BY total DESC;
                """
    
    with cnx.cursor(dictionary=True) as cursor:
        cursor.execute(statement)
        result = cursor.fetchall()

    return result
