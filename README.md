## Installation

```bash
git clone https://github.com/daudputra/YT-downloader-docker-flask.git
cd YT-downloader-docker-flask
```

```bash
docker build --tag yt-downloader .
```

## Usage

```bash
docker run -p 80:5000 yt-downloader
```

## Change the path
```bash
download_path = 'your/full/path'
```
## Enter the page URL
```bash
Go to http://localhost:80
```
  
## License

[MIT](LICENSE)
