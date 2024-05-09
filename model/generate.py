import json
from pytube import YouTube
from pytube import Search
f= open('music_gnera.txt','r')
k = open("gnera_last_pice.json",'w')
# c=0
k.write('{"genre":{\n')
for i in f:
	i = i.replace('\n','')
	query = str(i)
	print(query)
	songs = []
	try:
		search_results = Search(query).results
		for i in range(10):
			video_url =  search_results[i].watch_url
			print(video_url)
			songs.append(str(video_url))
	except:
		pass
	k.write(f'"{query}":{songs},\n')
	# c =c+1
k.write('} } \n')

