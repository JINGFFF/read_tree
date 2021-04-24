#!/usr/bin/env python
import sys
import os
import re
#from uncertainty_unfold import *
import ROOT
from ROOT import gROOT, THStack, TH1D, TList, TFile, TH2D
from math import fabs, sqrt



file1 = TFile.Open("/data/pku/home/pengj/testvbs/data/for_analysis/2018_tight_for_analysis_single_muon_A.root");
dir1 = file1.Get("treeDumper");
tree1 =dir1.Get("PKUCandidates");
ll = tree1.Print()
#print type(ll)
#print ll

