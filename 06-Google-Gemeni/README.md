# Google-Gemeni API:

This repository contains various modules and components developed as part of the **Google Gemeni Project** under the **Gen-AI-Engineering** organization. Each module serves a unique purpose in leveraging generative AI models and enhancing capabilities across different modalities, including text processing, image recognition, embedding creation, and function calling.

## Table of Contents

1. [01-All-Models](#01-all-models)
2. [02-Text-to-Text](#02-text-to-text)
3. [03-Image-to-Text](#03-image-to-text)
4. [04-Chat-History](#04-chat-history)
5. [05-Embedding](#05-embedding)
6. [06-Function-Calling](#06-function-calling)

## Folder Structure

### 01-All-Models

This folder contains various AI models, which serve as the core of this project. It includes multiple generative and analytical models for different applications.

### 02-Text-to-Text

This module focuses on text-based input and output transformations. It includes utilities for tasks like summarization, paraphrasing, language translation, and other text-to-text model applications.

### 03-Image-to-Text

The image-to-text module enables AI to interpret images and generate textual descriptions. This module can be used for image captioning, optical character recognition (OCR), and more.

### 04-Chat-History

The chat history module stores and manages conversation logs, allowing for better context retention and improved interactive AI experiences.

### 05-Embedding

This module is used to generate embeddings for various data types, which can be applied in tasks such as semantic search, recommendation engines, and similarity-based matching.

### 06-Function-Calling

The function-calling module allows for dynamic code execution or service integration, enabling advanced interaction and functionality within AI-driven applications.

## Additional Files

- `.gitignore` - Specifies files and directories that should be ignored by Git.
- `README.md` - This document.
- `poetry.lock` - Dependency lock file for project consistency.
- `pyproject.toml` - Configuration file for managing dependencies and project settings using Poetry.

## Getting Started

To get started with this project, clone the repository:

```bash
git clone https://github.com/abdulrehman1004/Gen-AI-Engineering.git
```

Navigate to the `06-Google-Gemeni` directory and install dependencies using [Poetry](https://python-poetry.org/):

```bash
cd 06-Google-Gemeni
poetry install
```

## Usage

Each module can be executed independently. Detailed usage instructions will be provided in the individual module folders.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.
