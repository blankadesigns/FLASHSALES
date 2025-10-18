import streamlit as st
import requests
import pandas as pd

# ==============================
# CONFIG
# ==============================
API_BASE = "https://your-backend-service.onrender.com/api"  # <-- Replace with your Render backend URL

st.set_page_config(page_title="Marketplace Admin Dashboard", layout="wide")

# ==============================
# SIDEBAR LOGIN
# ==============================
st.sidebar.title("🔑 Admin Login")
admin_email = st.sidebar.text_input("Email")
admin_password = st.sidebar.text_input("Password", type="password")
login_button = st.sidebar.button("Login")

# Store token in session
if "token" not in st.session_state:
    st.session_state["token"] = None

if login_button:
    try:
        res = requests.post(
            f"{API_BASE}/auth/login",
            json={"email": admin_email, "password": admin_password},
            timeout=10
        )
        if res.status_code == 200:
            st.session_state["token"] = res.json().get("token")
            st.sidebar.success("✅ Logged in successfully!")
        else:
            st.sidebar.error("❌ Invalid credentials or login failed")
    except requests.exceptions.RequestException as e:
        st.sidebar.error(f"Connection error: {e}")

# ==============================
# MAIN DASHBOARD
# ==============================
if st.session_state["token"]:
    headers = {"Authorization": f"Bearer {st.session_state['token']}"}

    st.title("📊 Marketplace Admin Dashboard")
    tabs = st.tabs(["🏠 Listings", "👥 Users"])

    # ---------- LISTINGS TAB ----------
    with tabs[0]:
        st.subheader("All Listings")
        try:
            r = requests.get(f"{API_BASE}/listings", headers=headers, timeout=10)
            if r.status_code == 200:
                listings_data = r.json()
                if isinstance(listings_data, list) and len(listings_data) > 0:
                    df_listings = pd.DataFrame(listings_data)
                    search = st.text_input("🔍 Search listings by title")
                    if search:
                        df_listings = df_listings[df_listings["title"].str.contains(search, case=False, na=False)]
                    st.dataframe(df_listings)
                else:
                    st.info("No listings found.")
            else:
                st.warning(f"Failed to fetch listings (Status {r.status_code})")
        except requests.exceptions.RequestException as e:
            st.error(f"Error loading listings: {e}")

    # ---------- USERS TAB ----------
    with tabs[1]:
        st.subheader("Registered Users")
        try:
            u = requests.get(f"{API_BASE}/users", headers=headers, timeout=10)
            if u.status_code == 200:
                users_data = u.json()
                if isinstance(users_data, list) and len(users_data) > 0:
                    df_users = pd.DataFrame(users_data)
                    st.dataframe(df_users)
                else:
                    st.info("No users found.")
            else:
                st.warning(f"Failed to fetch users (Status {u.status_code})")
        except requests.exceptions.RequestException as e:
            st.error(f"Error loading users: {e}")

else:
    st.info("Please log in using your admin credentials to view the dashboard.")
