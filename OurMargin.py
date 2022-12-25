
import heapq as heap
from  LRM import LRM
from DistanceToPi import distanceToPi
from BlomLB import blomLB
from OurLB import OurLB

class OurMargin:
    def __init__(self):
        self.nodeExplored = 0
        self.numLP = 0

    def marginOurs(self,C,B,cw):
        Q = []
        U = LRM(B,C)
        print("upper bound = ",U)
        C_w = set(C)-{cw}
        for c in C_w:
            self.nodeExplored = self.nodeExplored + 1
            pi = [c]
            l = blomLB(B,C,pi)
            if l < U:
                heap.heappush(Q, [l,pi])

        while(len(Q) != 0 ):
            l,pi = heap.heappop(Q)
            if l < U:
                U = min(U,self.expandMOurs(l,pi,U,Q,C,B))

        return U

    def expandMOurs(self,l,pi,U,Q,C,B):
        if len(pi) == len(C):
            m = OurLB(B, pi)
            if m >= U:
                return U
            self.numLP = self.numLP + 1
            return distanceToPi(B,pi)
        else:
            C_pi = set(C) - set(pi)
            for c in C_pi:
                self.nodeExplored = self.nodeExplored + 1
                pi_prime = list(pi)
                pi_prime.insert(0,c)
                l_new = blomLB(B,C,pi_prime)
                l_prime = max(l,l_new)
                if l_prime < U:
                    m = OurLB(B,pi_prime)
                    l_prime = max(l_prime,m)
                if l_prime < U:
                    heap.heappush(Q,[l_prime,pi_prime])
        return U
