# Install required libraries
!pip install gradio vaderSentiment pandas plotly nltk -q

# Clone the GitHub repository
!git clone https://github.com/sudhir-voleti/sentiGradio.git
%cd sentiGradio

# Install additional dependencies if specified in requirements.txt (optional)
# !pip install -r requirements.txt -q

# Ensure NLTK resources are downloaded
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

# Launch the Gradio app directly
import gradio as gr
from importlib import import_module
import socket
import time

def find_free_port(start_port, end_port):
    """Find a free port in the given range."""
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("0.0.0.0", port))
                return port
            except OSError:
                continue
    raise RuntimeError(f"No free ports found in range {start_port}-{end_port}")

try:
    # Import the app module
    app_module = import_module('app')
    # Access the demo object (named 'demo' in app.py)
    demo = app_module.demo

    # Find a free port in the range 7860-7870
    free_port = find_free_port(7860, 7870)
    print(f"Using free port: {free_port}")

    # Launch with share=True and the found free port
    demo.launch(share=True, inline=False, server_port=free_port)
    print("Gradio app is running. Click the URL above to open it.")
except AttributeError:
    print("Error: 'demo' object not found in app.py. Ensure the Gradio Blocks object is named 'demo'.")
except RuntimeError as e:
    print(f"Error finding free port: {str(e)}")
except Exception as e:
    print(f"Error launching app: {str(e)}")

# Keep the cell running to maintain the app
while True:
    time.sleep(10)
