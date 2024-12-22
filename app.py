import streamlit as st
import ollama
from PIL import Image
import io
import base64

st.set_page_config(
    page_title="Document OCR with Llama Vision",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Document OCR with Llama Vision")
st.write("Upload an image containing text, and I'll extract the content for you!")

def process_image(image):
    # Convert PIL Image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_bytes = img_byte_arr.getvalue()
    
    try:
        # Create the chat message with the image
        response = ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': 'Please extract and return only the text content from this image. Format it in a clear and readable way.',
                'images': [img_bytes]
            }]
        )
        return response['message']['content']
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
        return "Failed to process image. Please make sure Ollama is running and the llama3.2-vision model is installed."

# File uploader
uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    try:
        # Display the uploaded image
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Uploaded Image")
            image = Image.open(uploaded_file)
            st.image(image, use_column_width=True)
        
        with col2:
            st.subheader("Extracted Text")
            with st.spinner("Processing image..."):
                extracted_text = process_image(image)
                st.write(extracted_text)
                
                if extracted_text:
                    # Add a download button for the extracted text
                    st.download_button(
                        label="Download extracted text",
                        data=extracted_text,
                        file_name="extracted_text.txt",
                        mime="text/plain"
                    )
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")

# Add instructions and information
with st.expander("ℹ️ How to use"):
    st.write("""
    1. Make sure Ollama is running locally (`ollama serve` in terminal)
    2. Ensure you have the llama3.2-vision model installed (`ollama pull llama3.2-vision`)
    3. Click the 'Browse files' button above to upload an image
    4. Wait for the OCR processing to complete
    5. View the extracted text on the right side
    6. Download the extracted text using the download button if needed
    
    Supported image formats: PNG, JPG, JPEG
    """)

# Add footer
st.markdown("---")
st.markdown("Powered by Llama 3.2 Vision model through Ollama") 