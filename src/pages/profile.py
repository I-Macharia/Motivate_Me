import streamlit as st
from utils.data_utils import fetch_user_details_from_nextjs

def profile_page():
    st.title("User Profile")

    if 'user_id' not in st.session_state or st.session_state.user_id is None:
        st.error("You need to log in to view your profile.")
        return

    username = st.session_state.username
    if user_details := fetch_user_details_from_nextjs(username):
        st.subheader(f"Welcome, {username}!")
        civic_pass_status = user_details.get("civic_pass_id")
        ipfs_link = user_details.get("ipfs_hash")

        if civic_pass_status:
            st.success("Your Civic Pass is active!")
            st.markdown(f"[View Civic Pass Metadata on IPFS](https://ipfs.io/ipfs/{ipfs_link})")
        else:
            st.warning("Your Civic Pass is not active. Please issue a new one.")
    else:
        st.error("Failed to fetch user details.")

if __name__ == "__profile__":
    profile_page()
