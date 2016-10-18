# ElectionsDataAnalysis
2016 US Elections Data analysis in python 

This folder consists of python script files to generate plot the graphs and to generate the DataFrame with min, mean, median, Standard Deviation, max, 1st Qu, 2nd Qu using numpy module.

plots/ - 
	This directory contains all the png images which are basically graphs between various attributes.

Elections.py - This is core python scripting file which generates the plots and summary of the given dataset

primary_results.csv - Contains all the data related to 2016 US presidential elections. The attributes are
	state  : state where the primary or caucus was held
	state_abbreviation  : two letter state abbreviation
	county  : county where the results come from
	fips  : FIPS county code
	party  : Democrat or Republican
	candidate  : name of the candidate
	votes  : number of votes the candidate received in the corresponding state and county (may be missing)
	fraction_votes  : fraction of votes the president received in the corresponding state, county, and primary.

electionsDataAnalysisInPython.html - contains total documentation of this project. Kindly open this file within this directory because all the project related images are linked to the plots directory.
