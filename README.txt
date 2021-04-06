# Colour Swatch Generator

This is a Python script that reads a list of colours from standard input and
writes PNG files showing those colours.  It takes two command-line parameters:
the size of the images to be created and the name of an output directory
(which must already exist).

For example, if `colours.txt` looks like this:

```
AABBCC
#DDEEFF
```

and you run

```python
python3 create-swatches.py 15 img < colours.txt
```

then `AABBCC.png` and `DDEEFF.png` will be created in `img/`.
