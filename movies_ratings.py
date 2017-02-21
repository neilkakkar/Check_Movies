from __future__ import print_function

import os
import omdb
import re
import operator
import sys

pattern = re.compile('[a-zA-Z0-9 ]+')

notmovie = re.compile('srt$|pdf$|zip$')
#print (os.getcwd())
#print (os.listdir(path))

def search(movies):
	dic = {}
	for movie in movies:
		#print(movie)
		if len(movie)<=3:
			continue
		try:
			obj = omdb.title(movie)
			#print(obj)
			if(obj!=[]):
				dic[movie] = obj.imdb_rating 
				#print (obj)
			pass
		except:
			pass#print("Error establishing connection\n")

	return (dic)

def clean(movies):
	l = []
	for movie in movies:
		if notmovie.search(movie):
			#print(movie)
			continue

		movie = movie.replace('.',' ')
		#print(movie)

		res =pattern.findall(movie)

		interest = res[0]
		flag = 0
		for i in range(1,len(interest)-1):
			if (not interest[i].isdigit() and interest[i-1].isdigit()):
				movie = interest[:i]
				#print(movie)
				flag = 1
				break

		if flag==0:
			movie = interest

		l.append(movie)
	return l

def main():
	path = os.getcwd()#"F:\odc downloads"

	if(len(sys.argv)==2):
		path = sys.argv[1]

	movies = os.listdir(path)
	movies = clean(movies)
	print("Searching...")
	dic = search(movies)

	sorted_list = sorted(dic.items(),key = operator.itemgetter(1))
	sorted_list = sorted_list[::-1]

	for item in sorted_list:
		print(item[0]," ------------  ",item[1])

	#print(len(sorted_list))


if __name__ == "__main__":
	main()