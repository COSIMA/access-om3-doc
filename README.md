# ACCESS-OM3 Documentation
Experimenting with ways to document COSIMA's [ACCESS-OM3](https://github.com/COSIMA/access-om3) global ocean - sea ice - wave model.

There's almost nothing here yet! Watch this space.

## Quick start

Do this to download the sources for this document:
```bash
git clone --recursive https://github.com/COSIMA/access-om3-doc.git  # NB: need --recursive due to submodules
cd access-om3-doc
./setup.sh 
```
You should then be able to generate access-om3-doc.pdf using `latex`. You'll also need to run `bibtex` to get the references and `makeindex` to make the index.

### Pulling updates

To update a previous clone of this repository to the latest version, you will need to do
```bash
git pull
git submodule update --init --recursive  # update all the submodules
```

## File/directory layout

`configs` contains submodules which have namelists of interest. See `.gitmodules` for their origin. See below for how to add and update configurations.

`tables` contains tabulated namelists in various formats including markdown and CSV. Those with `_diff` in the name only include differences.

`make_tables.py` updates the tables of namelists in the `tables` directory. Requires [nmltab](https://github.com/aekiss/nmltab).

`update_configs.sh` updates submodules in `configs`.

`access-om3-doc.tex` is draft documentation in Latex.

## Changing configurations

### Updating configurations

The submodules in the `configs` directory are pinned to particular commits. If you want to update them to the latest commits on the specified branches, run `update_configs.sh`. Then run `make_tables.py` if you want to update the tables.

### Altering configurations

If you edit `.gitmodules` to change the submodule's url or branch, you'll need to run `git submodule sync` and then `update_configs.sh`.

### Adding new configurations

Configurations in the `configs` directory are all submodules.

To add a new configuration, do this:
```bash
git submodule add -b <branch> <repo-url> configs/<config-name>
```
where `<config-name>` uniquely identifies the repository and branch, and does not already exist in `configs`, e.g.
```bash
git submodule add -b 1deg_jra55do_iaf https://github.com/COSIMA/MOM6-CICE6.git configs/MOM6-CICE6_1deg_jra55do_iaf
```
(Note: you need to explicitly specify the branch (even if it's the default branch), because `update_configs.sh` needs it. If you forgot to do this, you can define a branch for an existing submodule with `git submodule set-branch -b <branch> configs/<config-name>`; then run `update_configs.sh`.)

You might then want to edit and run `make_tables.py` to make new tables using your added configurations.

### Removing configurations

```
git rm configs/<config-name>
```
then edit `make_tables.py` to remove references to the removed configuration.

NB: tables with the removed configurations will still exist in `tables`. To remove these, do `rm -r tables` and run `make_tables.py`. Also remove references to the removed tables from `access-om3-doc.tex`.
