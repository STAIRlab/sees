# Claudio Perez
# October 2021
from math import sin, cos

import opensees
from opensees.units.english import ft, deg

def assembly(**kwds):
    """
    # Painter street overcrossing

    ```
         ^ y
         |      146    |    119'   |
       _________________________________
       #~o______________-o _________o~## ___
       ##\           || ||         /####  | 17'
       z .\__________|| ||________/#####------> x
       ##############o##o###############
    ```

    - This model assumes linear horizontal and vertical alignment
      curves
    - Reinforcement is ignored and gross section properties are used
      in the modeling of the deck.

    """

    skew_angle = 38.9*deg
    skew_x     = sin(skew_angle) * 19*ft
    skew_z     = cos(skew_angle) * 19*ft
    foundation_2_elev = (3.5/2 + 102) * ft
    vert_gird_offset = 32

    Height_column_to_soffit = 24.0*ft
    H = Height_column_to_soffit + vert_gird_offset


    assm = opensees.model(ndm=3, ndf=6,
      # Nodes
      nodes = {
      #     label        [      x             y          z
          "abut_1":      [     0.0,           H,        0.0],
          "abut_3":      [265.0*ft,           H,        0.0],
          "bent_top":    [146.0*ft,           H,        0.0],
          "bent_top_nw": [146.0*ft-skew_x,    H,     skew_z],
          "bent_bot_nw": [146.0*ft-skew_x,  0.0*ft,  skew_z],
          "bent_top_se": [146.0*ft+skew_x,    H,    -skew_z],
          "bent_bot_se": [146.0*ft+skew_x,  0.0*ft, -skew_z]
      },

      # Boundaries
      zeros = [
          #[["bent_bot_nw", "bent_bot_se"], [1, 1, 1, 1, 1, 1]]
        [["bent_bot*", "abut_*"], [1, 1, 1, 1, 1, 1]]
      ],

      # Zero-length connections
      conns = [
      #     type                nodes        dofs
          ["abutment", ["abut_3", "abut_1"],  []]
      ],

      # Structural Elements
      elems = [
      #     type          inode             jnode
          ["girder",   ["abut_1",        "bent_top"   ]],
          ["column",   ["bent_bot_nw",   "bent_top_nw"]],
          ["column",   ["bent_bot_se",   "bent_top_se"]],
          ["girder",   ["bent_top",      "abut_3"     ]],
          ["link",     ["bent_top_nw",   "bent_top"   ]],
          ["link",     ["bent_top_se",   "bent_top"   ]],
      ]
    )
    return assm

import opensees.emit

print(opensees.emit.JSON(assembly()).dump())




