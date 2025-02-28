import streamlit as st
from transformers import pipeline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.set_page_config(page_title="QuCreate Streamlit Lab - Financial News Sentiment Analyzer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab - Financial News Sentiment Analyzer")
st.divider()

# Initialize sentiment analysis pipeline with FinBERT
@st.cache_resource
def load_sentiment_pipeline():
    """
    Loads the FinBERT sentiment analysis pipeline.
    Utilizes st.cache_resource to load the model only once, improving app performance.
    """
    try:
        sentiment_pipeline = pipeline("sentiment-analysis", model="ProsusAI/finbert")
        return sentiment_pipeline
    except Exception as e:
        st.error(f"Error loading sentiment analysis model: {e}")
        return None

sentiment_analyzer = load_sentiment_pipeline()

if sentiment_analyzer:
    st.header("Financial News Sentiment Analysis", divider='blue')
    st.write(
        """
        This application analyzes the sentiment of financial news articles using a pre-trained FinBERT model. 
        FinBERT is specifically trained on financial text data, making it highly effective for financial sentiment analysis. 
        **Learning Outcomes:**
        - Understand how sentiment analysis can be applied to financial news.
        - Visualize sentiment scores and interpret their meaning.
        - Interact with the application by inputting your own news articles and observing real-time sentiment changes.
        """
    )

    # Sample News Articles (Self-sufficient dataset)
    sample_articles = {
        "Positive News": "Stocks soared to new heights today as investors cheered strong earnings reports and positive economic data. The Dow Jones Industrial Average jumped 300 points, while the S&P 500 and Nasdaq Composite also recorded significant gains.",
        "Neutral News": "The Federal Reserve announced today that it would hold interest rates steady, citing moderate economic growth and stable inflation. The central bank will continue to monitor economic conditions and is prepared to adjust policy as needed.",
        "Negative News": "Market plunged sharply today amid concerns over rising inflation and potential interest rate hikes. The Dow Jones Industrial Average tumbled 500 points, with technology stocks leading the decline. Investors are worried about the impact of higher rates on corporate earnings.",
        "Mixed News": "Economic data released today painted a mixed picture of the economy. While the unemployment rate fell to a new low, inflation remained stubbornly high. Analysts are divided on whether the Federal Reserve will need to take more aggressive action to combat inflation."
    }

    article_source = st.radio("Select Article Source:", ["Enter Article Text", "Choose Sample Article"], index=0, horizontal=True)

    if article_source == "Enter Article Text":
        news_article_input = st.text_area("Enter Financial News Article:", height=200, placeholder="Paste your news article here...")
        if not news_article_input:
            st.info("Enter or paste a financial news article in the text area above to analyze its sentiment.")
    else:
        sample_article_name = st.selectbox("Choose a Sample Article:", list(sample_articles.keys()), index=0)
        news_article_input = sample_articles[sample_article_name]
        st.info(f"You have selected the sample article: **{sample_article_name}**.")

    if news_article_input:
        with st.spinner("Analyzing sentiment..."):
            sentiment_result = sentiment_analyzer(news_article_input)

        st.subheader("Sentiment Analysis Results:", divider='green')

        sentiment_label = sentiment_result[0]['label']
        sentiment_score = sentiment_result[0]['score']

        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Overall Sentiment", value=sentiment_label.capitalize())
        with col2:
            st.metric(label="Sentiment Score", value=f"{sentiment_score:.4f}")

        st.info(f"**Explanation:** The sentiment analysis model has determined the overall sentiment of the article to be **{sentiment_label.lower()}**. "
                f"The sentiment score ranges from 0 to 1, with higher scores indicating a stronger confidence in the predicted sentiment. "
                f"In this case, a score of **{sentiment_score:.4f}** suggests the model's confidence level.")

        # Visualization of Sentiment Score
        st.subheader("Sentiment Score Visualization", divider='green')
        st.write("The bar chart below visually represents the sentiment score. A higher bar indicates a stronger sentiment.")

        sentiment_data = pd.DataFrame({
            'Sentiment': [sentiment_label.capitalize()],
            'Score': [sentiment_score]
        })

        fig_bar, ax_bar = plt.subplots(figsize=(6, 4))
        sns.barplot(x='Sentiment', y='Score', data=sentiment_data, palette={"Positive": " Greens_d", "Negative": "Reds_d", "Neutral": "Blues_d"}, ax=ax_bar)
        ax_bar.set_title('Sentiment Score Distribution')
        ax_bar.set_ylabel('Sentiment Score')
        ax_bar.set_ylim([0, 1]) # Set y-axis limit from 0 to 1 for score
        st.pyplot(fig_bar)

        st.write(
            """
            **Understanding Sentiment Analysis in Finance:**
            Sentiment analysis is crucial in finance as it helps in quantifying market sentiment from news, social media, and other textual data. 
            By understanding the sentiment polarity (positive, negative, neutral), investors can gain insights into market trends and make informed decisions. 
            For example, consistently positive news sentiment about a company or sector might indicate a potential investment opportunity, while negative sentiment could signal risks.

            This application demonstrates a basic application of sentiment analysis. More advanced applications may involve:
            - **Time-series sentiment analysis:** Tracking sentiment changes over time to identify trends.
            - **Granular sentiment analysis:** Analyzing sentiment at a sentence or phrase level to understand nuances.
            - **Integration with market data:** Correlating sentiment scores with stock prices and other market indicators to build predictive models.

            **Reference:** This application is inspired by the concepts discussed in the document "Advances in Natural Language Understanding for Investment Management," particularly page 10, which highlights the significance of sentiment analysis in financial markets.
            """
        )

else:
    st.error("Sentiment analysis model failed to load. Please check the logs for more details.")

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
