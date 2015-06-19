Basic instructions.

1 - Edit MiniAOD/Validation/plugins/Validation.cc to add the desired plots. In case accessors are different for AOD and MiniAOD
the code needs to be specialized accordingly.

2 - Run MiniAOD/Validation/python/ConfFile_cfg.py on the proper sample to produce a flat ROOT tree with information to validate.

3 - Repeat step 2 with all the samples that need to be compared.

4 - The python script makeHisto.py produces a ROOT file with all the histograms defined in the appropriate configuration file
(default plot.def). The syntax of the configuration is:
histoname bin low high (histoname has to match the corresponding branch name in the previously generated tree)

Example:
python makeHisto.py miniaod.root reco.root (option --help available)

The logic of the script is the following: first make a map with entries corresponding to the same event from the two rootfiles.
Then, for each in common, histograms are filled with entries corresponding to matched electrons.

5 - The python script makePlot.py produces the comparison plots (both single png files and .root file with all the canvases).
Example:
python makePlot.py output.root (option --help available)
