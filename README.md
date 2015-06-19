Basic instructions.

1-<br>
cmsrel CMSSW_7_4_X<br>
cd CMSSW_7_4_X/src/<br>
cmsenv<br>
git cms-init<br>
git clone https://github.com/matteosan1/MiniAOD<br>
scram b<br>

2 - Edit MiniAOD/Validation/plugins/Validation.cc to add the desired plots. In case accessors are different for AOD and MiniAOD the code needs to be specialized accordingly.

3 - Run MiniAOD/Validation/python/ConfFile_cfg.py on the proper sample to produce a flat ROOT tree with information to validate.

4 - Repeat step 3 with all the samples that need to be compared.

5 - The python script makeHisto.py produces a ROOT file with all the histograms defined in the appropriate configuration file
(default plot.def). The syntax of the configuration is:<br>
histoname bin low high (histoname has to match the corresponding branch name in the previously generated tree)
<br>
Example:<br>
python makeHisto.py miniaod.root reco.root (option --help available)<br>
<br>
The logic of the script is the following: first make a map with entries corresponding to the same event from the two rootfiles. Then, for each in common, histograms are filled with entries corresponding to matched electrons.<br>
<br>
6 - The python script makePlot.py produces the comparison plots (both single png files and .root file with all the canvases).<br>
Example:<br>
python makePlot.py output.root (option --help available)<br>
<br>
