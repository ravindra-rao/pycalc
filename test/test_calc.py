'''
Created on Mar. 12, 2023

@author: wearo
'''

from yopycalc.calc import add

import sys
for i in sys.path:
    print(i)
    


def test_add():
    assert add(2,3) ==5
    print("add Function works correctly")

test_add()
# if __name__ == '__main__':
#     test_add()