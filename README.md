# Motivate Me 🚀

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.29.0-red.svg)](https://streamlit.io/)

> **Your daily dose of inspiration, powered by words that move you.**

Motivate Me is an AI-powered motivational quotes platform that provides personalized inspiration through interactive chatbots. The application uses machine learning to match user input with relevant quotes, creating a meaningful and motivational experience.

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technology Stack](#-technology-stack)
- [Machine Learning Pipeline](#-machine-learning-pipeline)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## ✨ Features

- **Basic Quote Chatbot**: Enter your thoughts, feelings, or situation and receive a relevant motivational quote.
- **Advanced RAG Chatbot**: Engage in deeper conversations about motivation and personal growth, powered by Retrieval-Augmented Generation (RAG).
- **User-Friendly Interface**: Clean, responsive design with intuitive navigation.
- **Quote Recommendation Engine**: ML-powered matching of user input to our quote database.
- **Chat History**: Preservation of conversation history within sessions.

## 📁 Project Structure
Okay, here's an updated README.md based on the current codebase, with a focus on the RAG chatbot and instructions for accessing gated Hugging Face models:

```markdown
# Motivate Me 🚀

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.29.0-red.svg)](https://streamlit.io/)

> **Your daily dose of inspiration, powered by words that move you.**

Motivate Me is an AI-powered motivational quotes platform that provides personalized inspiration through interactive chatbots. The application uses machine learning to match user input with relevant quotes, creating a meaningful and motivational experience.

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technology Stack](#-technology-stack)
- [Machine Learning Pipeline](#-machine-learning-pipeline)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## ✨ Features

- **Basic Quote Chatbot**: Enter your thoughts, feelings, or situation and receive a relevant motivational quote.
- **Advanced RAG Chatbot**: Engage in deeper conversations about motivation and personal growth, powered by Retrieval-Augmented Generation (RAG).
- **User-Friendly Interface**: Clean, responsive design with intuitive navigation.
- **Quote Recommendation Engine**: ML-powered matching of user input to our quote database.
- **Chat History**: Preservation of conversation history within sessions.

## 📁 Project Structure

```
my-streamlit-app/
├── src/
│   ├── app.py                # Main entry point of the Streamlit application
│   ├── models.py             # ML model definitions and training
│   ├── my_functions.py       # Core functionality and utility functions
│   ├── pages/
│   │   ├── about.py          # About page with information about the application
│   │   ├── chatbot.py        # Basic chatbot functionality
│   │   ├── main.py           # Main interface and landing page
│   │   └── rag_chatbot.py    # Advanced chatbot using RAG
│   ├── utils/
│   │   ├── chat_utils.py     # Utility functions for chatbot interactions
│   │   ├── data_utils.py     # Functions for loading and processing data
│   │   └── aimodel.py    # AI model agent for RAG
│   └── types/
│       └── index.py          # Custom types and interfaces
├── data/
│   ├── quotes_2.csv          # Dataset of quotes used by the chatbot
│   └── Tweets.csv            # Sample tweets for training/testing
├── config/
│   └── config.yaml           # Configuration settings
├── requirements.txt          # Project dependencies
├── .gitignore                # Git ignore file
├── LICENSE                   # CC0 1.0 Universal License
└── README.md                 # Project documentation
```

## 🚀 Installation


1. **Clone the repository**
    ```bash
   git clone https://github.com/yourusername/Motivate_Me.git
   cd Motivate_Me
   ```
2. **Create and activate a virtual environment**
   ```bash
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Accessing Gated Hugging Face Models (if applicable)**

   - Some models, like `mistralai/Mistral-7B-Instruct-v0.2` used in the RAG chatbot, require access to a gated repository on Hugging Face.
   - To use these models:
     1.  Request access on the [model page](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) with your Hugging Face account.
     2.  Log in to the Hugging Face CLI:
         ```bash
         huggingface-cli login
         ```
         and enter your access token.

## 💻 Usage

1. **Run the Streamlit application**
   ```bash
   streamlit run src/app.py
   ```

2. **Navigate using the sidebar**
   - **Home**: Introduction to Motivate Me
   - **Chat**: Basic quote chatbot
   - **Advanced Chat**: RAG-powered conversational chatbot
   - **About**: Information about the project

3. **Interacting with the chatbot**
   - Type your thoughts, questions, or current situation
   - Receive relevant motivational quotes with author attribution
   - Continue the conversation or clear chat history

## 🔧 Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: Scikit-learn, NLTK, Spacy, Sentence Transformers, FAISS
- **Data Processing**: Pandas, NumPy
- **Text Processing**: TF-IDF Vectorization
- **Model**: Support Vector Machine (SVM), Large Language Models (LLMs)
- **Visualization**: Matplotlib, WordCloud

## 🧠 Machine Learning Pipeline

1. **Data Preprocessing**
   - Text cleaning and normalization
   - Stopword removal
   - Tokenization

2. **Feature Engineering**
   - TF-IDF vectorization of quotes and authors
   - Sentence Embeddings (for RAG)

3. **Model Training**
   - SVM model with RBF kernel
   - Hyperparameters: C=10, gamma=1
   - LLM fine-tuning (optional)

4. **Quote Matching**
   - Process user input
   - Vector representation comparison
   - Return most relevant quote(s)

5. **Model Storage**
   - Compressed pickle files for efficient storage
   - Separate vectorizer and model files

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure to update tests as appropriate and follow the code style guidelines.

## 📄 License

This project is licensed under the Creative Commons Zero v1.0 Universal - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

Have questions or want to connect? Reach out to me on X!
- **X**: [![Follow me on X](https://img.shields.io/badge/X-Follow%20Me-blue?logo=x)](https://x.com/Enigmaticbobman)

- **GitHub**: [github.com/I-Macharia/Motivate_Me](https://github.com/I-Macharia/Motivate_Me)

---

Made with ❤️ by [Macharia]

> 🚀 *"The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle."* - Steve Jobs
```

