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
	
	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.bar(np.arange(len(views_list)), views_list, color = 'green')
	plt.savefig('Assets/Graphs/views_bar_graph.png')
	
def plot_views_vs_videos_line():
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

	for i in range(len(views_list)):
		if views_list[i] > 3e6:
			views_list[i] = 3e6
		
		
	plt.xlabel('Videos')
	plt.ylabel('views')

	# to make it more readable, this video had like 7 million views so other charts look very small, hence changed it
	
	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.plot(np.arange(len(views_list)), views_list, color = 'green')
	plt.savefig('Assets/Graphs/views_line_graph.png')
	
def plot_views_vs_videos_hist():
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
	likes_list = [] # new list that we will use to plot the graph
	for i in range(len(video_likes)):
		if video_likes[i] == 'None\n' :
			video_likes[i] = '0\n'


# assigning the values from the raw string values to the new int list
	for likes in video_likes:
		likes_list.append(int(likes.rstrip('\n')))

	bin_val = 1000
	bins = []
	Max = 0
	for i in likes_list:
		if i > Max:
			Max = i
	for i in range(15):
		bins.append(i*bin_val)


	plt.hist(likes_list, bins, histtype='bar', rwidth=0.8, color = 'yellow')
	plt.xlabel('Views')
	plt.ylabel('Number of videos')
	plt.title('Number of videos vs likes')
	plt.savefig('Assets/Graphs/likes_hist_graph.png')

def plot_ratings_vs_videos():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_ratings = fio.read.get_ratings() 
	ratings_list = [] # new list that we will use to plot the graph
	
	for i in range(len(video_ratings)):
		if video_ratings[i] == 'None\n' :
			video_ratings[i] = '0.0\n'
			
	# assigning the values from the raw string values to the new int list
	for ratings in video_ratings:
		ratings_list.append(float(ratings.rstrip('\n')))

	plt.xlabel('Videos')
	plt.ylabel('Ratings')

	# to make it more readable, this video had like 7 million ratings so other charts look very small, hence changed it
	ratings_list[0] = 2.346 # random value here

	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.plot(np.arange(len(ratings_list)), ratings_list, color = 'red')
	plt.savefig('Assets/Graphs/ratings_bar_graph.png')

def plot_ratings_vs_videos_hist():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_ratings = fio.read.get_ratings()
	ratings_list = [] # new list that we will use to plot the graph
	for i in range(len(video_ratings)):
		if video_ratings[i] == 'None\n' :
			video_ratings[i] = '0.0\n'
	
	
	# assigning the values from the raw string values to the new int list
	for ratings in video_ratings:
		ratings_list.append(float(ratings.rstrip('\n')))
	
	bin_val = 0.25
	bins = []
	for i in range(8):
		bins.append(3+i*bin_val)
	print(bins)
	plt.hist(ratings_list, bins, histtype='bar', rwidth=0.8, color = 'pink')
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
	likes_list = [] # new list that we will use to plot the graph
	
	for i in range(len(video_likes)):
		if video_likes[i] == 'None\n' :
			video_likes[i] = '0.0\n'
	
	
	# assigning the values from the raw string values to the new int list
	for likes in video_likes:
		likes_list.append(float(likes.rstrip('\n')))
	
	for i in range(len(likes_list)):
		if likes_list[i] > 5e5:
			likes_list[i] = 5e5
	
	plt.xlabel('Videos')
	plt.ylabel('likes')
	
	
	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.plot(np.arange(len(likes_list)), likes_list, color = 'green')
	plt.savefig('Assets/Graphs/likes_line_graph.png')

def plot_dislikes_vs_videos():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""

# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_dislikes = fio.read.get_dislikes()
	for i in range(len(video_dislikes)):
		if video_dislikes[i] == 'None\n' :
			video_dislikes[i] = '0.0\n'
	dislikes_list = [] # new list that we will use to plot the graph
	
	# assigning the values from the raw string values to the new int list
	for dislikes in video_dislikes:
		dislikes_list.append(float(dislikes.rstrip('\n')))
		
	for i in range(len(dislikes_list)):
		if dislikes_list[i] > 6e3:
			dislikes_list[i] = 6e3

	
	plt.xlabel('Videos')
	plt.ylabel('dislikes')
	
	
	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.bar(np.arange(len(dislikes_list)), dislikes_list, color = 'green')
	plt.savefig('Assets/Graphs/dislikes_bar_graph.png')

def plot_dislikes_vs_videos_hist():
	"""
	Plots a graph by looking at the data stored in the files, and then saves the graph in Assets/Graphs as png.
	None -> None
	"""
	
	# this list is the raw list from the file, contains '\n' at the end that we don't need
	video_dislikes = fio.read.get_dislikes()
	dislikes_list = [] # new list that we will use to plot the graph
	for i in range(len(video_dislikes)):
		if video_dislikes[i] == 'None\n' :
			video_dislikes[i] = '0\n'
	
	
	# assigning the values from the raw string values to the new int list
	for dislikes in video_dislikes:
		dislikes_list.append(int(dislikes.rstrip('\n')))
	
	bin_val = 1000
	bins = []
	Max = 0
	for i in dislikes_list:
		if i > Max:
			Max = i
	for i in range(15):
		bins.append(i*bin_val)
	
	
	plt.hist(dislikes_list, bins, histtype='bar', rwidth=0.8, color = 'yellow')
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
	categories_list = [] # new list that we will use to plot the graph
	
	# assigning the values from the raw string values to the new int list
	for categories in video_categories:
		categories_list.append(categories.rstrip('\n'))
	
	cat_list = ['Education', 'Science & Technology', 'Music', 'Autos & Vehicles', 'Entertainment', 'Howto & Style', 'People & Blogs']
	cat_list_disp = ['Education', 'Science', 'Music', 'Vehicles', 'Entertain', 'How-to', 'People']
	sorted_cats = [0 for i in range(len(cat_list))]
	
	for i in range(len(cat_list)):
		for j in range(i, len(categories_list)):
			if cat_list[i] == categories_list[j]:
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
	categories_list = [] # new list that we will use to plot the graph
	
	# assigning the values from the raw string values to the new int list
	for categories in video_categories:
		categories_list.append(categories.rstrip('\n'))
	
	cat_list = ['Education', 'Science & Technology', 'Music', 'Autos & Vehicles', 'Entertainment', 'Howto & Style', 'People & Blogs']
	cat_list_disp = ['Education', 'Science', 'Music', 'Vehicles', 'Entertain', 'How-to', 'People']
	sorted_cats = [0 for i in range(len(cat_list))]
	
	for i in range(len(cat_list)):
		for j in range(i, len(categories_list)):
			if cat_list[i] == categories_list[j]:
				sorted_cats[i] += 1
	# plots a simple graph that is saved as png in Assets/Graphs/. This file can then be accessed by other files.
	plt.pie(sorted_cats, labels = cat_list_disp,explode = (0.1, 0, 0, 0, 0, 0, 0), shadow = True )
	plt.savefig('Assets/Graphs/categories_pie_chart.png')

# plot_views_vs_videos()
# plot_ratings_vs_videos_hist()
# plot_views_vs_videos_hist()
# plot_views_vs_videos_line()
# plot_ratings_vs_videos()
# plot_likes_vs_videos()
# plot_likes_vs_videos_hist()
# plot_dislikes_vs_videos()
# plot_dislikes_vs_videos_hist()
# plot_categories_vs_videos()
# plot_categories_vs_videos_pie()
