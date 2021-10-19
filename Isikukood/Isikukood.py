ik=''
ikoodid=list()
arvud=list()
print('Isikukoodi analüüz: '.center(50,'_'))
#while len(ik)!=11 or ik.isdigit()!=True or int(list(ik)[0]) not in [1,2,3,4,5,6,7] or int(list(ik)[3]+list(ik)[4])<=0 or int(list(ik)[3]+list(ik)[4])>13:
#    pass test
while len(ik)!=11 or ik.isdigit()!=True:
    try:
        ik=input('Isikukood: ')
    except ValueError:
        print('Viga')
print('Esimene sümbol: ')
ik_list=list(ik)
if int(ik_list[0]) not in [1,2,3,4,5,6,7]:
    print(ik_list[0], ' - vale number')
else:
    print(ik_list[0], ' - õige number')
    kuu=ik_list[3]+ik_list[4]
    kuu=int(kuu)
    if kuu>0 and kuu<13:
        print(ik_list[3],ik_list[4], 'õige andmed')
        paev=int(ik_list[5]+ik_list[6])
        if int(ik_list[0])==1 or int(ik_list[0])==2:
            aasta=int('18'+ik_list[1]+ik_list[2])
        elif int(ik_list[0])==1 or int(ik_list[0])==4:
            aasta=int('19'+ik_list[1]+ik_list[2])
        elif int(ik_list[0])==1 or int(ik_list[0])==6:
            aasta=int('20'+ik_list[1]+ik_list[2])
        if kuu in [1,3,5,7,8,10,12] and paev>0 and paev<32:
            print(ik_list[5],ik_list[6], 'õige paev')
        elif (kuu in [2,4,6,9,11] and paev>0 and paev<31) or (kuu == 2 and paev>0 and paev<29):
            print(ik_list[5],ik_list[6], 'õige paev')
        elif aasta%4==0 and kuu==2 and paev>0 and paev<30:
            print(ik_list[5],ik_list[6], 'õige paev')
        else:
            print(ik_list[5],ik_list[6], 'valed päevad')
    else:
        print(ik_list[3],ik_list[4], 'valed andmed')

sum=0
for i in range(1,11):
    if i<10:
        sum+=i*int(ik_list[i-1])
    else:
        sum+=(i-9)*int(ik_list[i-1])
print('Sum = ',sum)
jaak=sum//11
print('jaak1: ', jaak)
if jaak==10:
    sum=0
    for i in range(3,13):
        if i<=9:
            sum+=i*int(ik_list[i-1])
            print('Ty tut')
        else:
            sum+=(i-9)*int(ik_list[i-1])
            print('Teper tut')
    print('jaak2: ', jaak)
    jaak=sum//11
jaak=sum-jaak*11
print('Kontrollnumber: ', jaak)
if jaak ==int(ik_list[10]):
    print('Isikukood on õige')
    ikoodid.append(ik)
    print(ikoodid)
else:
    print('Isikukood on vale')
    arvud.append(ik)
    print(arvud)


#MarinaOleinik/Isikukood

