with open('AT_FINAL.txt', encoding = 'utf-8') as vstup:
    radky = vstup.readlines()


rozdelene_radky = [radek.replace('\t',';') for radek in radky]

#print(rozdelene_radky)

with open("AT_FINAL.csv", mode='a', encoding='utf-8') as vystup:
    vystup.writelines(rozdelene_radky)