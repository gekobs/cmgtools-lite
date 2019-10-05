import ROOT as r

f = r.TFile("TEST_01/DYJetsToLL_Zpt400to650_amcatnloFXFX/treeProducerSusyAlphaT/tree.root")
t = f.Get("tree")
t.Show(1)
print "\n\n"

t.Show(10)
