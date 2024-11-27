import streamlit as st
import sys
import os

# Add the parent directory to Python path to import from core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.methods import greet


def main():
    st.set_page_config(page_title="Streamlit App", layout="wide")

    st.title("Core")

    # Example of using a method from core
    message = greet("User")
    st.write(message)

    # Display environment variables
    st.subheader("Environment Variables")
    graph_server_url = os.getenv("GRAPH_SERVER_URL", "Not set")
    st.write(f"Graph Server URL: {graph_server_url}")


if __name__ == "__main__":
    main()
