import streamlit as st
from retrivel_augment import create_retrieval_chain, handle_query

# ========================= Streamlit UI =========================


def initialize_ui():
    """Initializes the Streamlit UI."""
    st.set_page_config(
        page_title="Formula 1 Chatbot",
        layout="centered",
        page_icon="🏎️",
    )
    st.title("🏎️ Formula 1 Chatbot")
    st.subheader("Get instant answers to your Formula 1 queries!")
    st.markdown(
        """
        <style>
        .stButton button {
            background-color: #FF5733;
            color: white;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main_ui():
    """Main Streamlit UI."""
    initialize_ui()

    # Load the RAG pipeline
    rag_chain = create_retrieval_chain()

    # Initial suggested queries
    st.markdown("### Suggested Queries")
    initial_queries = [
        "Who is the head of racing for Aston Martin’s F1 Academy team?",
        "Who is the highest-paid F1 driver?",
        "Who will be the newest driver for Ferrari?",
        "Who is the current Formula One World Driver's Champion?",
    ]

    # Display buttons for initial queries
    for query in initial_queries:
        if st.button(query):
            st.session_state["last_query"] = query

    # Input box for user queries
    user_query = st.text_input(
        "Enter your Formula 1 question:",
        value=st.session_state.get("last_query", ""),
        placeholder="Type your question here...",
    )

    # Handle the query if entered
    if user_query:
        with st.spinner("Fetching the answer..."):
            result = handle_query(rag_chain, user_query)

            # Display the result
            st.markdown(f"### Answer:\n\n{result['answer']}")
            if result["sources"]:
                st.markdown("### Sources:")
                for doc in result["sources"]:
                    st.markdown(f"- **Source**: {doc.metadata['source']}")
                    st.markdown(f"  {doc.page_content[:200]}...")


if __name__ == "__main__":
    main_ui()
