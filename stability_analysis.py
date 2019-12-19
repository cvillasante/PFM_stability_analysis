import pandas as pd
import numpy as np

def loadResponseCurve(filename, dx):
    '''Loads a PFM response curve from a text file.
        Args:
            filename (string): path to the response curve file
            dx (float): spacing between adjacent data points in nanometers
        Returns:
            responseCurve (pandas dataframe): the response curve
    '''
    response = np.loadtxt(filename)[::2] # to-do: fix this in labview!
    position = np.arange(len(response) * 2 * dx)
    responseCurve = pd.DataFrame({"position": position, "response": response})

    return responseCurve

def derivativeOfResponseCurve(responseCurve):
    '''Take the derivative of a response curve and attach new column to input dataframe
        Args:
            responseCurve(pandas dataframe): the response curve
    '''
    dx = responseCurve['position'].values[1]
    ddx = np.diff(responseCurve['response'])/dx
    responseCurve['derivative'] = ddx
    responseCurve['derivative'] = list(ddx) + [0]

def findLinearRegionOfResponseCurve(responseCurve):
    '''Find linear region of a response curve, defined by +/- 10% of max slope
    Append linear region column to input data frame.
        Args:
            responseCurve (pandas dataframe): the response curve
        Returns:
            avgSlope (float): average slope of linear region
    '''
    if 'derivative' not in responseCurve:
        derivativeOfResponseCurve(responseCurve)

    ddx = responseCurve[]'derivative'].values
    linRange = (ddx > 0.9*(max(ddx))) & (ddx <= 1.1*(max(ddx)))
    peakRange = ddx[linRange]
    responseCurve['linearRange'] = linRange
    
    return np.mean(peakRange)