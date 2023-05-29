# Crypto Price API
## Requires
Docker Engine

## build
docker build -t crypto_api_python .
## start
docker run -d -v "$(pwd):/app" crypto_api_python

## Changlog
### 1.1
- made filename more descriptive
- added timestamp to data
### 1.0
initial release