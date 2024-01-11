import matplotlib.pyplot as plt
import pandas as pd

class_a = [85, 90, 75, 60, 78, 88, 95]
class_b = [80, 70, 90, 88, 85, 80, 92]

df = pd.DataFrame({'Class a': class_a, 'Class b': class_b})

df.boxplot(column=['Class a', 'Class b'])
plt.title('Boxplot')
plt.ylabel('grade')
plt.show()