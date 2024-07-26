import streamlit as st
import login
import home

def main():
    if "login_state" not in st.session_state:
        st.session_state.login_state = False

    if st.session_state.login_state:
        # Sidebar for page navigation
        st.sidebar.title("Navigation")
        page = st.sidebar.selectbox("Select a Page", ["Home"], key="page_select")

        # Display selected page content
        if page == "Home":
            home.main()

        # Logout button in the sidebar
        st.sidebar.markdown("---")  # Optional separator line for better visual separation
        if st.sidebar.button("Logout", key="logout_button_main"):
            st.session_state.login_state = False
            st.session_state.login_successful = False
            st.session_state.message = ""
            st.session_state.login_inputs = {"email": "", "password": ""}
            st.session_state.user_data = {}  # Clear user data
            st.experimental_rerun()
    else:
        login.main()

if __name__ == "__main__":
    main()
