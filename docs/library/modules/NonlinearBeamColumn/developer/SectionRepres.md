# SectionRepres

SectionRepres is an abstract base class and thus no objects of it's
type can be instantiated. It has pure virtual functions which must be
implemented in it's derived classes.

// Written by Remo M. de Souza
// November 1998


```cpp
// $Revision: 1.2 $
// $Date: 2003-02-14 23:01:37 $

// File: SectionRepres.h

#include <TaggedObject.h>

class SectionRepres: public TaggedObject
{
  public:

    // Section creation functions

    SectionRepres(int tag);    
        
    // Section edition functions

    virtual ~SectionRepres();
   
    // Section inquiring functions
     
    virtual int  getType(void) const = 0;
    friend OPS_Stream &operator<<(OPS_Stream &s, const SectionRepres &sectionRepres);    
    
  protected:
    
  private:
};

bool OPS_addSectionRepres(SectionRepres *newComponent);
SectionRepres *OPS_getSectionRepres(int tag);
void OPS_clearAllSectionRepres(void);

#endif

```
