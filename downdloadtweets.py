import tweepy
import csv

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Function to authenticate and return the API object
def authenticate_twitter_app():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

# Function to download tweets and save them in a CSV file
def download_tweets(ticket_symbol, count):
    api = authenticate_twitter_app()
    tweets = tweepy.Cursor(api.search, q=ticket_symbol, lang="en", tweet_mode="extended").items(count)
    
    with open("tweets.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Tweet", "Username", "Date"])
        
        for tweet in tweets:
            writer.writerow([tweet.full_text, tweet.user.screen_name, tweet.created_at])

    print("Tweets downloaded and saved successfully!")

# Example usage
if __name__ == "__main__":
    ticket_symbol = "$AAPL"  # Replace with your desired ticket symbol
    tweet_count = 100  # Number of tweets to download
    
    download_tweets(ticket_symbol, tweet_count)
