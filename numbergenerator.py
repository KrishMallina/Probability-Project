class rand_num_gen:
    def __init__(self, a = 24693, c = 3517, K = 2**17, seed=1000):
        self.a = a
        self.c = c
        self.K = K
        self.x0 = seed

        self.x_prev = (self.a*self.x0+self.c)%self.K

    def  generate(self):
        self.x_prev = (self.a*self.x_prev+self.c)%self.K
        return self.x_prev
    
K = 2**17
lcg = rand_num_gen()
for i in range(52):
    print(lcg.generate()/K)