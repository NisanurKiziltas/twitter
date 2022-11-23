import snscrape.modules.twitter as sntwitter
maxTweets = 300
#nisanur yazan twitleri çek
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('nisanur+ since:2000-01-01 until:2022-11-17').get_items()): #from:@AntonioNeri_HPEhesabından 2000 ile 2020 arasındaki verileri çekiyor.
    if i>maxTweets:
        break
    print(tweet.content) #içerik
    print(tweet.username)
    print(tweet.date)
    print("\n")