import streamlit as st
import pandas as pd
from PIL import Image
import user_info
import llm

def extract_user_info(lines):
    st.write("user_name", lines[0].strip().decode('utf-8'))
    st.session_state.user_name = lines[0].strip().decode('utf-8')
    st.write("user_birthdate", lines[1].strip().decode('utf-8'))
    st.session_state.user_birthdate = lines[1].strip().decode('utf-8')
    st.write("user_height", lines[2].strip().decode('utf-8'))
    st.session_state.user_height = lines[2].strip().decode('utf-8')
    st.write("user_weight", lines[3].strip().decode('utf-8'))
    st.session_state.user_weight = lines[3].strip().decode('utf-8')
    st.write("user_daily_calorie_intake", lines[4].strip().decode('utf-8'))
    st.session_state.user_daily_calorie_intake = lines[4].strip().decode('utf-8')
    st.write("user_daily_calorie_burn", lines[5].strip().decode('utf-8'))
    st.session_state.user_daily_calorie_burn = lines[5].strip().decode('utf-8')

def set_user_info(prompt, user_info):
    user_info.set_user_name(st.session_state.get("user_name"))
    user_info.set_user_birthdate(st.session_state.get("user_birthdate"))
    user_info.set_user_height(st.session_state.get("user_height"))
    user_info.set_user_weight(st.session_state.get("user_weight"))
    user_info.set_user_daily_calorie_intake(st.session_state.get("user_daily_calorie_intake"))
    user_info.set_user_daily_calorie_burn(st.session_state.get("user_daily_calorie_burn"))
    user_info.add_user_question(prompt)


# Function to display the User Info and Profile Upload page
def user_info_page():
    st.header("User Information and Profile Picture")

    with st.form("user_info_form", clear_on_submit=True):
        username = st.text_input("Username")
        email = st.text_input("Email")
        bio = st.text_area("Bio")
        profile_pic = st.file_uploader("Upload a profile picture", type=['png', 'jpg', 'jpeg'])
        submitted = st.form_submit_button("Submit Profile photo")
        if submitted:
            st.success("User Information Submitted Successfully!")
            if profile_pic is not None:
                st.image(profile_pic, caption='Uploaded Profile Picture.', use_column_width=True)

        user_info_file = st.file_uploader("Upload user info", type=['xml', 'json', 'csv', 'txt'])
        submitted = st.form_submit_button("Submit User Info")
        if submitted:
            st.success("User Information Submitted Successfully!")
            if user_info_file is not None:
                lines = user_info_file.readlines()
                if lines is not None:
                    extract_user_info(lines)

# Function to display the Chat Interface page
def chat_interface_page(user_info):
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

        set_user_info(prompt, user_info)

        response = f"{llm.llm(user_info.populate_user_info())}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Go to", ["User Info and Profile Upload", "Chat Interface"])

    user = user_info.UserInfo(1)
    if app_mode == "User Info and Profile Upload":
        user_info_page()
    elif app_mode == "Chat Interface":
        chat_interface_page(user)



if __name__ == "__main__":
    main()
