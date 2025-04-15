import streamlit as st
from PIL import Image

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="E-Commerce Demo",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="auto"
)

# -----------------------------
# Sidebar: Search & Filters
# -----------------------------
st.sidebar.header("Search & Filters")
search_term = st.sidebar.text_input("Search Products")
cost_range = st.sidebar.slider("Select Price Range ($)", min_value=0, max_value=1000, value=(0, 1000))
category = st.sidebar.selectbox("Category", ["All", "Electronics", "Wearables", "Computers"])

# -----------------------------
# Initialize session state (cart)
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = {}  # format: {product_name: quantity}

# -----------------------------
# Dummy Data for Products
# -----------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 50,
        "image": "assets/headphones.jpeg",
        "description": "High-quality wireless headphones with noise cancellation.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 120,
        "image": "assets/smart_watch.jpeg",
        "description": "Fitness tracking smart watch with long battery life.",
        "category": "Wearables"
    },
    {
        "name": "Laptop",
        "price": 800,
        "image": "assets/laptop.jpeg",
        "description": "Sleek laptop with powerful performance for work and play.",
        "category": "Computers"
    },
    {
        "name": "Bluetooth Speaker",
        "price": 40,
        "image": "assets/speaker.jpeg",
        "description": "Compact speaker with impressive sound quality.",
        "category": "Electronics"
    },
    {
        "name": "DSLR Camera",
        "price": 650,
        "image": "assets/camera.jpeg",
        "description": "Professional DSLR camera for photography enthusiasts.",
        "category": "Electronics"
    }
]

# Extra "deal" products
deal_products = [
    {
        "name": "Gaming Mouse",
        "price": 30,
        "original_price": 45,
        "image": "assets/gaming.jpeg",
        "description": "High DPI gaming mouse with colorful lighting.",
    },
    {
        "name": "Noise Cancelling Earbuds",
        "price": 25,
        "original_price": 50,
        "image": "assets/buds.jpeg",
        "description": "In-ear buds with active noise cancelling technology.",
    }
]

# -----------------------------
# Helper Functions
# -----------------------------
def add_to_cart(product_name, quantity=1):
    """Add the specified quantity of a product to the cart."""
    if product_name in st.session_state.cart:
        st.session_state.cart[product_name] += quantity
    else:
        st.session_state.cart[product_name] = quantity

def show_cart():
    """Display items in the cart with an enlarged image, quantity, and pricing details."""
    st.write("### Your Cart")
    if not st.session_state.cart:
        st.info("Your cart is empty.")
        return

    total_amount = 0
    for product_name, qty in st.session_state.cart.items():
        # Search for product details in main or deal products
        product = next((p for p in products if p["name"] == product_name), None)
        if not product:
            product = next((dp for dp in deal_products if dp["name"] == product_name), None)
        if product:
            line_price = product["price"] * qty
            total_amount += line_price
            # Create a layout row with an enlarged image and details
            col_img, col_detail = st.columns([1, 3])
            with col_img:
                st.image(product["image"], width=100)
            with col_detail:
                st.write(f"**{product_name}**")
                st.write(f"Quantity: {qty}")
                st.write(f"Price: ${product['price']} each")
                st.write(f"Total: ${line_price}")
            st.markdown("---")
    st.write(f"### Cart Total: ${total_amount}")
    if st.button("Proceed to Payment"):
        st.success("Payment option would appear here (Stripe, PayPal, etc.)")

def display_products(product_list):
    """Display a list of products with interactive quantity input and an Add to Cart button."""
    for product in product_list:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.image(product["image"], width=120)
        with col2:
            st.subheader(product["name"])
            st.write(product["description"])
            st.write(f"**Price:** ${product['price']}")
            qty = st.number_input(
                "Quantity",
                min_value=0,
                max_value=5,
                value=0,
                key=f"qty_{product['name']}"
            )
        with col3:
            if st.button("Add to Cart 🛒", key=f"add_{product['name']}"):
                if qty > 0:
                    add_to_cart(product["name"], qty)
                    st.success(f"Added {qty} of {product['name']} to cart!")
                else:
                    st.warning("Please select a quantity greater than 0 to add to cart.")
        st.markdown("---")

# -----------------------------
# Filtering Products Based on Input
# -----------------------------
filtered_products = products

# Search filter
if search_term:
    filtered_products = [p for p in filtered_products if search_term.lower() in p["name"].lower()]

# Cost filter (after search filtering)
filtered_products = [p for p in filtered_products if cost_range[0] <= p["price"] <= cost_range[1]]

# Category filter
if category != "All":
    filtered_products = [p for p in filtered_products if category.lower() in p["category"].lower()]

# -----------------------------
# Top Logo and Title
# -----------------------------
# -----------------------------
# Top Logo and Title
# -----------------------------
col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    st.image("assets/logo.png", width=1000)  # Wider logo

    # Center the entire heading line block, not the text inside
    st.markdown("""
        <div style='display: flex; justify-content: center; width: 100%;'>
            <h1 style='white-space: nowrap;'>Welcome to Our E-Commerce Website</h1>
        </div>
        <div style='text-align: center;'>
            <p style='font-size: 18px;'>Explore a seamless shopping experience!</p>
        </div>
    """, unsafe_allow_html=True)


st.markdown("---")

# -----------------------------
# Navigation Tabs
# -----------------------------
tabs = st.tabs(["Home", "Today's Deal", "Customer Service", "Cart/Checkout"])

# -----------------------------
# Home Tab
# -----------------------------
with tabs[0]:
    st.subheader("🛍️ Featured Products")
    if filtered_products:
        display_products(filtered_products)
    else:
        st.warning("No products found that match your criteria.")
    st.markdown("---")
    st.subheader("💳 Secure Payment")
    st.markdown("Integrate with Stripe to process payments. [Learn More](https://stripe.com/docs)")

# -----------------------------
# Today's Deal Tab
# -----------------------------
with tabs[1]:
    st.subheader("🔥 Today's Deal")
    st.write("Grab these limited-time discounts before they're gone!")
    for dp in deal_products:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.image(dp["image"], width=120)
        with col2:
            st.subheader(dp["name"])
            st.write(dp["description"])
            st.markdown(
                f"<p><span style='color:red; font-weight:bold;'>${dp['price']}</span> <del>${dp['original_price']}</del></p>",
                unsafe_allow_html=True
            )
            qty = st.number_input(
                "Quantity",
                min_value=0,
                max_value=5,
                value=0,
                key=f"deal_qty_{dp['name']}"
            )
        with col3:
            if st.button("Add to Cart 🛒", key=f"deal_add_{dp['name']}"):
                if qty > 0:
                    add_to_cart(dp["name"], qty)
                    st.success(f"Added {qty} of {dp['name']} to cart!")
                else:
                    st.warning("Please select a quantity greater than 0 to add to cart.")
        st.markdown("---")

# -----------------------------
# Customer Service Tab
# -----------------------------
with tabs[2]:
    st.subheader("💁 Customer Service")
    st.write("How can we help you today?")
    st.markdown("""
    - **Shipping Info:** Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    - **Returns & Exchanges:** Phasellus auctor dolor at sapien accumsan, sed dignissim arcu feugiat.
    - **Warranty:** Maecenas aliquet lacinia lacus, non gravida nisi pretium quis.
    - **Contact Us:** Email us at support@ecommerce.com or call 1-800-123-4567.
    """)

# -----------------------------
# Cart/Checkout Tab
# -----------------------------
with tabs[3]:
    show_cart()

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 E-Commerce Demo. Built with ❤️ using Streamlit.</p>", unsafe_allow_html=True)
