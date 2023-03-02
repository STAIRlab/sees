cmake_minimum_required(VERSION 3.19)
project(OpenSeesRT)

add_subdirectory(src/libg3)

install(TARGETS 
         OpenSeesRT LIBRARY DESTINATION .)


