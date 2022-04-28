THIS INTERFACE IS GONNA CHANGE. 1) MOVABLE_OBJECT SO CAN RENDER IN
PARALLEL, 2) SET_MINMAX() and 3) ONLY ONE CALL TO GET RGB VALUES, i.e.
getRGB(value, &r, &g, &b)



# ColorMap 

```cpp
#include <earthquake/ColorMap.h>
```



class ColorMap







The ColorMap is an abstract class, it defines the interface all concrete
subclasses must provide. A ColorMap object is used to determine the
mapping between scalar quantities to be displayed in an image and the
rgb values that are displayed.

// Constructor






// Destructor






// Public Methods











Does nothing.




Does Noting.




To return the red intensity of the rgb triple for the scalar quantity
*value*.

To return the green intensity of the rgb triple for the scalar quantity
*value*.

To return the blue intensity of the rgb triple for the scalar quantity
*value*.
