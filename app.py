import streamlit as st
from dotenv import load_dotenv


load_dotenv()


def main():
    st.set_page_config(page_title="Chat with PDF",page_icon=":books:")

    st.header("Chat with Multiple PDFs :books:")

    st.text_input("Ask a question about your documents :")

    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Enter your PDFs here and click on process")
        st.button("Process")



if __name__=="__main__":
    main()