import streamlit as st


def main():
    st.title('File Upload and Display App')

    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx', 'txt', 'pdf', 'png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)

        # Display the content of the file
        if uploaded_file.type == "text/csv" or uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            # For CSV or Excel file
            df = pd.read_csv(uploaded_file)
            st.dataframe(df)
        elif uploaded_file.type == "text/plain":
            # For text file
            text = str(uploaded_file.read(), "utf-8")
            st.text(text)
        elif uploaded_file.type == "application/pdf":
            # For PDF file
            st.write("PDF file cannot be displayed directly. Please download the file to view.")
        elif uploaded_file.type in ["image/png", "image/jpeg", "image/jpg"]:
            # For images
            st.image(uploaded_file.read(), caption='Uploaded Image.', use_column_width=True)
        else:
            st.write("This file type is not supported for display")


if __name__ == "__main__":
    main()
