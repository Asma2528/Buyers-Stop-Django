# Buyer’s Stop - E-Commerce Website

Welcome to **Buyer’s Stop**, a fully functional e-commerce website built with Django and modern web technologies. This project demonstrates a complete online shopping experience with product browsing, cart management, checkout, and order tracking.

---

## 🛠️ Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript, jQuery, Bootstrap
- **Database:** SQLite (default with Django, easily switchable to MySQL/PostgreSQL)
- **Others:** Django templating, static files handling

---

## 📦 Features & Modules

- **Home Page:** Showcase products with quick view options  
- **Product Listing:** View and browse available products  
- **Add to Cart:** Add desired quantity of products to cart  
- **Quick View:** Preview product details without leaving the page  
- **Checkout:** Place orders by filling shipping details  
- **Order Tracker:** Track order status using order ID  
- **Blog:** Read and interact with blog posts  
- **Contact Us:** Form to submit queries and feedback  

---

## 🗃️ Database Models

- **Stories:** For blog posts and news  
- **Product:** Product information and details  
- **Order:** Order information placed by customers  
- **OrderUpdate:** Track status updates of orders  
- **Contact:** User messages and feedback  

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Asma2528/Buyers-Stop-Django.git
   cd BuyersStop

2. Create and activate virtual environment
   ```bash
    python -m venv env
    source env/bin/activate       # On Linux/macOS
    env\Scripts\activate          # On Windows

3. Install dependencies
   ```bash
    pip install -r requirements.txt
   
4. Apply migrations
   ```bash
    python manage.py migrate

5. Run the development server
   ```bash
    python manage.py runserver
   
6. Access the site
7. Open your browser at http://127.0.0.1:8000/
