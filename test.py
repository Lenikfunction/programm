catalog = {

}
user = input('введите строку__').replace(',','').replace('.','').lower().split()
for el in user:
    if not el in catalog:
        catalog[el] = 1
    else:
        catalog[el] += 1
for k in catalog:
    print(k,':',catalog[k])