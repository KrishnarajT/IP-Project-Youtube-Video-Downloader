# here is an example graph
import numpy as np
import File_IO as fio
import matplotlib.pyplot as plt


def plot_views_vs_videos():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_views = fio.read.get_views() 
	views_list = [] # new list that we will use to plot the graph

	# assigning the values from the raw string values to the new int list
	for views in video_views:
		views_list.append(int(views.rstrip('\n')))

	plt.xlabel('Videos')
	plt.ylabel('views')

	# to make it more readable, this video had like 7 million views so other charts look very small, hence changed it
	views_list[0] = 2346 # random value here

	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.bar(np.arange(len(views_list)), views_list, color = 'green')
	plt.savefig('Assets/Graphs/views_bar_graph.png')
			

def plot_ratings_vs_videos():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_views = fio.read.get_ratings() 
	views_list = [] # new list that we will use to plot the graph

	# assigning the values from the raw string values to the new int list
	for views in video_views:
		views_list.append(float(views.rstrip('\n')))

	plt.xlabel('Videos')
	plt.ylabel('Ratings')

	# to make it more readable, this video had like 7 million views so other charts look very small, hence changed it
	views_list[0] = 2.346 # random value here

	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.plot(np.arange(len(views_list)), views_list, color = 'red')
	plt.savefig('Assets/Graphs/ratings_bar_graph.png')


def plot_likes_vs_videos():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_likes = fio.read.get_likes()
	print(video_likes)
	likes_list = [] # new list that we will use to plot the graph
	
	# assigning the values from the raw string values to the new int list
	for likes in video_likes:
		likes_list.append(float(likes.rstrip('\n')))
	
	print(likes_list)
	plt.xlabel('Videos')
	plt.ylabel('likes')
	
	for i in range(len(likes_list)):
		if likes_list[i] > 10000:
			likes_list[i] = 10000
	print(likes_list)
	
	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.bar(np.arange(len(likes_list)), likes_list, color = 'green')
	plt.savefig('Assets/Graphs/likes_bar_graph.png')


def plot_dislikes_vs_videos():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_dislikes = fio.read.get_dislikes()
	print(video_dislikes)
	dislikes_list = [] # new list that we will use to plot the graph
	
	# assigning the values from the raw string values to the new int list
	for dislikes in video_dislikes:
		dislikes_list.append(float(dislikes.rstrip('\n')))
	
	print(dislikes_list)
	plt.xlabel('Videos')
	plt.ylabel('dislikes')
	
	for i in range(len(dislikes_list)):
		if dislikes_list[i] > 1000:
			dislikes_list[i] = 1000
	print(dislikes_list)
	
	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.bar(np.arange(len(dislikes_list)), dislikes_list, color = 'green')
	plt.savefig('Assets/Graphs/dislikes_bar_graph.png')


# plot_ratings_vs_videos()
# plot_views_vs_videos()
#plot_dislikes_vs_videos()
