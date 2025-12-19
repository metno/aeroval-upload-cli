# aeroval-upload-cli (auc)
Small upload CLI for the Aeroval Upload service. As of now it only runs with local host.

## Requirements

- >= Python 3.10



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


## Setup servers on local host

1. Clone and run the [frontend](https://gitlab.met.no/aeroval/web/-/tree/my-aeroval)
2. Clone and run the [api](https://gitlab.met.no/aeroval/users)
3. Download the [tusd go server](https://tus.github.io/tusd/getting-started/installation/) and run with 

```
./tusd -upload-dir=<folder to put uploaded files> -hooks-http http://localhost:8000/webhook -hooks-enabled-events pre-create,post-create,pre-finish,post-finish
```


## Running the CLI
The CLI needs an email and a password, as well as a list over files to upload

```
auc -e <email> -p <password> -f <file1.nc> -f <file2.nc>
```

If unsure, use 

```
auc --help
```



