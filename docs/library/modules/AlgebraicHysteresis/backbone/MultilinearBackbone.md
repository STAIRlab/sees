# Multilinear

`MultilinearBackbone` is a backbone defined by many points.

:::{apidoc="opensees.backbone.Multilinear"}
:::

## C++ Interface

```cpp
class MultilinearBackbone : public HystereticBackbone
{
 public:
  MultilinearBackbone(int tag, int numPoints, const Vector &e, const Vector &s);
    
 private:
  double *E;
  double *e;
  double *s;
  double *c;
  int numPoints;
};
```


Code developed by: <span style="color:blue">MHS</span>

Created: Aug 2000

