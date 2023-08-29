# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:36:18 2023

@author: Philippe.Lott
"""

class myPerfectGas:
    def __init__(self,g,Cp,Cv):
        self.g = g
        self.R = 8.3144598
        self.Cp = Cp
        self.Cv = Cv
        
    def Volume(self,P,T,n):
        V = n*self.R*T/P
        return V
    
    def Pressure(self,T,n,V):
        P = n*self.R*T/V
        return P
    
    def Temperature(self,P,n,V):
        T = P*V/(n*self.R)
        return T
    
    def Moles(self,P,T,V):
        n = P*V/(self.R*T)
        return n
    
    def Isen_Temperature(self,T,P1,P2):
        NewT1 = T*(P2/P1)**((self.g-1)/self.g)
        return NewT1

    def Isen_Pressure(self,P,T1,T2):
        NewP1 = P*(T2/T1)**((self.g)/(self.g-1))
        return NewP1
    
class myVdWGas(myPerfectGas):
    def __init__(self,g,Cp,Cv,a,b):
        super().__init__(g,Cp,Cv) 
        self.a = a
        self.b = b
        
    def Volume(self,P,T,n):
        #V = n*self.R*T/P
        V = n*((self.R*T)**3)/(P*((self.R*T)**2)+n*self.b)
        return V
    
    def Pressure(self,T,n,V):## OK
        #P = n*self.R*T/V
        P = (n*self.R*T)/(V-n*self.b)-self.a*n**2/(V**2)
        return P
    
    def Temperature(self,P,n,V): ## OK
        T = (P+self.a*n**2/(V**2))*(V-n*self.b)/(n*self.R)
        return T
    
    def Moles(self,P,T,V):
        n = P*V/(self.R*T)
        return n
    
    #def Isen_Temperature(self,T,P1,P2):
    #    NewT1 = T*(P2/P1)**((self.g-1)/self.g)
    #    return NewT1

    #def Isen_Pressure(self,P,T1,T2):
    #    NewP1 = P*(T2/T1)**((self.g)/(self.g-1))
    #    return NewP1    