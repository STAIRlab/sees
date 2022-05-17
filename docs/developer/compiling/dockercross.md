# Cross Compiling


```shell
{
docker run --rm dockcross/windows-shared-x86 
} > ./dockcross-windows-shared-x86
chmod +x ./dockcross-windows-shared-x86
```

> You may need to run `sudo dockerd` first to start
> the docker daemon.


```
mkdir build_win
cd build_win
cp ../conanfile.py .
sudo ../dockcross-windows-shared-x86 conan install .
```

```shell
cd ../
sudo ./dockcross-windows-shared-x86 cmake -B build_win/
```


```
