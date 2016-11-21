import sys
sys.path.append("/Users/njlindsey/Workspace/projectsBerkeley/ANGF/")
import progs.core as core
import progs.fki as fki
# import progs.fkiPlot as fkiPlot
import numpy as np

#inputs
modelfile="MODEL.01"
distancefile="DIST"
freqfile="FREQ"
sourceDepth=0.25
receiverDepth=0

# npts=2048
#
# #generate array of frequencies
# freqs=np.linspace(0.01,0.5,npts)
# np.savetxt('FREQ',freqs,fmt='%f')
#
# #generate array of frequencies
# freqs=core.mungeFreq(freqfile)
# print(len(freqs))

#generate complete GF using CPS FKI programs
fki.calcGF(modelfile,distancefile,sourceDepth,receiverDepth)
#
# #read eigenfunctions from ascii into a numpy array
# with open('SLDER.TXT','r') as lovedispfile:
#     [headerL,paramsL,dataL]=eigCalc.mungeEig(lovedispfile)
# with open('SRDER.TXT','r') as raydispfile:
#     [headerR,paramsR,dataR]=eigCalc.mungeEig(raydispfile)
#
# #plot dispersion
# fig1=eigPlot.Dispersion(freqs,paramsL,paramsR);
#
# #plot eigenfunctions
# fig2=eigPlot.Eigenfunctions(freqs,headerL,headerR,dataL,dataR);
