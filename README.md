# aeroval-upload-cli (auc)
Small upload CLI for the Aeroval Upload service. As of now it only runs with local host.

## Requirements

- Python >= 3.12



## Installing the CLI

Clone the repo
```
git clone git@github.com:metno/aeroval-upload-cli.git
```
then in the cloned folder, install the CLI with pip
```
pip install .
```

The cli is now called `auc`


## Running the CLI
The CLI needs an email and a password, as well as a list over files to upload

```
auc -e <email> -p <password> -f <file1.nc> -f <file2.nc>
```

If unsure, use 

```
auc --help
```



