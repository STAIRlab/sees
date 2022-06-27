# Patch


   Written by Remo M. de Souza
   December 1998


```cpp
// $Revision: 1.2 $
// $Date: 2003-02-14 23:01:36 $
// $Source: /usr/local/cvs/OpenSees/SRC/material/section/repres/patch/Patch.h,v $

// File: Patch.h

#ifndef Patch_h 
#define Patch_h 


#include <OPS_Globals.h>

class Cell;

class Patch
{
  public:

    Patch();
    virtual ~Patch();
    
    // edition functions

    virtual void setMaterialID (int materialID) = 0;
    
    // inquiring functions

    virtual int     getMaterialID (void) const = 0; 
    virtual int     getNumCells   (void) const = 0;
    virtual Cell  **getCells      (void) const = 0;
    virtual Patch  *getCopy       (void) const = 0;

    virtual void Print(OPS_Stream &s, int flag =0) const =0;   
    friend OPS_Stream &operator<<(OPS_Stream &s, const Patch &patch);    

  protected:
    
  private:
};


#endif

```
