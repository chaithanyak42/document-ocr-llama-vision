# Document OCR with Llama Vision 📄

A powerful and user-friendly Streamlit application that performs Optical Character Recognition (OCR) using the Llama 3.2 Vision model through Ollama. This application allows users to upload images containing text and extract the content with high accuracy.

## 🌟 Features

- Clean and intuitive web interface built with Streamlit
- Support for multiple image formats (PNG, JPG, JPEG)
- Real-time text extraction from images
- Side-by-side display of original image and extracted text
- Download functionality for extracted text
- Comprehensive error handling and user feedback
- Responsive layout that works on various screen sizes

## 🔧 Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.com/download) installed on your system
- At least 8GB of VRAM for the 11B model (or 64GB for the 90B model)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/chaithanyak42/document-ocr-llama-vision.git
cd document-ocr-llama-vision
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

3. Install and start Ollama:
```bash
# Install Ollama from https://ollama.com/download

# Start the Ollama server
ollama serve
```

4. Pull the Llama 3.2 Vision model:
```bash
ollama pull llama3.2-vision
```

## 💻 Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (typically `http://localhost:8501`)

3. Use the application:
   - Click the "Browse files" button to upload an image
   - Wait for the OCR processing to complete
   - View the extracted text on the right side
   - Download the extracted text using the provided button

## 📁 Project Structure

```
document-ocr-llama-vision/
├── README.md
├── requirements.txt
└── app.py
```

## 🛠️ Technical Details

The application uses several key technologies:

- **Streamlit**: For the web interface and application framework
- **Ollama**: To interact with the Llama Vision model
- **Pillow**: For image processing and handling
- **Llama 3.2 Vision**: The underlying AI model for OCR

## ⚠️ Important Notes

- Ensure Ollama is running (`ollama serve`) before starting the application
- The quality of text extraction depends on the image quality and text clarity
- The application requires an active internet connection for the first model download
- Processing time may vary based on your system specifications and image size

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Visit the [GitHub repository](https://github.com/chaithanyak42/document-ocr-llama-vision) to contribute.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.com/) for providing the Llama Vision model
- [Streamlit](https://streamlit.io/) for the excellent web framework
- The open-source community for various dependencies used in this project

## 📧 Contact

For questions and feedback, please [open an issue](https://github.com/chaithanyak42/document-ocr-llama-vision/issues) in the GitHub repository. 