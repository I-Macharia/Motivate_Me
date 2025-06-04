import streamlit as st
from utils.civic_pass_utils import get_civic_pass_status

def profile_page():
    st.title("User Profile")

    if 'user_id' not in st.session_state or st.session_state.user_id is None:
        st.error("You need to log in to view your profile.")
        return

    username = st.session_state.username
    st.subheader(f"Welcome, {username}!")

    civic_pass_status = get_civic_pass_status(st.session_state.user_id)
    if civic_pass_status:
        st.success("Your Civic Pass is active!")
    else:
        st.warning("Your Civic Pass is not active. Please issue a new one.")

if __name__ == "__main__":
    profile_page()