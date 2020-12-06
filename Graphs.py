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
	
# plot_ratings_vs_videos()
# plot_views_vs_videos()