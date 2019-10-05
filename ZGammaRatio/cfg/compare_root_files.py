#!/usr/bin/env python
# Tai Sakuma <sakuma@cern.ch>
import sys
import os
import ROOT
import unittest
import math

##__________________________________________________________________||
file1path = sys.argv[1]
file2path = sys.argv[2]
sys.argv[:] = [sys.argv[0]]

##__________________________________________________________________||
class AlphaToolTest(unittest.TestCase):

    def test_one(self):
        file1 = ROOT.TFile.Open(file1path)
        file2 = ROOT.TFile.Open(file2path)
        self.assert_tfile(file1, file2)

    def assert_tfile(self, file1, file2):
        keys1 = file1.GetListOfKeys()
        keys2 = file2.GetListOfKeys()
        self.assert_tkeys(keys1, keys2)
        for key1 in keys1:
            keyname = key1.GetName()
            obj1 = file1.Get(keyname)
            obj2 = file2.Get(keyname)
            obj1classname = obj1.__class__.__name__
            obj2classname = obj2.__class__.__name__
            self.assertEqual(obj1classname, obj2classname)
            if 'TDirectoryFile' == obj1classname:
                self.assert_tfile(obj1, obj2)
            elif 'THStack' == obj1classname:
                self.assert_thstack(obj1, obj2)
            elif 'TTree' == obj1classname:
                self.assert_ttree(obj1, obj2)
            elif 'TLegend' == obj1classname:
                pass
            else:
                print "unknown class:", obj1classname

    def assert_tkeys(self, keys1, keys2):
        self.assertEqual(keys1.GetSize(), keys2.GetSize())
        keynames1 = [k.GetName() for k in keys1]
        keynames2 = [k.GetName() for k in keys2]
        self.assertEqual(sorted(keynames1), sorted(keynames2))

    def assert_thstack(self, obj1, obj2):
        self.assertEqual(obj1.GetNhists(), obj2.GetNhists())
        for h1, h2 in zip(obj1.GetHists(), obj2.GetHists()):
            self.assert_th1(h1, h2)

    def assert_th1(self, h1, h2):
        self.assertEqual(h1.GetName(), h2.GetName())
        self.assertEqual(h1.GetNbinsX(), h2.GetNbinsX())
        for i in range(0, h1.GetNbinsX() + 2):
            self.assertEqual(h1.GetBinCenter(i), h2.GetBinCenter(i))
            self.assertEqual(h1.GetBinContent(i), h2.GetBinContent(i))
            self.assertEqual(h1.GetBinError(i), h2.GetBinError(i))

    def assert_ttree(self, tree1, tree2):
        self.assert_ttree_leaf_definition(tree1, tree2)
        self.assert_ttree_entries(tree1, tree2)

    def assert_ttree_leaf_definition(self, tree1, tree2):
        leaves1 = [l for l in tree1.GetListOfLeaves()]
        leaves2 = [l for l in tree2.GetListOfLeaves()]
        if not len(leaves1) == len(leaves2):
            print "len(leaves)", len(leaves1), len(leaves2)
        for leaf1 in leaves1:
            leaf2 = [l for l in leaves2 if l.GetName() == leaf1.GetName()]
            self.assertEqual(1, len(leaf2))
            leaf2 = leaf2[0]
            self.assert_leaf_definition(leaf1, leaf2)

    def assert_leaf_definition(self, leaf1, leaf2):
        self.assertEqual(leaf1.GetName(), leaf2.GetName())
        self.assertEqual(leaf1.GetTypeName(), leaf2.GetTypeName())
        
    def assert_ttree_entries(self, tree1, tree2):
        if not tree1.GetEntries() == tree2.GetEntries():
            print "GetEntries()", tree1.GetEntries(), tree2.GetEntries()
        branchNames = [l.GetName() for l in tree1.GetListOfLeaves()]
        for i in xrange(tree1.GetEntries()):
            if tree1.GetEntry(i) <= 0: break
            tree2.GetEntry(i)
            for branchName in branchNames:
                if  getattr(tree1, branchName) == getattr(tree2, branchName): continue
                if math.isnan(getattr(tree1, branchName)) and math.isnan(getattr(tree2, branchName)): continue
                try:
                    print branchName, [e for e in getattr(tree1, branchName)], [e for e in getattr(tree2, branchName)]
                except:
                    print branchName, getattr(tree1, branchName), getattr(tree2, branchName)

##__________________________________________________________________||
if __name__ == '__main__':
    unittest.main()
