normalize-python
================

Python script to normalize input path. 'Normalize' means remove (and evaluate)
instances of '.' and '..' in *nix path names. For example, executing

```python norm.py /path/to/the/./first/../next/directory/../folder```

returns

```/path/to/the/next/folder```.

This is done via the function norm_path, which takes a string as input and
returns the normalized string.