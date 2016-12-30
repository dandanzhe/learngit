def mix(s1, s2):
    l1,num1,l2,num2=[],{},[],{}
    res=[]
    result=""
    for i in s1:
        l1.append(i)
    for i in s2:
        l2.append(i)
    m1=set(l1)
    m2=set(l2)
    for i in m1:
        num1[i]=l1.count(i)
    for i in m2:
        num2[i]=l2.count(i)
    for key1,val1 in num1.items():
        for key2,val2 in num2.items():
            if key1 not in s2 and val1>1 and key1 in "qwertyuiopasdfghjklzxcvbnm"and ([-val1,"1",key1] not in res):
                res.append([-val1,"1",key1])
            if (key2 not in s1 )and val2>1 and key2 in "qwertyuiopasdfghjklzxcvbnm" and ([-val2,"2",key2] not in res):      
                res.append([-val2,"2",key2])
            if key1==key2 and key1 in "qwertyuiopasdfghjklzxcvbnm":
                if val1==val2 and val1!=1:
                    res.append([-val1,"=",key1])
                if val1>val2:
                    res.append([-val1,"1",key1])
                if val1<val2:
                    res.append([-val2,"2",key1])
    res=sorted(res)
    for i in range(len(res)):
        result=result+res[i][1]+":"+(-res[i][0])*res[i][2]+"/"
    return result[:-1]
print mix(" In manIy langu::ages", " there's a pair of functions")


