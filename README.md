# QuLab - Financial News Sentiment Analyzer

## Description

This Streamlit application, **QuLab - Financial News Sentiment Analyzer**, is designed to analyze the sentiment of financial news articles. It leverages the power of FinBERT, a pre-trained language model specifically fine-tuned for financial text, to accurately determine whether the sentiment expressed in a news article is positive, negative, or neutral.

**Key Features:**

- **Financial Sentiment Analysis:** Utilizes FinBERT, a state-of-the-art model for financial sentiment analysis, ensuring high accuracy and relevance to financial contexts.
- **User-Friendly Interface:** Built with Streamlit, the application provides an intuitive and interactive user interface for easy sentiment analysis.
- **Article Input Flexibility:** Users can either input their own financial news article text or choose from a selection of pre-loaded sample articles with varying sentiments.
- **Clear Sentiment Visualization:** Presents the analysis results with a clear sentiment label (Positive, Negative, Neutral), a sentiment score indicating confidence, and a visual bar chart for easy interpretation.
- **Educational Focus:**  Provides context and explanations about sentiment analysis in finance, its importance in investment decision-making, and potential advanced applications.
- **Self-Contained Demonstration:** Includes sample news articles, making the application immediately usable without requiring external data sources.

This application serves as an educational tool to demonstrate the practical application of Natural Language Processing (NLP) in finance and provides a hands-on experience with sentiment analysis.

## Installation

To run this Streamlit application, you need to have Python installed on your system. Follow these steps to install the necessary libraries and set up the environment:

1. **Clone the repository (if applicable):**
   If you have access to the application code repository, clone it to your local machine. Otherwise, save the provided Python code as a `.py` file (e.g., `sentiment_analyzer.py`).

2. **Navigate to the project directory:**
   Open your terminal or command prompt and navigate to the directory where you saved the Python file.

3. **Create a virtual environment (recommended):**
   It is recommended to create a virtual environment to isolate project dependencies.
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`

4. **Install required libraries:**
   Use pip to install the necessary Python libraries. These are specified in the code and include Streamlit, Transformers, Matplotlib, Seaborn, and Pandas.
   ```bash
   pip install streamlit transformers matplotlib seaborn pandas
   ```
   Alternatively, you can create a `requirements.txt` file with the following content:
   ```
   streamlit
   transformers
   matplotlib
   seaborn
   pandas
   ```
   And install using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Once you have installed the required libraries, you can run the Streamlit application:

1. **Run the application:**
   In your terminal or command prompt, within the project directory and with the virtual environment activated (if used), run the Streamlit app using the following command, replacing `your_app_name.py` with the actual name of your Python file (e.g., `sentiment_analyzer.py`).
   ```bash
   streamlit run your_app_name.py
   ```

2. **Access the application in your browser:**
   Streamlit will automatically open the application in your default web browser. If it doesn't open automatically, you can access it by navigating to the URL displayed in your terminal (usually `http://localhost:8501`).

3. **Using the Sentiment Analyzer:**
   - **Article Source:** Choose between "Enter Article Text" to paste your own financial news article or "Choose Sample Article" to select from pre-defined examples.
   - **Input Article:**
     - If you selected "Enter Article Text", paste your financial news article into the text area provided.
     - If you selected "Choose Sample Article", select an article from the dropdown menu.
   - **Analyze Sentiment:** The application will automatically analyze the sentiment of the provided article upon input or selection. A loading spinner will indicate that the analysis is in progress.
   - **View Results:** The application will display:
     - **Overall Sentiment:**  The sentiment label (Positive, Negative, or Neutral).
     - **Sentiment Score:** A numerical score between 0 and 1 representing the model's confidence in the predicted sentiment.
     - **Sentiment Score Visualization:** A bar chart visually representing the sentiment score.
     - **Explanation:**  A brief explanation of the results and the significance of sentiment analysis in finance.

4. **Explore Sample Articles:** Experiment with the provided sample articles to see how the sentiment analyzer performs on different types of financial news.

5. **Analyze Custom Articles:**  Find financial news articles from online sources and paste them into the application to analyze their sentiment in real-time.

## Credits

This application is developed by **QuantUniversity** as part of the QuCreate Streamlit Lab initiative for educational purposes.

- **FinBERT Model:**  The sentiment analysis is powered by the pre-trained FinBERT model developed by Prosus AI. We acknowledge and appreciate their contribution to the NLP community.
- **Streamlit:** The application is built using Streamlit, an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.
- **Libraries:**  This application utilizes the following Python libraries: Transformers, Matplotlib, Seaborn, and Pandas. We thank the developers and maintainers of these libraries.

For more information about QuantUniversity and our educational resources, please visit [www.quantuniversity.com](https://www.quantuniversity.com).

## License

© 2025 QuantUniversity. All Rights Reserved.

This demonstration is for educational use and illustration only. Any reproduction of this demonstration requires prior written consent from QuantUniversity. For full legal documentation, please contact QuantUniversity through our website.
