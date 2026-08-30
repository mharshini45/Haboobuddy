import streamlit as st
import datetime
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def setup_page():
    st.set_page_config(
        page_title="HabooBuddy",
        page_icon="🍵",
        layout="wide"
    )
    
def show_header():
    st.markdown("""
                <style>
                .block-container {
                    padding-top: 1rem;
                }
                </style>
                """,unsafe_allow_html=True)
    if "orders" not in st.session_state:
        st.session_state.orders = []
        
    st.title("HabooBuddy 🍵")
    st.caption("Your friendly coffee ordering app")
    st.image(os.path.join(BASE_DIR,"images","coffee.jpg"),width=400)
    
def recommend_coffee():
    hour=datetime.datetime.now().hour
    if hour < 11:
        suggestion="Latte -🌅 a great morning pick-up"
    elif hour < 17:
        suggestion="Mocha -☀️ a perfect afternoon refresher"
    else:
        suggestion ="Americano - 🌇 cozy evening"    
    st.info(f"💡Suggested for you : {suggestion}")    
            
def show_menu():
    st.subheader("📋 OUR MENU")
    menu={
        "Latte" : 80,
        "Hop Cold" : 120,
        "Americano" : 140,
        "Smoothie Cold" : 200,
        "Mocha" : 110
    }
    selected_coffee = st.selectbox("Choose your coffee 🍵",list(menu.keys()))
    price = menu[selected_coffee]
    st.write(f"**{selected_coffee}** - ₹{price}")
    return selected_coffee,price

def get_order_options():
    st.subheader("🛠️ Customize Your Order")
    quantity=st.slider("How many cups 🍵? ",min_value=1,max_value=10,value=1)
    size=st.radio("Choose size 📏",["Small","Medium","Large "])
    addons=st.multiselect("Add-ons ➕",["Extra-Sugar","Whipped Cream","Extra Shot","Cinnamon"])
    return quantity,size,addons

def calculate_total(price,quantity,size,addons):
    size_extra={"Small":0,"Medium":10,"Large":20}
    addon_prices={"Extra-Sugar":0,"Whipped Cream":15,"Extra Shot":20,"Cinnamon":5}
    addon_total=0
    for item in addons:
        addon_total+=addon_prices[item]
    total=(price + size_extra[size] + addon_total)*quantity
    st.metric(" Total Price",f"₹{total}")
    return total

def place_order(selected_coffee,quantity,size,total):
    if st.button("🍵 Place Order"):
        st.success(f"Order placed ! {quantity} x {size} {selected_coffee} = Total ₹{total}")
        st.balloons()
        st.session_state.orders.append({
            "coffee":selected_coffee,
            "quantity":quantity,
            "size":size,
            "total":total
        })
        
def track_orders():
    st.sidebar.subheader("📦 Order History")
    if len(st.session_state.orders)==0:
        st.sidebar.write("No orders yet 🍵")
    else:
        for order in  st.session_state.orders:
            st.sidebar.write(f"{order['quantity']} x{order['size']} {order ['coffee']} - {order ['total']}")  
             

setup_page()    
show_header()  
recommend_coffee()
selected_coffee,price=show_menu()
quantity,size,addons=get_order_options()
total=calculate_total(price,quantity,size,addons)
place_order(selected_coffee,quantity,size,total)    
track_orders()


 
