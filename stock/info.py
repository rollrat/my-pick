import FinanceDataReader as fdr

df = fdr.DataReader('091990')

print(df)
df.to_csv('asdf', sep='\t', encoding='utf-8')
for x in df:
    print(x)
