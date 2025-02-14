# E-commerce-project
Overview

This is a full-featured eCommerce web application built using Django. The project allows users to browse products, add them to their cart, place orders, and make payments. Admins can manage products, orders, and customers from a dedicated dashboard.

Features

User authentication (Registration, Login, Logout, Password Reset)

Product listing and details page

Shopping cart functionality

Order management

Payment integration (e.g., Stripe, PayPal)

Admin dashboard for product and order management

Technologies Used

Backend: Python, Django, Django REST Framework

Frontend: HTML, CSS, JavaScript

Database: Sqlite3

Authentication: Django Authentication

Payment Gateway: Stripe/PayPal

Usage

Access the website at http://127.0.0.1:8000/

Admin dashboard: http://127.0.0.1:8000/admin/

API Endpoints (if using Django REST Framework)

Method

Endpoint

Description

GET

/api/products/

Get all products

GET

/api/products/<id>/

Get product details

POST

/api/cart/

Add to cart

GET

/api/orders/

Get user orders

POST

/api/orders/

Place an order
