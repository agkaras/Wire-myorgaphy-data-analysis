
import pandas as pd
#insert the path to txt file with results
input_file = '~/Library/CloudStorage/OneDrive-UniwersytetJagielloński/experiments/miograf/old_PPP/C57BL_28m_3m_6-AN_DHEA_5-11-24.txt'

df = pd.read_csv(input_file, sep='\t', decimal=',', skiprows=9, header=None, names=['t',1,2,3,4,5,6,7,8,'komentarz'], index_col=9)


#preview of commented lines to check if comments match in case of error
dfff = df.filter(like='#*', axis=0)
print(dfff)

#creating empty result table for adding calculated values
results = pd.DataFrame()

#contraction induced with 60mM KCl
x60 = df.index.get_loc((df.loc['#* KCl60 ']).name) - 1 #value 1s before the comment
results['KCl60_con'] = (df.loc['#* KCl60 ': '#* P2 '].max()) - df.iloc[x60]

#maximal contraction induced with phenylephrine (3μM)
mPhe =  df.index.get_loc((df.loc['#* Phe3uM ']).name) - 1
results['Phe_max'] = (df.loc['#* Phe3uM ': '#* PP '].max()) - df.iloc[mPhe]

#submaximal contraction induced with 0.1-1μM phenylephrine
xPhe = df.index.get_loc((df.loc['#* subPhe ']).name) - 1
results['Phe_con'] = (df.loc['#* subPhe ': '#* Ach0,001 '].max()) - df.iloc[xPhe]

#relaxation to cumulative concentrations of acetylcholine 0.01–10 μM
yAch = df.index.get_loc((df.loc['#* Ach0,001 ']).name) - 1 #value 1s before the comment
results['Ach0,001'] = df.iloc[yAch] - (df.loc['#* Ach0,001 ':'#* Ach0,01 '].min())
results['Ach0,01'] = df.iloc[yAch] - (df.loc['#* Ach0,01 ':'#* Ach0,1 '].min())
results['Ach0,1'] = df.iloc[yAch] - (df.loc['#* Ach0,1 ':'#* Ach1 '].min())
results['Ach1'] = df.iloc[yAch] - (df.loc['#* Ach1 ':'#* Ach10 '].min())
results['Ach10'] = df.iloc[yAch] - (df.loc['#* Ach10 ':'#* P3 '].min())

#third submaximal contraction induced with 0.1-1μM phenylephrine
yPhe = df.index.get_loc((df.loc['#* 2subPhe ']).name) - 1
results['Phe_con2'] = (df.loc['#* 2subPhe ': '#* SNP0,001 '].max()) - df.iloc[yPhe]

#second relaxation to cumulative concentrations of SNP 0.001–1 μM
ySNP = df.index.get_loc((df.loc['#* SNP0,001 ']).name) - 1
results['SNP0,001'] = df.iloc[ySNP] - (df.loc['#* SNP0,001 ':'#* SNP0,01 '].min())
results['SNP0,01'] = df.iloc[ySNP] - (df.loc['#* SNP0,01 ':'#* SNP0,1 '].min())
results['SNP0,1'] = df.iloc[ySNP] - (df.loc['#* SNP0,1 ':'#* SNP1 '].min())
results['SNP1'] = df.iloc[ySNP] - (df.loc['#* SNP1 ':'#* P4 '].min())

######################
#incubation with PPP inhibitors

#submaximal contraction induced with 0.1-1μM phenylephrine
zPhe = df.index.get_loc((df.loc['#* 3subPhe ']).name) - 1
results['3Phe_con'] = (df.loc['#* 3subPhe ': '#* 2Ach0,001 '].max()) - df.iloc[zPhe]

#relaxation to cumulative concentrations of acetylcholine 0.01–10 μM
zAch = df.index.get_loc((df.loc['#* 2Ach0,001 ']).name) - 1 #value 1s before the comment
results['2Ach0,001'] = df.iloc[zAch] - (df.loc['#* 2Ach0,001 ':'#* 2Ach0,01 '].min())
results['2Ach0,01'] = df.iloc[zAch] - (df.loc['#* 2Ach0,01 ':'#* 2Ach0,1 '].min())
results['2Ach0,1'] = df.iloc[zAch] - (df.loc['#* 2Ach0,1 ':'#* 2Ach1 '].min())
results['2Ach1'] = df.iloc[zAch] - (df.loc['#* 2Ach1 ':'#* 2Ach10 '].min())
results['2Ach10'] = df.iloc[zAch] - (df.loc['#* 2Ach10 ':'#* K '].min())

#calculation of relaxation for acetylcholine as % of Phe induced contraction
results['%Ach0,001'] = results['Ach0,001'] * 100 / results['Phe_con']
results['%Ach0,01'] = results['Ach0,01'] * 100 / results['Phe_con']
results['%Ach0,1'] = results['Ach0,1'] * 100 / results['Phe_con']
results['%Ach1'] = results['Ach1'] * 100 / results['Phe_con']
results['%Ach10'] = results['Ach10'] * 100 / results['Phe_con']

#calculation of relaxation for SNP as % of contraction
results['%SNP0,001'] = results['SNP0,001'] * 100 / results['Phe_con2']
results['%SNP0,01'] = results['SNP0,01'] * 100 / results['Phe_con2']
results['%SNP0,1'] = results['SNP0,1'] * 100 / results['Phe_con2']
results['%SNP1'] = results['SNP1'] * 100 / results['Phe_con2']

#calculation of relaxation for acetylcholine as % of Phe induced contraction
results['%2Ach0,001'] = results['2Ach0,001'] * 100 / results['3Phe_con']
results['%2Ach0,01'] = results['2Ach0,01'] * 100 / results['3Phe_con']
results['%2Ach0,1'] = results['2Ach0,1'] * 100 / results['3Phe_con']
results['%2Ach1'] = results['2Ach1'] * 100 / results['3Phe_con']
results['%2Ach10'] = results['2Ach10'] * 100 / results['3Phe_con']

#export to excel file in chosen directory
results.drop(labels='t', axis=0, inplace=True)
results.to_excel('~/Library/CloudStorage/OneDrive-UniwersytetJagielloński/experiments/miograf/old_PPP/C57BL_28m_3m_6-AN_DHEA_5-11-24.xlsx')
print(results)