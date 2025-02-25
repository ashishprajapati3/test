# streamlit_app.py

import streamlit as st

# Title of the app
st.title("My Basic Streamlit App")

# Display some text
st.text("This is a basic example of using Streamlit for creating web apps!")

# Add a header
st.header("Streamlit Functions Demonstration")

# Display some text with markdown
st.markdown("You can also use **Markdown** to style your text!")

# Add an interactive widget: Button
if st.button("Say Hello"):
    st.write("Hello, Streamlit!")

# Create a simple input form with text input
name = st.text_input("Enter your name:", "Your Name Here")

# Display the entered name
st.write(f"Hello, {name}!")

# Add a slider to select a number
number = st.slider("Select a number", 0, 100, 50)

# Display the selected number
st.write(f"You selected: {number}")

