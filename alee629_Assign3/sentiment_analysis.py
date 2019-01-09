#Assignment 3: Sentiment Analysis
#Andrea Lee 250836721

def create_list(tweet_filename, keyword_filename): #function to open files and create lists

    tweet_file = open(tweet_filename, 'r', encoding='utf‐8') #open tweet file
    tweet_list = tweet_file.readlines() #read tweet file and create list of tweets

    keyword_file = open(keyword_filename, 'r', encoding='utf‐8') #open keyword file
    keyword_list = keyword_file.readlines() #read keyword file and create list of (keyword, value)

    tweet = []
    keyword = []
    value = []

    for single_tweet in tweet_list:
        single_tweet_list = single_tweet.split() #split each tweet in list of tweets
        tweet.append(single_tweet_list) #create list of words for each tweet in list of tweets

    for word in keyword_list:
        word_list = word.split(',') #split each (keyword, value) in keyword list
        keyword.append(word_list[0]) #create separate list for keywords
        value.append(int(word_list[1])) #create separate list for values

    return tweet, keyword, value #return list of tweets, keyword list and value list


def region_tweet(tweet_filename, keyword_filename): #function to determine region of tweet

    tweet, keyword, value = create_list(tweet_filename, keyword_filename) #call create_list function to get tweet, keyword and value lists

    p1 = [49.189787, -67.444574]
    p2 = [24.660845, -67.444574]
    p3 = [49.189787, -87.518395]
    p4 = [24.660845, -87.518395]
    p5 = [49.189787, -101.998892]
    p6 = [24.660845, -101.998892]
    p7 = [49.189787, -115.236428]
    p8 = [24.660845, -115.236428]
    p9 = [49.189787, -125.242264]
    p10 = [24.660845, -125.242264]

    eastern = []
    central = []
    mountain = []
    pacific = []

    punctuation = '!@#$%^&*()_=+`~[]{}\|:;\'\",.<>/?'

    for single_tweet in tweet:
        latitude = float(single_tweet[0].strip(punctuation)) #strip punctuation from latitude number and change to float
        longitude = float(single_tweet[1].strip(punctuation)) #strip punctuation from longitude number and change to float
        if p1[0] > latitude > p2[0] and p1[1] > longitude > p3[1]: #determine which tweets are in eastern region
            eastern.append(single_tweet) #create list of eastern region tweets
        elif p1[0] > latitude > p2[0] and p3[1] > longitude > p5[1]: #determine which tweets are in central region
            central.append(single_tweet) #create list of central region tweets
        elif p1[0] > latitude > p2[0] and p5[1] > longitude > p7[1]: #determine which tweets are in mountain region
            mountain.append(single_tweet) #create list of mountain region tweets
        elif p1[0] > latitude > p2[0] and p7[1] > longitude > p9[1]: #determine which tweets are in pacific region
            pacific.append(single_tweet) #create list of pacific region tweets

    return eastern, central, mountain, pacific #return list of tweets for each region


def region_score(tweet_filename, keyword_filename, region): #function to determine happiness score for region

    tweet, keyword, value = create_list(tweet_filename, keyword_filename) #call create_list function to get tweet, keyword and value lists

    counted_tweet = 0
    count = False
    sentiment_value_region = 0
    punctuation = '1234567890!@#$%^&*()-_=+`~[]{}\|:;\'\",.<>/?'

    for single_tweet in region:
        sentiment_value_tweet = 0
        counted_keyword = []
        for word in single_tweet:
            word = word.lower().strip(punctuation) #strip punctuation from words and convert to lowercase
            if word in keyword:
                sentiment_value_tweet += value[keyword.index(word)] #calculate sum of keyword sentiment values in single tweet
                count = True
                counted_keyword.append(word) #create list of keywords in single tweet
        if count == True:
            counted_tweet += 1 #if tweet has keyword, count tweet
            count = False
        if len(counted_keyword) > 0:
            happiness_score_tweet = (sentiment_value_tweet/len(counted_keyword)) #calculate happiness score of single tweet
            sentiment_value_region += happiness_score_tweet #calculate sum of single tweet happiness scores in region

    if counted_tweet == 0:
        happiness_score_region = 'none' #if there are no counted tweets, there is no happiness score of region
    else:
        happiness_score_region = (sentiment_value_region/counted_tweet) #calculate happiness score of region

    return happiness_score_region, counted_tweet #return tuple containing average score and number of counted tweets for region


def compute_tweets(tweet_filename, keyword_filename): #function to output list of location scores

    try:
        eastern, central, mountain, pacific = region_tweet(tweet_filename, keyword_filename) #call region_tweet function to get list of tweets for each region
        eastern_score = region_score(tweet_filename, keyword_filename, eastern) #call region_score function to get happiness score and counted tweet tuple for eastern region
        central_score = region_score(tweet_filename, keyword_filename, central) #call region_score function to get happiness score and counted tweet tuple for central region
        mountain_score = region_score(tweet_filename, keyword_filename, mountain) #call region_score function to get happiness score and counted tweet tuple for mountain region
        pacific_score = region_score(tweet_filename, keyword_filename, pacific) #call region_score function to get happiness score and counted tweet tuple for pacific region

        return [eastern_score, central_score, mountain_score, pacific_score] #return list of tuples

    except IOError:
        return [] #if invalid file name, return a blank list
