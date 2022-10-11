# Importing packages and modules we need
import pandas as pan
import matplotlib.pyplot as plt

# Importing data
data = pan.read_csv('trees.csv',
                  names = ['Index','Girth',
                           'Height','Volume'])
# Cleaning the data 
del data['Index']
data.drop(0, inplace = True)

data['Girth'] = data['Girth'].astype(float)
data['Height'] = data['Height'].astype(float)
data['Volume'] = data['Volume'].astype(float)

data['Girth'] *= 0.0254
data['Height'] *= 0.305
data['Volume'] *= 0.0283

# Measuring the data
max_girth = (data['Girth'].round(2)).max()
max_height = (data['Height'].round(2)).max()
max_vol = (data['Volume'].round(2)).max()

min_girth = (data['Girth'].round(2)).min()
min_height = (data['Height'].round(2)).min()
min_vol = (data['Volume'].round(2)).min()

avg_girth = round(data['Girth'].mean(), 2)
med_girth = (data['Girth'].round(2)).median()
mod_girth = (data['Girth'].round(2)).mode()

avg_height = round(data['Height'].mean(), 2)
med_height = (data['Height'].round(2)).median()
mod_height = (data['Height'].round(2)).mode()

avg_vol = round(data['Volume'].mean(), 2)
med_vol = (data['Volume'].round(2)).median()
mod_vol = (data['Volume'].round(2)).mode()

# Creating table of the calculated data
df = pan.DataFrame({'Girth':[max_girth, min_girth,
                             avg_girth, med_girth,
                             mod_girth[0]],
                    'Height':[max_height, min_height,
                              avg_height, med_height,
                              mod_height[0]],
                    'Volume':[max_vol, min_vol,
                              avg_vol, med_vol,
                              mod_vol[0]]},
                   index = ['Maximum', 'Minimum',
                           'Average', 'Median','Mode'])

# Displaying the data
print('Tree measurements data\n')
print(data.round(1), end = '\n\n')
print('Measurements\n')
print(df, end = '\n\n')
print('Graphs')

# Creating the Visuals
plt.plot(data['Girth'])
plt.title('Girth')
plt.ylabel('Metre')
plt.show()

plt.plot(data['Height'])
plt.title('Height')
plt.ylabel('Metre')
plt.show()

plt.plot(data['Volume'])
plt.title('Volume')
plt.ylabel('Cubic Metre')
plt.show()