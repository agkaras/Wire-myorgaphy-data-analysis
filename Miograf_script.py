import pandas as pd 
''' Calculation of results from wire myography recorded with LabChart and exported as txt file.
Input comments included in this script that should be used during recording or changed in result file:
#* KCl30 
#* P1
#* KCl60 
#* P2 
#* Phe3uM
#* PP 
#* Phe0,1
#* Ach0,001 
#* Ach0,01 
#* Ach0,1 
#* Ach1 
#* Ach10 
#* P3 
#* 2Phe0,1 
#* SNP0,001 
#* SNP0,01 
#* SNP0,1 
#* SNP1
#* K 
'''
#insert the path to txt file with results
input_file = '~/Documents/PHD/OneDrive - Uniwersytet Jagielloński/experiments/miograf/C57_2y_IL1b/C57_3m_22m_IL1b_24h_01-02-23_1.txt'

df = pd.read_csv(input_file, sep='\t', decimal=',', skiprows=9, header=None, names = ['t',1,2,3,4,5,6,7,8,'komentarz'], index_col=9)

#preview of commented lines to check if comments match in case of error



#contraction induced with 60mM KCl 
x60 = df.index.get_loc((df.loc['#* KCl60 ']).name) - 1
wyniki['KCl60_skurcz'] = (df.loc['#* KCl60 ': '#* P2 '].max()) - df.iloc[x60]

#maximal contraction induced with 3uM phenylephrine
mPhe =  df.index.get_loc((df.loc['#* Phe3uM ']).name) - 1
wyniki['Phe_max_skurcz'] = (df.loc['#* Phe3uM ': '#* PP '].max()) - df.iloc[mPhe]

#submaximal contraction induced with 0.1-1μM phenylephrine 
xPhe = df.index.get_loc((df.loc['#* subPhe ']).name) - 1
wyniki['Phe_skurcz'] = (df.loc['#* subPhe ': '#* Ach0,001 '].max()) - df.iloc[xPhe]

#relaxation to cumulative concentrations of acetylcholine 0.001–10 μM
yAch = df.index.get_loc((df.loc['#* Ach0,001 ']).name) - 1
wyniki['Ach0,001'] = df.iloc[yAch] - (df.loc['#* Ach0,001 ':'#* Ach0,01 '].min())
wyniki['Ach0,01'] = df.iloc[yAch] - (df.loc['#* Ach0,01 ':'#* Ach0,1 '].min())
wyniki['Ach0,1'] = df.iloc[yAch] - (df.loc['#* Ach0,1 ':'#* Ach1 '].min())
wyniki['Ach1'] = df.iloc[yAch] - (df.loc['#* Ach1 ':'#* Ach10 '].min())
wyniki['Ach10'] = df.iloc[yAch] - (df.loc['#* Ach10 ':'#* P3 '].min())

#second submaximal contraction induced with 0.1-1μM phenylephrine
yPhe2 = df.index.get_loc((df.loc['#* 2subPhe ']).name) - 1
wyniki['Phe_skurcz2'] = (df.loc['#* 2subPhe ': '#* SNP0,001 '].max()) - df.iloc[yPhe2]

#relaxation to cumulative concentrations of SNP 0.001–1 μM
ySNP = df.index.get_loc((df.loc['#* SNP0,001 ']).name) - 1
wyniki['SNP0,001'] = df.iloc[ySNP] - (df.loc['#* SNP0,001 ':'#* SNP0,01 '].min())
wyniki['SNP0,01'] = df.iloc[ySNP] - (df.loc['#* SNP0,01 ':'#* SNP0,1 '].min())
wyniki['SNP0,1'] = df.iloc[ySNP] - (df.loc['#* SNP0,1 ':'#* SNP1 '].min())
wyniki['SNP1'] = df.iloc[ySNP] - (df.loc['#* SNP1 ':'#* K '].min())

#calculation of relaxation for acetylcholine as % of contraction
wyniki['%Ach0,001'] = wyniki['Ach0,001'] *100 / wyniki['Phe_skurcz']
wyniki['%Ach0,01'] = wyniki['Ach0,01'] *100 / wyniki['Phe_skurcz']
wyniki['%Ach0,1'] = wyniki['Ach0,1'] *100 / wyniki['Phe_skurcz']
wyniki['%Ach1'] = wyniki['Ach1'] *100 / wyniki['Phe_skurcz']
wyniki['%Ach10'] = wyniki['Ach10'] *100 / wyniki['Phe_skurcz']

#calculation of relaxation for SNP as % of contraction
wyniki['%SNP0,001'] = wyniki['SNP0,001'] *100 / wyniki['Phe_skurcz2']
wyniki['%SNP0,01'] = wyniki['SNP0,01'] *100 / wyniki['Phe_skurcz2']
wyniki['%SNP0,1'] = wyniki['SNP0,1'] *100 / wyniki['Phe_skurcz2']
wyniki['%SNP1'] = wyniki['SNP1'] *100 / wyniki['Phe_skurcz2']



#export to excel file in chosen directory
wyniki.drop(labels='t', axis=0, inplace=True)
wyniki.to_excel('~/Documents/PHD/OneDrive - Uniwersytet Jagielloński/experiments/miograf/C57_2y_IL1b/C57_3m_22m_IL1b_24h_01-02-23_1.xlsx')
print(wyniki)
