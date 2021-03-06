##########################################################
# plot handling module
##########################################################
from dateutil import parser
from datetime import timedelta
import numpy


def lon2txt(lon, pos=None):
    '''convert numerical degree to string east/west degree
       you can use this function matplotlib axis labeling
       
       usage:
              from matplotlib.ticker import FuncFormatter
       
              ax.xaxis.set_major_formatter(FuncFormatter(lon2txt) 

    Arguments:
    
        lon : integer or float

    '''
    fmt = '%g'
    lon = (lon+360) % 360
    if lon>180:
        lonlabstr = u'%s\N{DEGREE SIGN}W'%fmt
        lonlab = lonlabstr%abs(lon-360)
    elif lon<180 and lon != 0:
        lonlabstr = u'%s\N{DEGREE SIGN}E'%fmt
        lonlab = lonlabstr%lon
    else:
        lonlabstr = u'%s\N{DEGREE SIGN}'%fmt
        lonlab = lonlabstr%lon
    return lonlab

def lat2txt(lat, pos=None):
    fmt = '%g'
    if lat<0:
        latlabstr = u'%s\N{DEGREE SIGN}S'%fmt
        latlab = latlabstr%abs(lat)
    elif lat>0:
        latlabstr = u'%s\N{DEGREE SIGN}N'%fmt
        latlab = latlabstr%lat
    else:
        latlabstr = u'%s\N{DEGREE SIGN}'%fmt
        latlab = latlabstr%lat
    return latlab

def timelist(start, end, nparray=True):
        startdate = parser.parse(start)
        enddate = parser.parse(end)
        deltadate = timedelta(days=1)
        tnum = (enddate-startdate).days+1
        
        if nparray:
            return numpy.array([startdate + deltadate*i for i in range(tnum)])
        else:
            return [startdate + deltadate*i for i in range(tnum)]
                                                                        
