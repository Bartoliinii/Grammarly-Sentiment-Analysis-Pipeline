from google_play_scraper import Sort, reviews
import argparse

def get_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-c","--country",type=str,required=True,help="Select country in which you would like to have reviews")
    ap.add_argument("-a","--ammount"type=int,required=True,help="Ammount of reviews")
    return vars(ap.parse_args())

def google_play(country: str = 'us', ammount: int = 1000):
    if len(country) != 2:
        raise ValueError("Country index contains only 2 characters")

    ammount = abs(int(ammount/3))
    
    text_reviews = []
    for i in range(1,4):
        result,_ = reviews(
        'com.grammarly.android.keyboard',
        lang='en',
        country=country,
        sort=Sort.NEWEST,
        count=ammount,
        filter_score_with=i
        )
        
    [text_reviews.append((review["userName"],review["content"],review["thumbsUpCount"])) for review in result]
    return text_reviews



def main(args):
    country = args["country"]
    ammount = args["ammount"]

    reviews = google_play(country, ammount)
    

if __name__=='__main__':
    args = get_args()
    main(args)
