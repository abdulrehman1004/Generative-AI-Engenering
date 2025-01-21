import streamlit as st
from chatbot import query_gemini

# Set Page Configuration
st.set_page_config(
    page_title="Health FAQ Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar Configuration
with st.sidebar:
    st.title("Health FAQ Chatbot 🤖")
    st.write("Welcome to the Health FAQ Chatbot. Ask any health-related question, and I'll provide an answer!")
    st.markdown("---")
    st.subheader("Connect with Me")
    st.markdown("- **Twitter**: AbdulReehman104")
    st.markdown("- **Threads**: @abdul_rehman_104")
    st.markdown("- **Instagram**: abdul_rehman_104")
    st.markdown("- **Facebook**: AbdulRehman1104")
    st.markdown("- **LinkedIn**: AbdulRehman104")
    st.markdown("---")
    st.caption("Built with ❤️ by Abdul Rehman.")


# Main Content Area Styles
st.markdown(
    """
    <style>
    .stTextInput > div > label {
        font-size: 1.2rem;
        font-weight: bold;
        color: #333;
    }
    .stButton > button {
        font-size: 1.1rem;
        padding: 0.6rem 2rem;
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 5px;
        transition: 0.3s ease;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    .stSuccess {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #d4d4d4;
        font-size: 1.1rem;
        color: #333;
    }
    .spinner {
        background-color: white;
        color: black;
        font-size: 1rem;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e1e4e8;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.title("Welcome to the Health FAQ Chatbot 🤖")
st.markdown(
    """
    ### How It Works:
    - Enter your health-related question in the text box below.
    - Press the **Ask** button to get an instant answer powered by Gemini 20.
    - View the response in a user-friendly format.
    """
)
st.markdown("---")

# Input Section
st.subheader("Ask Your Question Below")
user_query = st.text_input("Enter your question:")

# Process Query
if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Fetching response..."):
            st.markdown(
                """
                <div class="spinner">
                <strong>Processing your query, please wait...</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )
            response = query_gemini(user_query)
            st.success("Response:")
            st.markdown(
                f"""
                <div class="stSuccess">
                {response}
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.error("Please enter a valid query!")

# Footer
st.markdown("---")
st.markdown(
    """
    <footer style="text-align: center; font-size: 0.9rem; margin-top: 2rem;">
    <p>© 2024 Health FAQ Chatbot | Built with ❤️ and powered by <strong>Gemini 20</strong>.</p>
    </footer>
    """,
    unsafe_allow_html=True,
)
