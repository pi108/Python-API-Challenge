import scipy
from scipy import stats
from collections import namedtuple


#===========================================================================================#
# Start of Function: run_linear_regression
#===========================================================================================#


def run_linear_regression (x, y):
    '''Run Linear regression using `scipy.linregress` -> returns dictionary'''
    slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, y)

    regress_values = [float(slope) * i + float(intercept) for i in x]

    line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))

    correlation = stats.pearsonr(x,y)

    my_dict = {'slope': slope,
            'intercept': intercept,
            'rvalue': rvalue,
            'pvalue': pvalue,
            'stderr': stderr,
            'regress_values':regress_values,
            'line_eq':line_eq,
            'correlation':correlation}
    return my_dict


#===========================================================================================#
# End of Function: run_linear_regression
#===========================================================================================#






#===========================================================================================#
# Start of Function: run_correlation
#===========================================================================================#

    
def run_correlation (x, y):
    correlation = stats.pearsonr(x,y)
    return correlation 



#===========================================================================================#
# End of Function: run_correlation
#===========================================================================================#










