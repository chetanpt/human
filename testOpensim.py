__author__ = 'Chetan'

from opensim import *

print "Hello Model"

#m = opensim.model('C:\OpenSim 3.3\Models\Gait2354_Simbody\gait2354_simbody.osim')
myModel = opensim.Model('C:\OpenSim 3.3\Models\Gait2354_Simbody\gait2354_simbody.osim')

print myModel.getCoordinateSet().getSize()
print str(myModel.getCoordinateSet())   
numberJoints= myModel.getJointSet().getSize()

print numberJoints