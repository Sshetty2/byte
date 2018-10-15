import pprint

def currency_conversion(file):
    with open(file, 'r') as f:
        document = f.readlines()

    currency_list = []
    currencyObj = {}
    for row in document:
        currencyObj["symbol"] = row.split()[0]
        currencyObj["rate"] = row.split()[1]
        currency_list.append(dict(currencyObj))
        # currency_list.append(currencyDic)
    print(currency_list)



print(currency_conversion("currency.txt"))
