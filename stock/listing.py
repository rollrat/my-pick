import FinanceDataReader as fdr


stocks = fdr.StockListing('KOSPI')
# stocks = fdr.StockListing('KOSDAQ')

# for i, s in stocks.iterrows():
#     print(str(s['Symbol']), str(s['Name']))

with open('result.txt', 'w', encoding='utf-8') as f:
    for _, row in stocks.iterrows():
        f.write(str(row['Symbol']) + '\t' + str(row['Name']) + '\n')
