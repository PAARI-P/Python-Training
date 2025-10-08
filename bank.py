import streamlit as st


users = {
    "Paari": {"pin": "1234", "balance": 5000},
    "Muhil": {"pin": "4321", "balance": 3000}
}


st.title("🏦 ATM Simulator")


st.sidebar.header("Login")
username = st.sidebar.text_input("Enter Username")
pin = st.sidebar.text_input("Enter PIN", type="password")

if st.sidebar.button("Login"):
    if username in users and users[username]["pin"] == pin:
        st.session_state["user"] = username
        st.success(f"Welcome, {username}!")
    else:
        st.error("Invalid username or PIN")


if "user" in st.session_state:
    user = st.session_state["user"]
    st.subheader(f"Hello, {user} 👋")
    balance = users[user]["balance"]

    option = st.selectbox("Choose an operation:", 
                          ["Check Balance", "Deposit", "Withdraw", "Logout"])

    if option == "Check Balance":
        st.info(f"Your current balance is ₹{balance}")

    elif option == "Deposit":
        amount = st.number_input("Enter amount to deposit", min_value=1)
        if st.button("Deposit"):
            users[user]["balance"] += amount
            st.success(f"Deposited ₹{amount}. New balance: ₹{users[user]['balance']}")

    elif option == "Withdraw":
        amount = st.number_input("Enter amount to withdraw", min_value=1)
        if st.button("Withdraw"):
            if amount <= users[user]["balance"]:
                users[user]["balance"] -= amount
                st.success(f"Withdrawn ₹{amount}. New balance: ₹{users[user]['balance']}")
            else:
                st.error("Insufficient balance!")

    elif option == "Logout":
        del st.session_state["user"]
        st.warning("Logged out successfully.")

else:
    st.info("Please login using the sidebar to continue.")