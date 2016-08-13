import numpy as np
from numpy import linalg as la

#相似度计算，若inA,inB都是行向量


#欧式距离
def euclidsimilar(inA,inB):
    return 1.0/(1.0+la.norm(inA-inB))

#皮尔逊相关系数
def pearsonsimilar(inA,inB):
    if len(inA)<3:
        return 1.0
    return 0.5+0.5*np.corrcoef(inA,inB,rowvar=0)[0][1]

#余弦相似度
def cossimilar(inA,inB):
    inA = np.mat(inA)
    inB = np.mat(inB)
    num = float(inA*inB.T)
    denom = la.norm(inA)*la.norm(inB)
    return 0.5+0.5*(num/denom)

inA=np.array([1,2,3])
inB=np.array([2,4,6])
print(euclidsimilar(inA,inB))

print(pearsonsimilar(inA,inB))
print(cossimilar(inA,inB))

