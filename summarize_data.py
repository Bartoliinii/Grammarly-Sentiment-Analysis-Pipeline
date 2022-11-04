from get_data import scrape_data
import pandas as pd
from transformers import pipeline

def summarize(df: pd.DataFrame):

    pipe = pipeline("summarization", model="facebook/bart-large-cnn",framework='pt', do_sample=False)

    for index, row in df.iterrows():
        pipe(df.at[index,"review"], max_length=6, min_length=3, do_sample=False)