# #Social Media Post Analyzer:
# #1. Develop a function that analyzes a social media post and returns the sentiment (positive, negative, neutral) and keywords used.
# #2. Expand the function to identify emojis and potential trends
# # post=input("Enter Quote: ")
# # def post_analyze(post):
# from textblob import TextBlob

# def get_sentiment(text):
#     analysis = TextBlob(text)
#     # Sentiment polarity ranges from -1 to 1
#     polarity = analysis.sentiment.polarity
    
#     if polarity > 0:
#         return "😊"  # Happy emoji
#     elif polarity < 0:
#         return "😢"  # Sad emoji
#     else:
#         return "😐"  # Neutral emoji

# # Example usage
# user_input = input("Enter a text or quote: ")
# result = get_sentiment(user_input)
# print(f"Sentiment: {result}")

#getting input
user=input("Enter Post: ")
def sentiment_analyse(post):
    #words
    positive=["good","awesome","happy","smile","nice","mind blowing"]
    negative=["bad","sad","cry","pain","painful","alone","ugly","lost"]
    P=0
    N=0
    #checking if input match to positive list
    for i in positive:
        if i in post:
            P+=1
    #checking if input match to negative list
    for i in negative:
        if i in post:
            N+=1
    #showing sentiments
    if P>N:
        return "Sentiment: 😊"
    elif P<N:
        return "sentiment: 😢"
    else:
        return "sentiment: 😐"
result=sentiment_analyse(user)
print(result)





























