import streamlit as st
import requests
from utils.data_utils import fetch_user_details_from_nextjs
from utils.civic_pass_utils import get_civic_pass_id

def login_page():
    st.title("Welcome to Motivate Me! 🚀")

    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
    if 'login_status' not in st.session_state:
        st.session_state.login_status = ""
    if 'username' not in st.session_state:
        st.session_state.username = ""

    def handle_civic_pass_login():
        username = "testUser"  # Replace with actual username input or token info
        # Here, you should integrate with the actual Civic Pass authentication flow.
        # For demonstration, let's assume you have a function to get the Civic Pass ID.

        civic_pass_id = get_civic_pass_id()
        if not civic_pass_id:
            st.session_state.login_status = "Failed to retrieve Civic Pass ID."
            return
        email = "test@example.com"
        try:
            response = requests.post(
                "http://localhost:3000/api/saveUser",  # API endpoint
                json={"username": username, "civicPassId": civic_pass_id, "email": email},
            )
            if response.status_code == 200:
                data = response.json()
                st.session_state.user_id = data.get("user_id")
                st.session_state.username = username
                st.session_state.login_status = "Civic Pass issued successfully!"
            else:
                st.session_state.login_status = "Failed to issue Civic Pass."
        except Exception as e:
            st.session_state.login_status = f"Error during login: {e}"

    if st.session_state.user_id is None:
        tab1, tab2 = st.tabs(["Login", "Sign Up"])

        with tab1:
            st.subheader("Login")
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")

            if st.button("Login"):
                user_details = fetch_user_details_from_nextjs(username)
                if user_details and user_details.get("username") == username:
                    st.session_state.user_id = user_details.get("user_id")
                    st.session_state.username = username
                    st.success("Login successful!")
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password")

            st.markdown("---")
            st.subheader("Or login with Civic Pass")
            if st.button("Login with Civic Pass"):
                handle_civic_pass_login()
            if st.session_state.login_status:
                st.write(st.session_state.login_status)

        with tab2:
            st.subheader("Sign Up")
            new_username = st.text_input("Username", key="signup_username")
            new_password = st.text_input("Password", type="password", key="signup_password")
            email = st.text_input("Email")

            if st.button("Sign Up"):
                try:
                    response = requests.post(
                        "http://localhost:3000/api/saveUser",
                        json={"username": new_username, "email": email},
                    )
                    if response.status_code == 200:
                        data = response.json()
                        st.session_state.user_id = data.get("user_id")
                        st.session_state.username = new_username
                        st.success("Sign up successful!")
                        st.experimental_rerun()
                    else:
                        st.error("Failed to sign up.")
                except Exception as e:
                    st.error(f"Error during sign up: {e}")
    else:
        st.success(f"Welcome back, {st.session_state.username}!")
