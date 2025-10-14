import streamlit as st
import json
import os

DATA_FILE = "bank_data.json"

# ---------- Load & Save Functions ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                st.warning("⚠️ JSON file was empty or corrupted. Starting fresh.")
                return {}
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- Create Account ----------
def create_account(data, name, pin, balance):
    if name in data:
        st.error(f"Account for '{name}' already exists!")
        return data
    data[name] = {"account_holder": name, "pin": pin, "balance": balance}
    save_data(data)
    st.success(f"✅ Account for {name} added successfully!")
    return data

# ---------- Display Accounts ----------
def display_accounts(data):
    if not data:
        st.info("No accounts found.")
    else:
        st.subheader("🏦 All Bank Accounts")
        for account in data.values():
            st.write(f"**Name:** {account['account_holder']}")
            st.write(f"**PIN:** {account['pin']}")
            st.write(f"**Balance:** ₹{account['balance']}")
            st.markdown("---")

# ---------- Update Account ----------
def update_account(data, name, new_pin=None, new_balance=None):
    if name not in data:
        st.error(f"Account for '{name}' does not exist!")
        return data
    if new_pin:
        data[name]['pin'] = new_pin
        st.success(f"🔒 PIN updated for {name}")
    if new_balance is not None:
        data[name]['balance'] = new_balance
        st.success(f"💰 Balance updated for {name}")
    save_data(data)
    return data

# ---------- Delete Account ----------
def delete_account(data, name):
    if name not in data:
        st.error(f"Account for '{name}' does not exist!")
        return data
    del data[name]
    save_data(data)
    st.success(f"🗑️ Account '{name}' deleted successfully!")
    return data

# ---------- Streamlit UI ----------
def main():
    st.set_page_config(page_title="Bank Account Manager", page_icon="🏦")
    st.title("🏦 Bank Account Manager")

    # Load data
    data = load_data()

    # Sidebar Menu
    menu = ["Create Account", "View Accounts", "Update Account", "Delete Account"]
    choice = st.sidebar.radio("Menu", menu)

    # -------- CREATE ACCOUNT --------
    if choice == "Create Account":
        st.subheader("➕ Create New Account")
        name = st.text_input("Account Holder Name")
        pin = st.text_input("4-digit PIN", type="password", max_chars=4)
        balance = st.number_input("Initial Balance (₹)", min_value=0.0, step=100.0)
        if st.button("Create Account"):
            if name and pin:
                data = create_account(data, name, pin, balance)
            else:
                st.warning("Please enter both name and PIN!")

    # -------- VIEW ACCOUNTS --------
    elif choice == "View Accounts":
        st.subheader("📋 All Bank Accounts")
        display_accounts(data)

    # -------- UPDATE ACCOUNT --------
    elif choice == "Update Account":
        st.subheader("✏️ Update Account")
        name = st.text_input("Enter Account Holder Name to Update")
        if name:
            update_option = st.radio("What do you want to update?", ["PIN", "Balance"])
            if update_option == "PIN":
                new_pin = st.text_input("Enter New 4-digit PIN", type="password", max_chars=4)
                if st.button("Update PIN"):
                    if new_pin:
                        data = update_account(data, name, new_pin=new_pin)
                    else:
                        st.warning("Please enter a new PIN.")
            elif update_option == "Balance":
                new_balance = st.number_input("Enter New Balance (₹)", min_value=0.0, step=100.0)
                if st.button("Update Balance"):
                    data = update_account(data, name, new_balance=new_balance)

    # -------- DELETE ACCOUNT --------
    elif choice == "Delete Account":
        st.subheader("🗑️ Delete Account")
        name = st.text_input("Enter Account Holder Name to Delete")
        if st.button("Delete Account"):
            if name:
                data = delete_account(data, name)
            else:
                st.warning("Please enter an account holder name.")

if __name__ == "__main__":
    main()
