# here is an example graph
import numpy as np
import File_IO as fio
import matplotlib.pyplot as plt

video_views = fio.read.get_views() # this list is the raw list from the file, contains '\n' at the end that we don't need
views_list = [] # new list that we will use to plot the graph

# assigning the values from the raw string values to the new int list
for views in video_views:
    views_list.append(int(views.rstrip('\n')))

plt.xlabel('Videos')
plt.ylabel('views')

views_list[0] = 2345 # to make it more readable, this video had like 7 million views so other charts look very small, hence changed it
print(views_list) # just to see what the data for the graph looks like
print(len(views_list))
plt.bar(np.arange(len(views_list)), views_list) # plots a simple graph
plt.show()