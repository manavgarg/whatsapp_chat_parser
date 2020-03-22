#!/usr/bin/env python

from collections import defaultdict
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 

users= defaultdict(list)

def plotWordCloud(k=50):
	stopwords = ["image", "omitted", "go", ".", "will"] + list(STOPWORDS) 
	words = ""
	for user in users:
		for tup in users[user]:
			words += " " + tup[2].lower()

	wordcloud = WordCloud(width=480, height=480, max_words=k,
		stopwords = stopwords).generate(words)
	# plot the WordCloud image  
	plt.figure()
	plt.imshow(wordcloud, interpolation="bilinear") 
	plt.axis("off") 
	plt.margins(x=0, y=0) 
	plt.show()
	#plt.savefig("wordcloud.png")

if __name__ == '__main__':
	fd = open("../_chat.txt",mode='r',encoding='utf8', newline='\r\n')
	for i, line in enumerate(fd):   
		date = line.split(",")[0].split("[")[1]
		time = line.split(",")[1].split("]")[0]
		user = line.split("]")[1].split(":")[0].strip()
		message = line.split("]")[1].split(":")[1]
		users[user].append((date, time, message))

	# Compute word cloud (k words) per user.
	plotWordCloud()	

	fd.close()
