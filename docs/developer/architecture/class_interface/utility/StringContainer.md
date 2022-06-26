# StringContainer


StringContainer is used to store information about a simulation; this
includes start and end times; program version, files opened for reading, files
opened for writing, and all parameters used (specified with pset or -par option
to program)

  // $Revision: 1.1 $
  // $Date: 2006-11-08 20:06:10 $
  // $Source: /usr/local/cvs/OpenSees/SRC/utility/StringContainer.h,v $
                                                                        
  // Created: 11/06

```cpp
class StringContainer
{
 public:
  StringContainer();
  ~StringContainer();
  int addString(const char *);
  const char *getString(int) const;
  const char *operator()(void);
  int getNumStrings() const;
  void clear(void);

 private:
  char **strings;
  int numStrings;
};
```

Code developed by: <span style="color:blue"> fmk</span>
