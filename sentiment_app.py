import gradio as gr
from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

def get_sentiment(input_text):
    return sentiment(input_text)


# result = get_sentiment("The movie was awesome")
# result

iface = gr.Interface(fn=get_sentiment, inputs="text", outputs=['text'], title="Sentimenet Analyzer")

iface.launch()