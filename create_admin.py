import requests

# ==============================
# CONFIGURATION
# ==============================
API_BASE = "https://your-backend-service.onrender.com/api"  # 🔧 Replace with your backend URL
ADMIN_NAME = "Admin User"
ADMIN_EMAIL = "admin@flashworks.com"
ADMIN_PASSWORD = "Admin123"

# ==============================
# CREATE ADMIN FUNCTION
# ==============================
def create_admin():
    url = f"{API_BASE}/auth/register"
    payload = {
        "name": ADMIN_NAME,
        "email": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD,
        "role": "admin"
    }

    print(f"📡 Sending request to {url} ...")

    try:
        response = requests.post(url, json=payload, timeout=10)

        # Success
        if response.status_code in (200, 201):
            print("✅ Admin account created successfully!")
            print("Login credentials:")
            print(f"  Email: {ADMIN_EMAIL}")
            print(f"  Password: {ADMIN_PASSWORD}")

        # Already exists
        elif response.status_code == 409:
            print("⚠️ Admin account already exists. Attempting to login...")

            # Attempt to login and get token
            login_payload = {"email": ADMIN_EMAIL, "password": ADMIN_PASSWORD}
            login_res = requests.post(f"{API_BASE}/auth/login", json=login_payload, timeout=10)
            if login_res.status_code == 200:
                token = login_res.json().get("token")
                print("✅ Logged in successfully!")
                print(f"Access Token: {token}")
            else:
                print(f"❌ Login failed. Status: {login_res.status_code}, Response: {login_res.text}")

        # Other errors
        else:
            print(f"❌ Failed to create admin. Status: {response.status_code}")
            try:
                print("Response:", response.json())
            except Exception:
                print("Response text:", response.text)

    except requests.exceptions.RequestException as e:
        print("🚨 Connection error:", e)


# ==============================
# RUN SCRIPT
# ==============================
if __name__ == "__main__":
