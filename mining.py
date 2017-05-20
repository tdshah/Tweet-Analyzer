
import re


#Goals - compare the popularity of Python, Ruby and Javascript programming languages and to retrieve programming tutorial links.
#3 steps:
#We will add tags to our tweets DataFrame in order to be able to manipualte the data easily.
#Target tweets that have "pogramming" or "tutorial" keywords.
#Extract links from the relevants tweets


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))


print (tweets['python'].value_counts()[True])
print (tweets['javascript'].value_counts()[True])
print (tweets['ruby'].value_counts()[True])


#comparison chart
prg_langs = ['python', 'javascript', 'ruby']
tweets_by_prg_lang = [tweets['python'].value_counts()[True], tweets['javascript'].value_counts()[True], tweets['ruby'].value_counts()[True]]

x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: python vs. javascript vs. ruby (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()


tweets['programming'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
tweets['tutorial'] = tweets['text'].apply(lambda tweet: word_in_text('tutorial', tweet))
tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet) or word_in_text('tutorial', tweet))

#counts of specific, relevant tweets
print (tweets['programming'].value_counts()[True])
print (tweets['tutorial'].value_counts()[True])
print (tweets['relevant'].value_counts()[True])


print (tweets[tweets['relevant'] == True]['python'].value_counts()[True])
print (tweets[tweets['relevant'] == True]['javascript'].value_counts()[True])
print (tweets[tweets['relevant'] == True]['ruby'].value_counts()[True])
 

tweets_by_prg_lang = [tweets[tweets['relevant'] == True]['python'].value_counts()[True], 
                      tweets[tweets['relevant'] == True]['javascript'].value_counts()[True], 
                      tweets[tweets['relevant'] == True]['ruby'].value_counts()[True]]
x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width,alpha=1,color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: python vs. javascript vs. ruby (Relevant data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()



#extracting links from the relevant tweets
#use regex to retrieving link that start with "http://" or "https://" from a text
#This function will return the url if found, otherwise it returns an empty string.

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''


#this column adds URL information
tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))

#new dataframe containing all the RELEVANT tweets that HAVE a link
tweets_relevant = tweets[tweets['relevant'] == True]
tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

print (tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link'])
print (tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['link'])
print (tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]['link'])


plt.show(block=True) 