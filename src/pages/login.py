import streamlit as st
from utils.data_utils import fetch_user_details_from_nextjs


def login_page():
    st.title("Welcome to Motivate Me! 🚀")

    if 'user_id' not in st.session_state:
        st.session_state.user_id = None

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
                    st.rerun()
                else:
                    st.error("Invalid username or password")

        with tab2:
            st.subheader("Sign Up")
            new_username = st.text_input("Username", key="signup_username")
            new_password = st.text_input("Password", type="password", key="signup_password")
            email = st.text_input("Email")

            if st.button("Sign Up"):
                st.error("Sign-up functionality is handled via the Next.js app.")
    return st.session_state.user_id is not None


if __name__ == "__login__":
    login_page()
