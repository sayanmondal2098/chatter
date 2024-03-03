# Generative Model for Blog and Text Generation

This repository contains a generative model that can be used to generate blog posts and text. The model used in this project is the Llama-GGML model, which is a powerful language model for generating high-quality text.

## Model Details

- Model Type: Llama-GGML
- Model URL: [https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)

## Getting Started

To get started with this generative model, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Load the Llama-GGML model using the provided model URL.
4. Use the model to generate blog posts and text.

## Example Usage

### Generate Text
To generate a small chunk of text using the Llama-GGML model, you can use the `chat.ipynb` notebook in the repository. This notebook provides an interactive interface where you can input a prompt and the model will generate a response.

### Generate Blog
To generate a blog using the Llama-GGML model with a Streamlit interface, you can use the `blog.py` script in the repository. This script provides a user-friendly interface where you can input the desired title and content length, and the model will generate a blog post accordingly.

TO run this
```bash 
streamlit run blog.py
```

Make sure you have the Llama-GGML model downloaded and loaded before running the `chat.ipynb` notebook or the `blog.py` script. You can download the model from the provided model URL in the Model Details section of the readme.

Happy generating!

## Folder Structure

Here is the current folder structure of the project:
- /chatter
    - models
        - downloaded model bin files
    - venv
        - Enviroment Specefic Files
    - readme.md
    - chat.ipynb
    - blog.py
    - .gitignore
    - requirement.txt
