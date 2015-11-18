import types

shop = {
        'byke':int(800),
        'iphone':int(5000),
        'milk':int(80),
        'coffee':int(58)
        }

while True:
    salary= raw_input('please input your salary:')
    
    try:
        salary= int(salary)
    except  ValueError as e:
        print e
    if type(salary) is not types.IntType:
        print 'input correct datatype'
        continue
    
    else:
        break

gouwuche = []   
while True:
            for i in shop:
                print i,shop[i]
            
            i= raw_input('please input the thing you waant to buy:') 
            if i in shop:
                
                if salary >= min(shop.values()):
                    salary =  salary - shop[i]
                    if salary >= 0:
                        gouwuche.append(i)
                        print 'remine money is %s:'% salary 
                    else:
                        salary = salary + shop[i]
                        print "you haven't enough  money pay for the shangpin,try other shangpin"
                        print 'remine money is %s:'% salary
                else:
                    print 'you have not enoghu money'
                    #打印购物车商品的名称和数量
                    gouwu = []
                    [gouwu.append(s) for s in gouwuche if s not in gouwu]
                    for shangpin in gouwu:
                        print shangpin,gouwuche.count(shangpin)
                    
                    print 'remaining money is : %s' %salary
                    break
            else:
                print  'input not in shop_list' 
