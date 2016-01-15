# DLutil

A few utility scripts and frequently-used code blocks for regular daily grind.

### DLdate:
Handles our file naming convention: DD-MM-YYYY in a specified root folder. Also creates datafile names based on the creation timestamp (including seconds).

### DLcamclient:
The boilerplate code for anything that needs to interface with our ZMQ camera server. This pattern will be useful for other instrument interfaces and it turns out to be a handy way to slap a nice API onto some lame instrument-specific, factory-provided c-code.
