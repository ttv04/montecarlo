import math
import numpy as np

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        out = ""
        for i in self.config:
            out += str(i)
        return out

    def __eq__(self, other):        
        return all(self.config == other.config)
    
    def __len__(self):
        return len(self.config)

    def on(self):
        """
        Return number of bits that are on
        """
        return np.sum(self.config)

    def off(self):
        """
        Return number of bits that are on
        """
        return len(self)-self.on()

    def flip_site(self,i):
        """
        Flip the bit at site i
        """
        try:
            self.config[i] = (self.config[i] + 1) % 2
        except ValueError:
            print("problem with i", i)
    
    def integer(self):
        """
        Return the decimal integer corresponding to BitString
        """
        out = 0
        for idx, i in enumerate(reversed(self.config)):
            if i==1:
                out += 2**idx
                # print(i, idx, i*(2**idx), out)
        return out
 
    def getBit(self, pos: int) -> int:
        return (self.config[pos])

    def set_config(self, s:list[int]):
        """
        Set the config from a list of integers
        """
        try:
            assert(len(s) == self.N)
        except:
            raise ValueError("provided config wrong size: ", len(s), " ")  
        self.config = s
        return

    def set_integer_config(self, dec:int):
        """
        convert a decimal integer to binary
    
        Parameters
        ----------
        dec    : int
            input integer
            
        Returns
        -------
        Bitconfig
        """
        digits_needed = math.ceil(math.log(dec+1,2))
        try:
            assert(self.N >= digits_needed)
        except:
            raise ValueError("not enough digits!")
            
        config = np.array([0 for i in range(self.N)])
        # bs = Bitconfig(digits)
    
        # for i in range(digits_needed):
        tmp = dec*1
        for i in reversed(range(self.N-digits_needed, self.N)):
            # print(tmp%2)
            config[i] = tmp%2
            tmp = tmp//2
        self.set_config(config)
        return 
    