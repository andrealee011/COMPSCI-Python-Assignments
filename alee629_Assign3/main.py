#Assignment 3: Sentiment Analysis
#Andrea Lee 250836721

import sentiment_analysis

input_tweet = input('Enter tweet file name:\n') #prompt user for tweet file name
input_keyword = input('Enter keyword file name:\n') #prompt user for keyword file name

scores = sentiment_analysis.compute_tweets(input_tweet, input_keyword) #call compute_tweets function from sentiment_analysis module to get happiness scores and number of counted tweets for each region

#print output

print()

if len(scores) == 0: #blank list is returned if invalid file name
    print('File name does not exist.') #if blank list is returned, print file name does not exist)

else:
    eastern_score = scores[0]
    eastern_happiness_score = eastern_score[0]
    eastern_counted_tweet = eastern_score[1]

    central_score = scores[1]
    central_happiness_score = central_score[0]
    central_counted_tweet = central_score[1]

    mountain_score = scores[2]
    mountain_happiness_score = mountain_score[0]
    mountain_counted_tweet = mountain_score[1]

    pacific_score = scores[3]
    pacific_happiness_score = pacific_score[0]
    pacific_counted_tweet = pacific_score[1]

    if eastern_counted_tweet == 0:
        print('The Eastern Timezone has no tweets.')
    elif eastern_counted_tweet == 1:
        print('The Eastern Timezone has %d tweet and a happiness score of %.2f.' % (eastern_counted_tweet, eastern_happiness_score))
    else:
        print('The Eastern Timezone has %d tweets and a happiness score of %.2f.' % (eastern_counted_tweet, eastern_happiness_score))

    if central_counted_tweet == 0:
        print('The Central Timezone has no tweets.')
    elif central_counted_tweet == 1:
        print('The Central Timezone has %d tweet and a happiness score of %.2f.' % (central_counted_tweet, central_happiness_score))
    else:
        print('The Central Timezone has %d tweets and a happiness score of %.2f.' % (central_counted_tweet, central_happiness_score))

    if mountain_counted_tweet == 0:
        print('The Mountain Timezone has no tweets.')
    elif mountain_counted_tweet == 1:
        print('The Mountain Timezone has %d tweet and a happiness score of %.2f.' % (mountain_counted_tweet, mountain_happiness_score))
    else:
        print('The Mountain Timezone has %d tweets and a happiness score of %.2f.' % (mountain_counted_tweet, mountain_happiness_score))

    if pacific_counted_tweet == 0:
        print('The Pacific Timezone has no tweets.')
    elif pacific_counted_tweet == 1:
        print('The Pacific Timezone has %d tweet and a happiness score of %.2f.' % (pacific_counted_tweet, pacific_happiness_score))
    else:
        print('The Pacific Timezone has %d tweets and a happiness score of %.2f.' % (pacific_counted_tweet, pacific_happiness_score))

#determine happiest region and print output

    happiness_scores = [eastern_happiness_score, central_happiness_score, mountain_happiness_score, pacific_happiness_score]
    for index, score in enumerate(happiness_scores):
        if score == 'none':
            happiness_scores[index] = 0
    highest_score = max(happiness_scores)

    regions = ['Eastern', 'Central', 'Mountain', 'Pacific']
    happiest_region = regions[happiness_scores.index(highest_score)]

    print('\nThe happiest region with counted tweets is the %s Timezone.' % happiest_region)
