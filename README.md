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

## Changes
## 1.1
- updated filename to be more descriptive
- added update timestamp to json data
### 1.0
- intial release