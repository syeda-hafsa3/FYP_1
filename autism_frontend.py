import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# Load the pre-trained model (replace 'model.h5' with your model file)
model = tf.keras.models.load_model('D:/HAFSA Workspace/7th Semester/FYP/autism_detection_model (1).h5')


# Customizing the app layout
st.set_page_config(page_title="Autism Detection System", page_icon=":guardsman:", layout="centered")

# Title and header
st.title("🌟 Autism Detection System 🌟")
st.subheader("Detect Autism in Children through Image Analysis")

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

# Upload image
st.subheader("Upload Image for Analysis:")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

# Preprocess function for the image
def preprocess_image(image):
    # Resize and normalize the image as per the model's requirement
    image = image.resize((224, 224))  # Example: resize to 224x224 (adjust as needed)
    image = np.array(image)  # Convert image to numpy array
    image = image / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("")

    # Button for analysis
    if st.button("Analyze"):
        st.write("Running Analysis...")
        
        # Preprocess the image
        preprocessed_image = preprocess_image(image)

        # Perform prediction using the model
        prediction = model.predict(preprocessed_image)

        # Example result based on predicted class (adjust this as per your model's output)
        # Assuming the model predicts 0 for Non-Autistic and 1 for Autistic
        result = "Autistic" if prediction[0] > 0.5 else "Non-Autistic"
        
        st.success(f"Analysis Complete! The child is likely {result}.")
        st.info("Note: This result is based on model analysis. Please consult a medical professional for an accurate diagnosis.")

else:
    st.write("Please upload an image to start the analysis.")

# Reset button functionality
if st.button("Reset"):
    st.experimental_rerun()

# Footer section
st.markdown("""
<hr>
<p style='text-align: center;'>Powered by Streamlit | Autism Detection System | 2024</p>
""", unsafe_allow_html=True)
