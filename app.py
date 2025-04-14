import streamlit as st

def product_catalog():
    st.header("Product Catalog Management")
    st.write("Display products with details, images, categories, and search functionality.")
    search_term = st.text_input("Search for a product")
    
    # Dummy products list (you can add your own images in the assets folder)
    products = [
        {"name": "Wireless Headphones", "price": "$50", "image": "assets/headphones.jpg", "description": "High-quality sound."},
        {"name": "Smart Watch", "price": "$120", "image": "assets/smart_watch.jpg", "description": "Keep track of your health."},
        {"name": "Laptop", "price": "$800", "image": "assets/laptop.jpg", "description": "Powerful performance."}
    ]
    
    if search_term:
        products = [p for p in products if search_term.lower() in p["name"].lower()]
    
    for product in products:
        st.subheader(product["name"])
        st.image(product["image"], width=150)
        st.write(product["description"])
        st.write(f"**Price:** {product['price']}")
        st.button("Add to Cart", key=product["name"])
        st.markdown("---")

def user_account():
    st.header("User Account Management")
    st.write("Register, login, manage profiles, and track order history.")
    st.button("Register")
    st.button("Login")

def shopping_cart():
    st.header("Shopping Cart and Checkout")
    st.write("Add products to your cart, review items, and complete purchases securely.")
    st.write("Cart is currently empty.")
    st.button("Proceed to Checkout")

def order_management():
    st.header("Order Management")
    st.write("Process orders, manage statuses, generate confirmations, and track orders.")
    st.write("No orders to display.")
    
def payment_processing():
    st.header("Payment Processing")
    st.write("Securely process online transactions using integrated payment gateways.")
    st.button("Pay Now")

def search_filter():
    st.header("Search and Filtering")
    st.write("Search for products based on keywords, categories, and filters.")
    st.text_input("Enter search keywords")
    st.selectbox("Select Category", ["Electronics", "Books", "Clothing", "Home & Kitchen"])

def admin_panel():
    st.header("Administrative Panel")
    st.write("Admin tools: manage products, users, orders, website content, and generate reports.")
    st.button("View Reports")
    st.button("Manage Users")

def main():
    # Configure page settings
    st.set_page_config(page_title="E-Commerce Demo", page_icon="🛒")
    
    # Top-level title and logo
    st.title("E-Commerce Website Demo")
    st.image("assets/logo.png", width=150, caption="Demo Logo")
    st.write("Welcome to our demo e-commerce website!")
    
    # Create navigation buttons using columns
    st.subheader("Navigate:")
    col1, col2 = st.columns(2)
    if col1.button("Product Catalog Management"):
        st.experimental_set_query_params(page="catalog")
        st.experimental_rerun()
    if col2.button("User Account Management"):
        st.experimental_set_query_params(page="account")
        st.experimental_rerun()
    
    col1, col2 = st.columns(2)
    if col1.button("Shopping Cart and Checkout"):
        st.experimental_set_query_params(page="cart")
        st.experimental_rerun()
    if col2.button("Order Management"):
        st.experimental_set_query_params(page="orders")
        st.experimental_rerun()
    
    col1, col2 = st.columns(2)
    if col1.button("Payment Processing"):
        st.experimental_set_query_params(page="payment")
        st.experimental_rerun()
    if col2.button("Search and Filtering"):
        st.experimental_set_query_params(page="search")
        st.experimental_rerun()
    
    if st.button("Administrative Panel"):
        st.experimental_set_query_params(page="admin")
        st.experimental_rerun()
    
    # Read the query parameters to determine which section to display
    query_params = st.experimental_get_query_params()
    if "page" in query_params:
        page = query_params["page"][0]
        st.sidebar.button("Back", on_click=lambda: st.experimental_set_query_params())  # Simple back button
        
        if page == "catalog":
            product_catalog()
        elif page == "account":
            user_account()
        elif page == "cart":
            shopping_cart()
        elif page == "orders":
            order_management()
        elif page == "payment":
            payment_processing()
        elif page == "search":
            search_filter()
        elif page == "admin":
            admin_panel()
    else:
        st.info("Select a section above to navigate.")

if __name__ == '__main__':
    main()
