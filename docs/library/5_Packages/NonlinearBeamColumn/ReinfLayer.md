# ReinfLayer

```cpp

// $Revision: 1.3 $
// $Date: 2003-02-14 23:01:37 $
// $Source: /usr/local/cvs/OpenSees/SRC/material/section/repres/reinfLayer/ReinfLayer.h,v $
                                                                        
                                                                        
// File: ReinfLayer.h
// Written by Remo M. de Souza
// December 1998

#include <OPS_Globals.h>

class ReinfBar;

class ReinfLayer
{
  public:

    ReinfLayer();
    virtual ~ReinfLayer();
    
    // edition functions

    virtual void setNumReinfBars     (int numReinfBars)        = 0;
    virtual void setMaterialID       (int materialID)          = 0;
    virtual void setReinfBarDiameter (double reinfBarDiemater) = 0;
    virtual void setReinfBarArea     (double reinfBarArea)     = 0;

    // reinforcing layer inquiring functions
    
    virtual int         getNumReinfBars     (void) const = 0;
    virtual int         getMaterialID       (void) const = 0; 
    virtual double      getReinfBarDiameter (void) const = 0;
    virtual double      getReinfBarArea     (void) const = 0;
    virtual ReinfLayer *getCopy             (void) const = 0;
    virtual ReinfBar   *getReinfBars        (void) const = 0;     
   
    virtual void Print(OPS_Stream &s, int flag =0) const = 0;   
    friend OPS_Stream &operator<<(OPS_Stream &s, const ReinfLayer &ReinfLayer);    
    
  protected:
    
  private:
};


#endif

```
