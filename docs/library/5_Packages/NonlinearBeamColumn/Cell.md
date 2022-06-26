# Cell

// Written by Remo M. de Souza
// December 1998



```cpp
// $Date: 2003/02/14 23:01:36 $
// $Source: /usr/local/cvs/OpenSees/SRC/material/section/repres/cell/Cell.h,v $
                                                                        
                                                                        
// File: Cell.h
//
#ifndef Cell_h 
#define Cell_h 

#include <OPS_Globals.h>

class Vector;

class Cell
{
  public:

    Cell();
    virtual ~Cell();
    
    // edition functions

    // reinforcing bar inquiring functions
    
    virtual        double getArea              (void) const = 0;
    virtual        double getdValue              (void) const = 0;
    virtual const  Vector &getCentroidPosition (void) = 0;
 
    virtual void   Print(OPS_Stream &s, int flag =0) const = 0;   
    friend OPS_Stream &operator<<(OPS_Stream &s, const Cell &Cell);    
    
  protected:
    
  private:
};


#endif

```
