from app_store_scraper import AppStore
import argparse

def get_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-c","--country",type=str,required=True,help="Select country in which you would like to have reviews")
    ap.add_argument("-a","--ammount"type=int,required=True,help="Ammount of reviews")
    return vars(ap.parse_args())

def main(args):
    country = args["country"]
    ammount = args["ammount"]

    AppStore(country="us", app_name="Grammarly: Writing App")

if __name__=='__main__':
