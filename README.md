# Crypto Price API
python runs, will create a file data.json that will include prices of the supported coins.
## Requires
Docker Engine

.env file with the following API variable from coinmarket cap.
```CMC_API_KEY=```
## build
docker build -t crypto_api_python .
## start
docker run -d -v "$(pwd):/app" crypto_api_python
