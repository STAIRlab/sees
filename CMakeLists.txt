cmake_minimum_required(VERSION 3.18.0)
project(OpenSeesRT)
find_package(PythonExtensions REQUIRED)

#add_library(_hello MODULE hello/_hello.cxx)
add_subdirectory(src/libg3)
python_extension_module(OpenSeesPyRT)
install(TARGETS OpenSeesRT OpenSeesPyRT LIBRARY DESTINATION opensees)
