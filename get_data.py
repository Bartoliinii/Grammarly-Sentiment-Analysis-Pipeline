from google_play_scraper import Sort, reviews
import pandas as pd
import argparse

def get_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-c","--country",type=str,required=True,help="Select country in which you would like to have reviews")
    ap.add_argument("-a","--ammount",type=int,required=True,help="Ammount of reviews")
    return vars(ap.parse_args())

def google_play(country: str = 'us', ammount: int = 1000, max_score: int = 3):

    if len(country) != 2:
        raise ValueError("Country index contains only 2 characters")
    max_score += 1
    ammount = abs(int(ammount/5))
    
    text_reviews = []
    print("------running scraping algorithm------")
    for i in range(1,max_score):
        result,_ = reviews(
        'com.grammarly.android.keyboard',
        lang='en',
        country=country,
        sort=Sort.NEWEST,
        count=ammount,
        filter_score_with=i
        )    
        [text_reviews.append((review["userName"],review["content"],review["thumbsUpCount"],i)) for review in result]

    return text_reviews



def scrape_data(country: str, ammount: int, max_score: int):
    print("------recieved data------")

    reviews = google_play(country, ammount, max_score)

    df = pd.DataFrame(reviews, columns=["user_name","review","thumbs_up_count","raiting"])
    return df