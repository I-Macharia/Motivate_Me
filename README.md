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
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## ✨ Features

- **Basic Quote Chatbot**: Enter your thoughts, feelings, or situation and receive a relevant motivational quote
- **Advanced RAG Chatbot**: Engage in deeper conversations about motivation and personal growth
- **User-Friendly Interface**: Clean, responsive design with intuitive navigation
- **Quote Recommendation Engine**: ML-powered matching of user input to our quote database
- **Chat History**: Preservation of conversation history within sessions

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
│   │   └── model_utils.py    # Functions for model interaction
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

4. **Download required NLTK data**
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

5. **Download required Spacy model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

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
- **Machine Learning**: Scikit-learn, NLTK, Spacy
- **Data Processing**: Pandas, NumPy
- **Text Processing**: TF-IDF Vectorization
- **Model**: Support Vector Machine (SVM)
- **Visualization**: Matplotlib, WordCloud

## 🧠 Machine Learning Pipeline

1. **Data Preprocessing**
   - Text cleaning and normalization
   - Stopword removal
   - Tokenization

2. **Feature Engineering**
   - TF-IDF vectorization of quotes and authors

3. **Model Training**
   - SVM model with RBF kernel
   - Hyperparameters: C=10, gamma=1

4. **Quote Matching**
   - Process user input
   - Vector representation comparison
   - Return most relevant quote

5. **Model Storage**
   - Compressed pickle files for efficient storage
   - Separate vectorizer and model files

## 📈 Roadmap

### Q2 2025
- Complete RAG model implementation
- Launch beta version to limited users
- Implement user feedback system

### Q3 2025
- Launch mobile application
- Add user accounts and preferences
- Introduce professional subscription tier

### Q4 2025
- Launch API for developers
- Introduce enterprise solutions
- Expand language support

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

- **Email**: contact@motivateme.com
- **GitHub**: [github.com/yourusername/Motivate_Me](https://github.com/yourusername/Motivate_Me)

---

Made with ❤️ by [Your Name]

> 🚀 *"The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle."* - Steve Jobs
