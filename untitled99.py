import streamlit as st
from PIL import Image
import numpy as np

# Customizing the app layout
st.set_page_config(page_title="Autism Detection System", page_icon=":guardsman:", layout="centered")

# Title and header
st.title("\U0001F31F Autism Detection System \U0001F31F")
st.subheader("Detect Autism in Children through Name and Image Analysis")

# Adding some styling to the page with improved color contrast
st.markdown("""
<style>
    .stApp {
        background-color: #add8e6;  /* Light Blue background */
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        font-size: 16px;
        padding: 12px;
        border-radius: 8px;
        width: 100%;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .stTextInput>div>input {
        padding: 10px;
        border-radius: 5px;
        border: 2px solid #ccc;
        font-size: 14px;
    }
    .stSubheader {
        color: black;  /* Set subheading text color to black */
        font-weight: bold;
    }
    .stFileUploader>div>label {
        color: #007bff;
    }
    .stSidebar {
        background-color: #343a40;
        color: white;
    }
    .stSidebar input {
        background-color: #444a53;
        color: white;
    }
    .stMarkdown {
        color: #333;
    }
    /* Custom heading colors */
    h1, h2 {
        color: black;  /* Set main heading text color to black */
    }
</style>
""", unsafe_allow_html=True)

# Sidebar styling and content
st.sidebar.header("User Information")
child_name = st.sidebar.text_input("Child's Name")
age = st.sidebar.number_input("Child's Age", min_value=1, max_value=18, step=1)

# Name-based classification
autistic_names = ["ali", "ahmed", "sara", "anum", "abdullah", "abeer", "areeba", "adeeba", "hafsa", "zain"]

if child_name:
    child_name_lower = child_name.strip().lower()  # Normalize the input
    if child_name_lower in autistic_names:
        st.sidebar.success(f"{child_name} is likely Autistic.")
    else:
        st.sidebar.success(f"{child_name} is likely Non-Autistic.")

# Upload image
st.subheader("Upload Image for Further Analysis:")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

# Preprocess function for the image
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize to 224x224 (adjust as needed)
    image = np.array(image)  # Convert image to numpy array
    image = image / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("")

    # Button for analysis
    if st.button("Analyze Image"):
        # Preprocess the image
        preprocessed_image = preprocess_image(image)

        # Mock prediction (Replace this with actual model prediction if available)
        prediction = np.random.rand()  # Random prediction for demonstration

        # Example result based on predicted class
        result = "Autistic" if prediction > 0.5 else "Non-Autistic"

        # Removed line that displayed the analysis result
        st.info("Note: This result is based on mock analysis. Please consult a medical professional for an accurate diagnosis.")

# Reset button functionality
if st.button("Reset"):
    st.experimental_rerun()

# Footer section
st.markdown("""
<hr>
<p style='text-align: center;'>Powered by Streamlit | Autism Detection System | 2024</p>
""", unsafe_allow_html=True)
