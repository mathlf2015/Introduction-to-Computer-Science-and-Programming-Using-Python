def nfruits(f_dic,f_str):
    assert len(f_dic)>0
    for each in range(len(f_str)):
        if each != len(f_str)-1:
            for i in f_dic:
                if i==f_str[each]:
                    f_dic[i]-=1
                else: f_dic[i]+=1
        else:
            f_dic[f_str[each]]-=1
    return max(f_dic.values())
#print(nfruits({}, 'SSSSS'))
#迭代
def nfruits(fruits,eaten):
    assert len(fruits), 'Python will starve to death. RIP!'
    assert all(fruit in fruits.keys() for fruit in eaten), 'Python doesn\'t want that! Throw it away!'
    assert all(fruit >= 0 for fruit in fruits.itervalues()), "Pythin has no fruits of that kind!"
    if len(eaten) <= 1:
        fruits[eaten] -= 1
        return max(fruits.itervalues())
    else:
        fruits = {key:value+1 for key, value in fruits.iteritems()}
        fruits[eaten[0]] -= 2
        return nfruits(fruits,eaten[1:])
