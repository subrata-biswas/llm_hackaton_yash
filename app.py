import streamlit as st
import pandas as pd
from PIL import Image


# Function to display the User Info and Profile Upload page
def user_info_page():
    st.header("User Information and Profile Picture")

    with st.form("user_info_form", clear_on_submit=True):
        username = st.text_input("Username")
        email = st.text_input("Email")
        bio = st.text_area("Bio")
        profile_pic = st.file_uploader("Upload a profile picture", type=['png', 'jpg', 'jpeg'])

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("User Information Submitted Successfully!")
            if profile_pic is not None:
                st.image(profile_pic, caption='Uploaded Profile Picture.', use_column_width=True)


# Function to display the Chat Interface page
def chat_interface_page():
    st.header("Chat Interface")
    st.write("This is a simple chat interface.")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Go to", ["User Info and Profile Upload", "Chat Interface"])

    if app_mode == "User Info and Profile Upload":
        user_info_page()
    elif app_mode == "Chat Interface":
        chat_interface_page()


if __name__ == "__main__":
    main()
