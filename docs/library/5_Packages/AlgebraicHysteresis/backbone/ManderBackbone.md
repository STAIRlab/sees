# Mander

`ManderBackbone`, implements the concrete backbone function utilized
by Mander, Priestly, and Park (1988) and presented by Popovic.

:::{apidoc="opensees.backbone.Mander"}
:::

```cpp
class ManderBackbone : public HystereticBackbone
{
 public:
  ManderBackbone(int tag, double fc, double epsc, double Ec);

  double getStress (double strain) {

    if (strain > 0.0)
      return 0.0;
    
    strain *= -1;

    double oneOverepsc = 1.0/epsc;
    
    double x = strain*oneOverepsc;
    double Esec = fpc*oneOverepsc;
    
    double r = Ec/(Ec-Esec);
    
    return -fpc*(x*r)/(r-1.0+pow(x,r));
  }

 private:
  double fpc;
  double epsc;
  double Ec;
};
```

Code developed by: <span style="color:blue">MHS</span>
Created: Mar 2001

