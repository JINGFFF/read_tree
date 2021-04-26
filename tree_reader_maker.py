#!/usr/bin/python

import sys
import time
import os
#year              = sys.argv[1];

#os.system("mkdir -p " + outdir);
#os.system("python tree_print.py >> tree.txt ")
infile =open('tree.txt', 'r')
lines = infile.readlines()


outfile_h = open('tree.h', 'w')
outfile_c = open('tree_read.C', 'w')

outfile_c.write('#include <TROOT.h> \n')
outfile_c.write('#include <TChain.h>\n')
outfile_c.write('#include <TCanvas.h>\n')
outfile_c.write('#include <TFile.h>\n')
outfile_c.write('#include <TCanvas.h>\n')
outfile_c.write('#include <TLorentzVector.h>\n')
outfile_c.write('#include <fstream>\n')
outfile_c.write('#include <iomanip>\n')
outfile_c.write('#include <TH1D.h>\n')
outfile_c.write('#include "TTreeReader.h"\n')
outfile_c.write('#include <TTreeReaderArray.h>\n')
outfile_c.write('#include <TH2.h>\n')
outfile_c.write('#include <algorithm>\n')
outfile_c.write('#include <cmath>\n')
outfile_c.write('#include <ctime>\n')
outfile_c.write('#include <map>\n')
outfile_c.write('#include <sstream>\n')
outfile_c.write('#include <string>\n')
outfile_c.write('#include <vector>\n')
outfile_c.write('#include <time.h>\n')
outfile_c.write('#include <stdlib.h>\n')

outfile_c.write('#include "tree.h"\n\n')
outfile_c.write('using namespace std;\n\n')

outfile_c.write('string getTime(){\n')
outfile_c.write('   time_t timep;\n')
outfile_c.write('   time (&timep);\n')
outfile_c.write('   char tmp[64];\n')
outfile_c.write('   strftime(tmp, sizeof(tmp), "%Y-%m-%d %H:%M:%S",localtime(&timep) );\n')
outfile_c.write('   return tmp;\n')
outfile_c.write('}\n')


outfile_c.write('void tree_read(){\n')
outfile_c.write('   string   time_start = getTime();\n')

outfile_c.write('   TString infilename = "/data/pku/home/pengj/testvbs/data/for_analysis/2018_tight_for_analysis_single_muon_A.root";\n')
outfile_c.write('   TFile *file1 =new TFile(infilename);\n')
outfile_c.write('   TDirectory * dir = (TDirectory*)file1->Get("treeDumper");\n')

outfile_c.write('   TTreeReader fReader ;\n')
outfile_c.write('   fReader.SetTree("PKUCandidates", dir);\n')

for i in range(0, len(lines)):
    if '*Br' in lines[i]:
        if '_F' in lines[i]:
           continue
        x = lines[i].split(':')
        branch = x[1].split(' ')
        value_pre = x[2].split(' ')
        value = value_pre[1].split('/')
        print branch[0] + ' ' + value[0] + ' ' + value[1]
        #print branch + value
        data_type, data_array_or_not = '', ''
        if '[' in value[0]:
            data_array_or_not = 'Array'
        else:
            data_array_or_not = 'Value'

        if value[1] == 'I':
            data_type = 'Int_t'
        if value[1] == 'D':
            data_type = 'Double_t'
        if value[1] == 'O':
            data_type = 'Bool_t'
        if value[1] == 'F':
            data_type = 'Float_t'     
    
        outfile_h.write(data_type + ' m_' + value[0] + ';\n')
        outfile_c.write('   TTreeReader'+data_array_or_not+'<'+data_type+'>    '+branch[0]+'  = {fReader, "'+branch[0]+'"};'  +'\n')

        


outfile_c.write('   Long64_t maxEntries = fReader.GetEntries(false);\n\n')
outfile_c.write('   int n = 0; \n')
outfile_c.write('   while (fReader.Next()) {\n\n\n')
outfile_c.write('      cout<<"event num : "<< n<<" "<<*nevent<<"   "<<*run<<"   "<<*ls<<endl;\n')
outfile_c.write('      n++;\n\n\n')
outfile_c.write('   }\n\n')
outfile_c.write('   string   time_end = getTime();\n')
outfile_c.write('   cout<<endl<<endl<<"time start : "<<time_start<<endl<<"time end   : "<<time_end<<endl;\n')

outfile_c.write('}\n')
