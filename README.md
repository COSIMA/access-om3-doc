# ACCESS-OM3 Documentation
Documentation for COSIMA's [ACCESS-OM3](https://github.com/COSIMA/access-om3) global ocean - sea ice - wave model.

There's almost nothing here yet! Watch this space.

## Quick start
Do this to download the sources for this document:
```
git clone --recursive https://github.com/COSIMA/access-om3-doc.git
cd access-om3-doc
./setup.sh 
```
You should then be able to generate access-om3-doc.pdf using `latex`. You'll also need to run `bibtex` to get the references and `makeindex` to make the index.


## File/directory layout

`configs` contains submodules which have namelists of interest.

`tables` contains tabulated namelists in various formats including markdown and CSV. Those with `_diff` in the name only include differences.

`./make_tables.py` will update the tables of namelists in the `tables` directory.

`access-om3-doc.tex` is draft documentation in Latex.