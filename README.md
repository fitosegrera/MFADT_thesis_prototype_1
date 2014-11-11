MFADT_thesis_prototype_1
========================

First prototype: Using Intel's Edison to meassure the network traffic of a user in a particular computer. A linear bar led graph hooked to an Intel Edison board will display the results.

###Dependencies

__For the intel Edison:__

-wiringx86 python library that must be installed in the Edison.
-PIP pyton package manager
-pymongo library for connecting to a mongodb database using python.




#Steps

Install wiring-x86 on the intel edison. Download using curl from: [LINK](https://github.com/emutex/wiring-x86)

    curl -O -L https://github.com/emutex/wiring-x86

Once downloaded type:

    cd wiring-x86

    python setup.py install
