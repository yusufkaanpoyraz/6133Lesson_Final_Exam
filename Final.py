#!/usr/bin/python

#Library for solutions
#Created by Kaan

print ("Which solution would you like to prepare? \n 10X PBS(1),\n 1X PBS(2),\n 1X PBSTX(3),\n Sodium Citrate(4),\n TBS(5),\n Boric Acid(6),\n %20 Sucrose/EDTA(7),\n %30 Sucrose / %20 EDTA(8),\n %20 Sucrose / %7,5 Gelatine(9),\n Clarity(10),\n Pestil Sterilization(11),\n Genotyping from fins(12),\n iScript cDNA Synthesis Kit(13),\n Concentration Calculator(19),\n Molarity Calculator(20)\n")
num = input("Enter number:")
if num == "1" :
    print ("10X PBS = For 1 L\n80 g NaCl,\n2 g KCl,\n14,4 g Na2HPO4\n2,4 g KH2PO4\n*Adjust pH 7,4 by adding HCl")
if num == "2" :
    print ("1X PBS = For 1 L\n100 mL 10X PBS\n900 mL dH2O")
if num == "3" :
    print ("1X PBSTX = For 1 L\n100 mL\n10X PBS\n900 mL dH20\n3 mL TritonX")
if num == "4" :
    print ("Sodium Citrate = for 500 mL\n1,47 g Tri-Sodium citrate(dihydrate)\n0,25 g Twen20\n*Store this solution at RT for 3 months.")
if num == "5" :
    print ("TBS = For 1 L\n6.05 g Tris\n8.76 g NaCl\n*Adjust pH to 7.5 with 1 M HCl")
if num == "6" :
    print ("Boric Acid = for 400 mL\n2,5 g Boric acid\n400 mL dH20\n*Adding acid to water!")
if num == "7" :
    print ("%20 Sucrose / EDTA = for 200 mL in PB\n40 g Sucrose\n40 g EDTA")
if num == "8" :
    print ("%30 Sucrose / %20 EDTA = for 200 mL in PB\n60 g Sucrose\n40 g EDTA")
if num == "9" :
    print ("%20 Sucrose / %7,5 Gelatine = for 400 mL in PB\n80 g Sucrose\n30 g Gelatine")
if num == "10" :
    print ("Clarity = for 250 mL\n3,10 g boric acid\n10 g SDS\n0,21 g Lithium hydroxide")
if num == "11" :
    print ("%1 SDS in Absolute EtOH or 0,1M NaOH / 1mM EDTA in water")
if num == "12" :
    print ("1 fin into 50 uL DNA Extraction Buffer \n DNA Extraction Buffer: \n (10mM Tris-HCl pH:8 \n 50mM KCl \n 0.3% NP4O \n 1 mM EDTA)\n 96 C 10-15 min \n Cool down \n Add proteinase K 2 uL \n Overnight 55 C \n 10 min 98 C")
if num == "13" :
    print ("4 uL Reaction Mix \n 1 uL Reverse Transcriptase \n Nuclease-free water VARIABLE \n RNA template VARIABLE")
if num == "19" :
    print ("Volume (mL)")
    volume = int(input ())
    print ("Molecular weight")
    molecular_weight = int(input ())
    print ("Weight (mg)")
    weight = int(input ())
    mol = weight / molecular_weight / volume
    print ("Concentration of the solution is:  ", mol, " M")
if num == "20" :
    print ("First concentration(M1):")
    M1 = int(input())
    print ("Final concentration(M2):")
    M2 = int(input())
    print ("Final volume(V2):")
    V2 = int(input())
    V1 = (M2*V2) / M1
    print ("First volume(V1): ", V1 )
