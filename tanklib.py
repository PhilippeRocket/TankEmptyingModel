# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:37:53 2023

@author: Philippe.Lott
"""

import sys

class myTank:
    def __init__(self, gas, P0, T0, V = None, n0 = None):
        """
        
        """
        self.P0 = P0
        self.T0 = T0
        self.T_ = [self.T0]
        self.P_ = [self.P0]
        self.gas = gas
        if V is None and n0 is None:
            print("Non-Physical tank definition")
            sys.exit()
        elif V is None:
            self.n0=n0
            self.V = self.gas.Volume(self.P0,self.T0,self.n0)
        elif n0 is None:
            self.V = V 
            self.n0 = self.gas.Moles(self.P0,self.T0,self.V)         
        else:
            print("Non-Physical tank definition")
            sys.exit()
        self.n0 = n0
        self.P = self.P0
        self.T = self.T0
        self.n = self.n0
            
    def inner_loop(self,dn,err0=1e-6,ct0=100):
        self.n = self.n-dn
        # Setting the initialization of the inner loop
        NewT = self.T
        NewP = self.P
        
        # Setting up the error and the max iterations
        err = 1
        ct = 0        
        while err > err0 and ct<ct0:
            # Compute P based on T at the previous iteration & Perfect Gas Eq
            #NewP1 = n2*R*NewT/V
            NewP1 = self.gas.Pressure(NewT,self.n,self.V)
            # Compute T based on Computed P and the isentropic equations
            #NewT1 = T0*(NewP1/P0)**((g-1)/g)
            NewT1 = self.gas.Isen_Temperature(self.T, self.P, NewP1)
            # Evalaute the error between the current and previous step
            err = abs(NewT1-NewT) + abs(NewP1-NewP)
            #Update Values of T & P for the step
            NewT = NewT1
            NewP = NewP1
            # Update counter
            ct+=1 
        return NewT,NewP    

    def iterate(self,dn):
        for d in dn:
            nT,nP = self.inner_loop(d)
            self.T_.append(nT)
            self.P_.append(nP)
            self.T=nT
            self.P=nP