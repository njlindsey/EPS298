#eigCalcRun.py script to execute eignenfunction computation
import sys
sys.path.append("/Users/njlindsey/Workspace/projectsBerkeley/ANGF/")
import progs.core as core
import progs.eigCalc as eigCalc
import progs.eigPlot as eigPlot
import numpy as np

#inputs
modelfile="./MODEL.01"
distancefile="DIST"
freqfile="FREQ"
sourceDepth=0.00
receiverDepth=0.00

##make model plot
with open(modelfile,'r') as mfile:
    figModel=eigPlot.Model(mfile)

#generate array of frequencies --> 0.01Hz - 1.00Hz
freqs=core.mungeFreq(freqfile)
freqs=np.linspace(0.01,0.5,10)
freqs=np.round(freqs,2)
np.savetxt('FREQ',freqs,fmt='%f')

#generate eignenfunctions using CPS
print('here')
eigCalc.calcLove(modelfile,distancefile,freqfile,sourceDepth,receiverDepth)
eigCalc.calcRay(modelfile,distancefile,freqfile,sourceDepth,receiverDepth)
#eigCalc.calcLove(modelfile,distancefile,sourceDepth,receiverDepth,freqfile)
#eigCalc.calcRay(modelfile,distancefile,sourceDepth,receiverDepth,freqfile)

######
######
######
#read eigenfunctions from ascii into a numpy array
with open('SLDER.TXT','r') as lovedispfile:
    [headerL,paramsL,dataL]=eigCalc.mungeEig(lovedispfile)

with open('SRDER.TXT','r') as raydispfile:
    [headerR,paramsR,dataR]=eigCalc.mungeEig(raydispfile)

#plot dispersion
freqsDisp=freqs.tolist() #params are read long period to short period
fig1=eigPlot.Dispersion(freqsDisp,paramsL,paramsR);

#plot eigenfunctions
freqsEig=freqs.tolist()
fig2=eigPlot.Eigenfunctions(freqsEig,headerL,headerR,dataL,dataR);
