# Crypto Price API
## Requires
Docker Engine

## build
docker build -t crypto_api_python .
## start
docker run -d -v "$(pwd):/app" crypto_api_python
