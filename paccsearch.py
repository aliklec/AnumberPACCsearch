import streamlit as st

# Add custom CSS for background image
st.markdown("""
<style>
    .stApp {
        background-image: url("https://img.freepik.com/free-vector/frame-with-dogs-vector-white-background_53876-127700.jpg?t=st=1741231042~exp=1741234642~hmac=971d3746fe733776e312819c2bd8c9f233ca7c2831693d51ef0ccb14ef09cab5&w=1060"); /* Replace with your image URL */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Increase font size of the input label */
    h3 {
        font-size: 24px;
        font-weight: bold;
        color: white; /* Adjust text color for better contrast */
    }

    /* Make the text input field white */
    input[type="text"] {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
        padding: 8px;
        border-radius: 5px;
    }

    /* Center the link */
    .centered-link {
        text-align: center;
        display: block;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* CSS for wider iframe */
    .iframe-container {
        position: relative;
        width: 180%;
        left: -40%;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Streamlit UI elements
st.title("Search PACC Animals by A Number")

# Display the input label separately in larger text
st.markdown("<h3>Enter A Number Below</h3>", unsafe_allow_html=True)

# Use a form to capture the Enter key press
with st.form(key='search_form'):
    search_id = st.text_input("")
    submit_button = st.form_submit_button(label='Search')

# Process form submission (triggered by either Enter key or Search button)
if submit_button:
    if search_id:
        
        formatted_id = search_id.capitalize()
        
        # Construct the URL using the entered ID
        url = f"https://24petconnect.com/PimaAdoptablePets/Details/PIMA/{formatted_id}"
        
        # Display the centered link with custom font size
        st.markdown(f'<div class="centered-link"><a href="{url}" target="_blank" style="font-size: 24px; font-weight: bold;">Click here to view animal details</a></div>', unsafe_allow_html=True)
        
        # Embed the webpage in an iframe
        st.markdown(f"""
        <div class="iframe-container">
            <iframe src="{url}" width="100%" height="1200" frameborder="0" style="border: 1px solid #ddd;"></iframe>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Please enter A Number.")
