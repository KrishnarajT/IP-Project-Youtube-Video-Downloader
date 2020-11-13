# here is an example graph

import File_IO as fio
import matplotlib.pyplot as plt

video_ratings = fio.read.get_ratings()

plt.xlabel('Range')
plt.ylabel('Rating')

plt.bar(range(24), video_ratings)
plt.show()