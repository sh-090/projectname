import streamlit as st

# Display a simple 'Hello World' message
#st.title('Hello, Streamlit!')
#st.write('Welcome to your first Streamlit app!')
# Access the secret
api_key = st.secrets["general"]["api_key"]

# Display it (for demonstration purposes, don't show real API keys in production)
st.write(f"My API key is: {api_key}")