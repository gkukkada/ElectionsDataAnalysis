import warnings
warnings.filterwarnings("ignore");

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Elections():
	"""docstring for Elections"""
	def __init__(self, data):
		self.data = data

	def summary(self):

		""" It Calculates the mean, median, 1st Qu, 2nd Qu, min value, max value from the given variables. """

		count = 0
		detail = dict()
		for i in self.data:
			detail[i]={}
			if i=='votes' or i=='fips' or i =='fraction_votes':
				detail[i]["Min"]=np.min(self.data[i], axis=0)
				detail[i]["Max"]=np.max(self.data[i], axis=0)
				detail[i]["1st Qu"]=np.percentile(self.data[i], 25)
				detail[i]["Median"]= np.median(self.data[i], axis=0)
				detail[i]["Mean"]=np.mean(self.data[i], axis=0)
				detail[i]["2nd Qu"]=np.percentile(self.data[i], 50)
				detail[i]["StdDev"]=np.std(self.data[i], axis=0)
			else:
				pass
			count += 1
		return detail

	def plotBar(self, state_abb, party_name):

		#Plot the graphs using seaborn
		pe = self.data[self.data.state_abbreviation == state_abb]
		g = sns.FacetGrid(pe[pe.party == party_name], col = 'candidate',  col_wrap = 2) # Adjust the col_wrap for better visuals.
		g.map(sns.barplot, 'votes', 'county',color="r");
		sns.plt.show()

if __name__ == '__main__':

	dataset = pd.read_csv('./primary_results.csv')
	df = pd.DataFrame(dataset)
	print(dataset.state.unique())

	# data dictionary with correct data types and relevant variables
	dataset_dtype = dataset.dtypes
	print(dataset_dtype)

	# data Set: summary and variable extraction
	x = Elections(df)
	hours_df = pd.DataFrame(x.summary())

	# Removing the unwanted attributes for displaying summary.
	del hours_df['state']
	del hours_df['candidate']
	del hours_df['county']
	del hours_df['state_abbreviation']
	del hours_df['party']
	print(hours_df)

	# Plot the graphs of Republicans and democrats in Arizona State counties
	x.plotBar('AZ','Republican')
	x.plotBar('AZ','Democrat')

	# Plot the graphs of Republicans and democrats in Texas State counties
	x.plotBar('TX','Republican')
	x.plotBar('TX','Democrat')

	# Plot the graphs of Republicans and democrats in Michigan State counties
	x.plotBar('MI','Republican')
	x.plotBar('MI','Democrat')

	# Plot the graphs of Republicans and democrats in Florida State counties
	x.plotBar('FL','Republican')
	x.plotBar('FL','Democrat')

	# Plot the graphs of Republicans and democrats in Ohio State counties
	x.plotBar('OH','Republican')
	x.plotBar('OH','Democrat')