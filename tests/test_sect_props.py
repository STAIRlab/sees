from opensees import section, patch
"""
This test validates section properties.

  __ __________________ __
 4   |    |  b   |    |
  __ |    |______|    |
     | a  |      | c  | 16
     |    |      |    |   
     |    |      |    |
     |____|      |____| __
     
     | 4  |  8   |  4 |
  

"""

def test():
    sect = section.FiberSection(areas=[
        patch.rect(vertices=[[-8,  0],[-4, 16]]),
        patch.rect(vertices=[[-4, 12],[ 4, 16]]),
        patch.rect(vertices=[[ 4,  0],[ 8, 16]]),
    ])

    assert sect.areas[0].ixc == 4*16**3/12
    assert sect.areas[1].ixc ==  8*4**3/12
    assert sect.areas[2].ixc == 4*16**3/12

    assert sect.centroid[1] == 9.2

    # centroid about x-x
    assert (14*8*4+8*2*16*4)/(16*8+4*8) == sect.centroid[1]

    #                           Ia        d      area         Ib
    assert sect.ixc == 2 * (4*16**3/12 + 1.2**2*(16*4)) + (8*4**3/12 + 4*8*4.8**2)





if __name__ == "__main__":
    test()

