# here is an example graph
import numpy as np
import File_IO as fio
import matplotlib.pyplot as plt

# All These functions plot the graph, and then save the figure in a folder.
# These figues are then accessed by main.py to show in the statistics page.


def plot_views_vs_videos():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	views_list = fio.read.get_views()
	plt.xlabel('Videos')
	plt.ylabel('views')
	plt.bar(np.arange(len(views_list)), views_list, color = 'green')
	plt.savefig('Assets/Graphs/views_bar_graph.png')

def plot_views_vs_videos_line():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	views_list = fio.read.get_views()
	for i in range(len(views_list)):
		if views_list[i] > 3e6:
			views_list[i] = 3e6
	
	plt.xlabel('Videos')
	plt.ylabel('views')
	plt.plot(np.arange(len(views_list)), views_list, color = 'green')
	plt.savefig('Assets/Graphs/views_line_graph.png')

def plot_views_vs_videos_hist():
	"""
	Plots a graph by looking at the data stored in the files, 
	and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	views_list = fio.read.get_views()
	
	bin_val = 1000
	bins = []
	Max = 0
	for i in views_list:
		if i > Max:
			Max = i
	for i in range(15):
		bins.append(i*bin_val)
	
	plt.hist(views_list, bins, histtype='bar', rwidth=0.8, color = 'yellow')
	plt.xlabel('Views')
	plt.ylabel('Number of videos')
	plt.title('number of videos with views')
	plt.savefig('Assets/Graphs/views_hist_graph.png')

def plot_likes_vs_videos_hist():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_likes = fio.read.get_likes()
	for i in range(len(video_likes)):
		if video_likes[i ] is None :
			video_likes[i] = 0
	
	bin_val = 1000
	bins = []
	Max = 0
	for i in video_likes:
		if i > Max:
			Max = i
	for i in range(15):
		bins.append(i*bin_val)
	
	
	plt.hist(video_likes, bins, histtype='bar', rwidth=0.8, color = 'yellow')
	plt.xlabel('Views')
	plt.ylabel('Number of videos')
	plt.title('Number of videos vs likes')
	plt.savefig('Assets/Graphs/likes_hist_graph.png')

def plot_ratings_vs_videos():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	video_ratings = fio.read.get_ratings()
	
	for i in range(len(video_ratings)):
		if video_ratings[i ] is None :
			video_ratings[i] = 0.0
	
	plt.xlabel('Videos')
	plt.ylabel('Ratings')
	
	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.plot(np.arange(len(video_ratings)), video_ratings, color = 'red')
	plt.savefig('Assets/Graphs/ratings_bar_graph.png')

def plot_ratings_vs_videos_hist():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_ratings = fio.read.get_ratings()
	for i in range(len(video_ratings)):
		if video_ratings[i ] is None :
			video_ratings[i] = 0.0
	
	bin_val = 0.25
	bins = []
	for i in range(8):
		bins.append(3+i*bin_val)
	print(bins)
	plt.hist(video_ratings, bins, histtype='bar', rwidth=0.8, color = 'pink')
	plt.xlabel('Views')
	plt.ylabel('Number of videos')
	plt.title('Number of videos vs ratings')
	plt.savefig('Assets/Graphs/ratings_hist_graph.png')

def plot_likes_vs_videos():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_likes = fio.read.get_likes()
	
	for i in range(len(video_likes)):
		if video_likes[i ] is None :
			video_likes[i] = 0.0
	
	for i in range(len(video_likes)):
		if video_likes[i] > 5e5:
			video_likes[i] = 5e5
	
	plt.xlabel('Videos')
	plt.ylabel('likes')
	
	
	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.plot(np.arange(len(video_likes)), video_likes, color = 'green')
	plt.savefig('Assets/Graphs/likes_line_graph.png')

def plot_dislikes_vs_videos():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	video_dislikes = fio.read.get_dislikes()
	for i in range(len(video_dislikes)):
		if video_dislikes[i ] is None :
			video_dislikes[i] = 0.0
	
	for i in range(len(video_dislikes)):
		if video_dislikes[i] > 6e3:
			video_dislikes[i] = 6e3
	
	plt.xlabel('Videos')
	plt.ylabel('dislikes')
	plt.bar(np.arange(len(video_dislikes)), video_dislikes, color = 'green')
	plt.savefig('Assets/Graphs/dislikes_bar_graph.png')

def plot_dislikes_vs_videos_hist():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_dislikes = fio.read.get_dislikes()
	for i in range(len(video_dislikes)):
		if video_dislikes[i ] is None :
			video_dislikes[i] = 0
	
	bin_val = 1000
	bins = []
	Max = 0
	for i in video_dislikes:
		if i > Max:
			Max = i
	for i in range(15):
		bins.append(i*bin_val)
	
	
	plt.hist(video_dislikes, bins, histtype='bar', rwidth=0.8, color = 'yellow')
	plt.xlabel('Views')
	plt.ylabel('Number of videos')
	plt.title('Number of videos vs dislikes')
	plt.savefig('Assets/Graphs/dislikes_hist_graph.png')

def plot_categories_vs_videos():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_categories = fio.read.get_categories()
	
	cat_list = ['Education', 'Science & Technology', 'Music', 'Autos & Vehicles', 'Entertainment', 'Howto & Style', 'People & Blogs']
	cat_list_disp = ['Education', 'Science', 'Music', 'Vehicles', 'Entertain', 'How-to', 'People']
	sorted_cats = [0 for i in range(len(cat_list))]
	
	for i in range(len(cat_list)):
		for j in range(i, len(video_categories)):
			if cat_list[i] == video_categories[j]:
				sorted_cats[i] += 1
	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.bar(cat_list_disp, sorted_cats, color = 'orange')
	plt.savefig('Assets/Graphs/categories_bar_graph.png')

def plot_categories_vs_videos_pie():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_categories = fio.read.get_categories()
	
	cat_list = ['Education', 'Science & Technology', 'Music', 'Autos & Vehicles', 'Entertainment', 'Howto & Style', 'People & Blogs']
	cat_list_disp = ['Education', 'Science', 'Music', 'Vehicles', 'Entertain', 'How-to', 'People']
	sorted_cats = [0 for i in range(len(cat_list))]
	
	for i in range(len(cat_list)):
		for j in range(i, len(video_categories)):
			if cat_list[i] == video_categories[j]:
				sorted_cats[i] += 1
	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.pie(sorted_cats, labels = cat_list_disp,explode = (0.1, 0, 0, 0, 0, 0, 0), shadow = True )
	plt.savefig('Assets/Graphs/categories_pie_chart.png')

plot_views_vs_videos()
plot_ratings_vs_videos_hist()
plot_views_vs_videos_hist()
plot_views_vs_videos_line()
plot_ratings_vs_videos()
plot_likes_vs_videos()
plot_likes_vs_videos_hist()
plot_dislikes_vs_videos()
plot_dislikes_vs_videos_hist()
plot_categories_vs_videos()
plot_categories_vs_videos_pie()
