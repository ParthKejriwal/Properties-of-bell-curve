import pandas as pd
import plotly.figure_factory as ff
import csv
import statistics

df=pd.read_csv('StudentsPerformance.csv')
maths=df['math score'].tolist()
#fig=ff.create_distplot([height],['Height'])
#fig.show()

mean=statistics.mean(maths)
median=statistics.median(maths)
mode=statistics.mode(maths)
std=statistics.stdev(maths)

maths_first_std_deviation_start,maths_first_std_deviation_end = mean-std,mean+std
maths_second_std_deviation_start,maths_second_std_deviation_end = mean-(2*std),mean+(2*std)
maths_third_std_deviation_start,maths_third_std_deviation_end = mean-(3*std),mean+(3*std)

maths_list_of_data_within_1_std_deviation = [result for result in maths if result > maths_first_std_deviation_start and result < maths_first_std_deviation_end]
maths_list_of_data_within_2_std_deviation = [result for result in maths if result > maths_second_std_deviation_start and result < maths_second_std_deviation_end]
maths_list_of_data_within_3_std_deviation = [result for result in maths if result > maths_third_std_deviation_start and result < maths_third_std_deviation_end]

print(len(maths_list_of_data_within_1_std_deviation)*100.0/len(maths))
print(len(maths_list_of_data_within_2_std_deviation)*100.0/len(maths))
print(len(maths_list_of_data_within_3_std_deviation)*100.0/len(maths))