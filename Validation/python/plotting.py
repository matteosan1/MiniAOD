import ROOT

filenames = ("aodsim.root", "miniaodsim.root")
files = []
canvases = []
histos = [{}, {}]

for filename in filenames:
    files.append(ROOT.TFile(filename))

for i, f in enumerate(files):
    hNames = f.GetListOfKeys()
    for n in hNames:
        h = f.Get(n.GetName()).Clone()
        histos[i][n.GetName()] = h

for k in histos[0]:
    canvases.append(ROOT.TCanvas("c" + k, "c"))
    histos[0][k].Draw()
    histos[1][k].Draw("SAME")

outoput = ROOT.TFile("output.root", "recreate")
for c in cavases:
    c.Write()
output.Close()
