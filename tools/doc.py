import inspect
from opensees import arg, obj

if __name__=="__main__":
    import opensees.lib

    for lib in [opensees.lib, opensees.patch]:
        for k,v in lib.__dict__.items():
            if isinstance(v, type):
                if issubclass(v, obj.Component):
                    #print(k)
                    s = str(inspect.signature(v))
                    print(f"{k}{s.replace('=None','')}")
                    try:
                        print(v.about)
                    except:
                        pass
                    try:
                        for a in v._args:
                            typ = a.__class__.__name__
                            print(f"\t| {a.name} (`{typ}`) |  {a.about} |")
                        print("\n")
                    except:
                        pass
            else:
                pass
                #print(type(v))
                #print(k)
