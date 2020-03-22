#!/usr/bin/env python

from collections import defaultdict
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import datetime
import calendar

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


def plotMsgExchange():
	msgX = defaultdict(dict)
	for user in users:
		for tup in users[user]:
			date,_,msg = tup
			fmtDate = datetime.datetime.strptime(date,"%m/%d/%y")
			monthStr = str(calendar.month_abbr[fmtDate.month])+'_'+str(fmtDate.year)
			if user in msgX[monthStr]:
				msgX[monthStr][user] += 1
			else:
				msgX[monthStr][user] = 0
	user_vals = defaultdict(list)
	index = []
	for key in msgX:
		index.append(key)
		for user in msgX[key]:
			user_vals[user].append(msgX[key][user])
	plt.figure()
	plt.xlabel('month')
	plt.ylabel('msg_exchanged')
	for user in users:
		plt.plot(index,user_vals[user], label=user)
	plt.legend()
	plt.show()


if __name__ == '__main__':
	fd = open("../_chat.txt",mode='r',encoding='utf8', newline='\r\n')
	for i, line in enumerate(fd):
		date = line.split(",")[0].split("[")[1]
		time = line.split(",")[1].split("]")[0]
		user = line.split("]")[1].split(":")[0].strip()
		message = line.split("]")[1].split(":")[1]
		users[user].append((date, time, message))

	# Compute word cloud (k words) per user.
	# plotWordCloud()
	plotMsgExchange()
	fd.close()
