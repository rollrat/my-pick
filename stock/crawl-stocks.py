import FinanceDataReader as fdr

with open('kosdaq.txt', 'r') as f:
    lines = f.readlines()
    length = len(lines)
    count = 0
    for l in lines:
        try:
            sn = l.split('\t')[0]
            n = l.split('\t')[1].strip()
            if n.endswith('풋'):
                continue
            elif n.endswith('콜'):
                continue

            df = fdr.DataReader(sn)
            df.to_csv('result-kosdaq/' + sn, sep='\t', encoding='utf-8')
            print('[' + str(count) + '/' + str(length) + ']')
        except:
            print('err: ' + l)
        finally:
            count += 1
