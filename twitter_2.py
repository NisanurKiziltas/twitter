import snscrape.modules.twitter as sntwitter
maxTweets = 30

#lang dili belirliyor.
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 lang:tr since:2020-01-01 until:2020-11-17').get_items()):
    if i > maxTweets:
        break
    print(tweet.content)
    print(tweet.username)
    print(tweet.date)
    print("\n")