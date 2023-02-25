cmake_minimum_required(VERSION 3.19)
project(OpenSeesRT)

if (WIN32)
  if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
    message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
    file(DOWNLOAD "https://raw.githubusercontent.com/conan-io/cmake-conan/0.18.1/conan.cmake"
                  "${CMAKE_BINARY_DIR}/conan.cmake"
                  TLS_VERIFY ON)
  endif()

  include(${CMAKE_BINARY_DIR}/conan.cmake)

  conan_cmake_run(CONANFILE src/libg3/conanfile.py
                  BASIC_SETUP CMAKE_TARGETS
                  BUILD missing)
endif()

add_subdirectory(src/libg3)

install(TARGETS 
         OpenSeesRT 
       # OpenSeesPyRT 
	       LIBRARY DESTINATION .)


