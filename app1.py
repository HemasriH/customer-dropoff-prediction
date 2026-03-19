import streamlit as st
import pickle

model = pickle.load(open("model1.pkl", "rb"))
scaler = pickle.load(open("scaler1.pkl", "rb"))
encoder = pickle.load(open("encoder1.pkl", "rb"))

st.set_page_config(page_title="Customer Journey Prediction", layout="centered")

st.title("E-Commerce Customer Journey Analytics")

st.write(
"""
Predict where a customer might drop in the purchase funnel and generate marketing strategies to reduce churn.
"""
)



products = {
    "Cotton T-Shirt": 733,
    "Power Bank": 1080,
    "Digital Alarm Clock": 2020,
    "Yoga Mat": 1690,
    "Bluetooth Speaker": 2500,
    "Laptop Bag": 1800,
    "Wireless Mouse": 1200,
    "Water Bottle": 600
}

st.subheader("Select Product")

product_name = st.selectbox("Product", list(products.keys()))
product_price = products[product_name]

st.write("Product Price:", product_price)



st.subheader("Customer Behaviour Inputs")

page_views = st.number_input("Page Views", 0, 20, step=1)
product_views = st.number_input("Product Views", 0, 20, step=1)
cart_adds = st.number_input("Cart Adds", 0, 10, step=1)

total_events = page_views + product_views + cart_adds

st.write("Total Events:", total_events)



if st.button("Predict Customer Drop Stage"):

    price_scaled = scaler.transform([[product_price]])[0][0]

    X = [[page_views, product_views, cart_adds, total_events, price_scaled]]

    prediction = model.predict(X)
    drop_stage = encoder.inverse_transform(prediction)[0]

    st.success(f"Predicted Drop Stage: {drop_stage}")

    if drop_stage == "Purchase":
        purchase_status = "Customer Completed Purchase"
    else:
        purchase_status = "Customer Did Not Purchase"

    st.subheader("Purchase Status")
    st.write(purchase_status)


    if drop_stage == "Add_to_Cart":
        churn_risk = "High"

    elif drop_stage == "Product_View":
        churn_risk = "Medium"

    else:
        churn_risk = "Low"

    st.subheader("Churn Risk Level")
    st.write(churn_risk)

   

    st.subheader("Recommended Marketing Strategy")

    if drop_stage == "Add_to_Cart":
        st.info("Offer discount or free shipping to encourage checkout.")

    elif drop_stage == "Product_View":
        st.info("Recommend similar or cheaper products to increase interest.")

    elif drop_stage == "Website_Visit":
        st.info("Show trending or popular products.")

    elif drop_stage == "Purchase":
        st.info("Suggest complementary products.")

    else:
        st.info("Display best-selling products.")


