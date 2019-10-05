
##### How to run the unit tests.

In one directory up from this directory:

```
python -m unittest discover -t ..
```


To run a particular test, from the two directories up (outside of this package)
e.g., 

```
python -m unittest alphat-logic.tests.test_Binning.TestBinning.test_call
```

`alphat-logic` is a name of the directory. If you checked out this repo as a
different name, e.g., `atlogic`, use the different name.
