# here is an example graph

import File_IO as fio
import matplotlib.pyplot as plt

video_ratings = fio.read.get_views()

plt.xlabel('Videos')
plt.ylabel('views')

plt.bar(range(24), video_ratings)
plt.show()