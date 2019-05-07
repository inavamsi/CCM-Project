'''
Experiment
We generate random numbers, sort them and find rules that fit them.
We simulate this n number of times and find the most naturally occuring rules
'''



from scipy.stats import norm
import numpy as np
import random

def sp_gaussian(mean, var, error):
  if(int)(error)!= error:
    return None
  
  if error==0:
    return norm.cdf(1,mean,var) - norm.cdf(-1,mean,var)
  if error >0:
    return norm.cdf(error+1,mean,var) - norm.cdf(error,mean,var)
  if error <0:
    return norm.cdf(error,mean,var) - norm.cdf(error-1,mean,var)
    
# Populating H
max_bound=100
H ={}
#A = []
#M= []
A_list=[1,2,3,4,5,6,7,8,9,10]
M_list=[2,3]


#for i in A_list:
#  A.append(lambda x :(x+i))
  
#for i in M_list:
#  M.append(lambda x :(x*i))
  
def generate_H(max_bound,A_list,M_list):
  H={}

  for i in range(0,len(A_list)):
    H['A'+str(A_list[i])] = {}
    for j in range(1,max_bound):
      if j +A_list[i]  <=max_bound:
        H['A'+str(A_list[i])][j]=j +A_list[i]     #A[i](j)
        #print('A'+str(A_list[i]), " ", j ," ", A[i](j))


  for i in range(0,len(M_list)):
    H['M'+str(M_list[i])] = {}
    for j in range(1,max_bound):
      if j*M_list[i] <=max_bound:
        H['M'+str(M_list[i])][j]= j*M_list[i]     #M[i](j)
        #print('M'+str(M_list[i]), " ", j ," ", M[i](j))
        
  return H
      
def generate_H_comb(max_bound,A_list,M_list):
  H={}

  for i in range(0,len(A_list)):
    H['A'+str(A_list[i])] = {}
    for j in range(1,max_bound):
      if j +A_list[i]  <=max_bound:
        H['A'+str(A_list[i])][j]=j +A_list[i]     

  for i in range(0,len(M_list)):
    H['M'+str(M_list[i])] = {}
    for j in range(1,max_bound):
      if j*M_list[i] <=max_bound:
        H['M'+str(M_list[i])][j]= j*M_list[i]    
        
  for m in range(0,len(M_list)):
    for a in range(0,len(A_list)):
      H['M'+str(M_list[m])+'A'+str(A_list[a])] = {}
      for j in range(1,max_bound):
        if j*M_list[m] +A_list[a]  <=max_bound:
          H['M'+str(M_list[m])+'A'+str(A_list[a])][j]=j*M_list[m] +A_list[a]
        
  return H
  
# Priors

def Prior(H,hef):
  (a,m,c)=hef
  tot=a+m+c
  a=a/tot
  m=m/tot
  c=c/tot
  
  Prior = {}
  a_counter=0
  m_counter=0
  c_counter=0
  for h in H.keys():
    if len(h)==2:
      if h[0]=='A':
        a_counter+=1
      else:
        m_counter+=1
    else:
      c_counter+=1
      
  for h in H.keys():
    if len(h)==2:
      if h[0]=='A':
        Prior[h] = a/a_counter
      else:
        Prior[h] = m/m_counter
    else:
      Prior[h] = c/c_counter
    
  return Prior
  
# take list as inpit and return list of tuples
def split_into_pairs(l):
  pairs=[]
  for i in range(0,len(l)-1):
    pairs.append((l[i],l[i+1]))
  return pairs
  
def prob_pair(pair,h,noise_mean,noise_var):
  (x1,x2)=pair
  if x1 in H[h].keys():
    error = x2 - H[h][x1]
    return sp_gaussian(noise_mean,noise_var,error)
  return 0
  
# Likelihood

def likelihood(H,D,noise_mean,noise_var):
  L_D={}

  for h in H.keys():
    L_D[h]=1
    for pair in split_into_pairs(D):
      L_D[h]=L_D[h]*prob_pair(pair,h,noise_mean,noise_var)
  return L_D

#bayes theorem

def posterior(H,Lhood,Prior):
  Posterior = {}

  scale =0
  for h in H.keys():
    scale+=Prior[h] * Lhood[h]

  for h in H.keys():
    Posterior[h]= Prior[h] * Lhood[h] / scale
  
  return Posterior
  
# Most likely hypothesis list

def most_likely_h(P, threshold):
  sorted_P = sorted(Post, key=Post.__getitem__, reverse=True)
  
  relevant=[]
  for i in sorted_P:
    if (P[sorted_P[0]] - P[i])/P[sorted_P[0]] <= threshold :
      relevant.append(i)
      
  return relevant
 
def main(n):
  #finding patterns in randomness
  noise_mean=0
  noise_var=0.66          # variance of noise, to set variance use first cell as reference
  threshold = 0.9999      # for full list set threshold = 1, foronly top elemnt set thrshiold =0


  max_bound=310
  A_list=[1,2,3,4,5,6,7,8,9,10]
  M_list=[2,3]
  #H=generate_H(max_bound,A_list,M_list)
  H=generate_H_comb(max_bound,A_list,M_list)
  hef=(5,4,1)            # ratio of prior for (+, x , comb)

  Prior_dist=Prior(H,hef)

  Ctr={}
  for h in H.keys():
    Ctr[h]=0

  for t in range(0,n):
    D=[]
    for i in range(0,5):
      D.append(random.randint(0,50))

    D.sort()

    Lhood=likelihood(H,D,noise_mean,noise_var)
    Post =posterior(H,Lhood,Prior_dist)
    for h in H.keys():
      if not np.isnan(Post[h]):
        Ctr[h]+=Post[h]



  top = most_likely_h(Ctr, 0.9)

  for h in top:
    print(h," : ",Ctr[h])
      
  
main(1000)
