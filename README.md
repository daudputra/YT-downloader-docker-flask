> [!CAUTION]
> Can't download videos that require login.
> 
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
[http://localhost:80](http://localhost:80)
  
## License

[MIT](LICENSE)
