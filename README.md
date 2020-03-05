### ArtsDownloader

inworking...

---

A lightweight image downloader for most Artwork website.

### Usage

```shell
$ python downloader.py <-l|--link> FullLink [-d|--debug] [-t|--target] TargetFolder
```

- link : direct link to artist's page, such like `https://www.artstation.com/alicejaunet`
- target : specific a folder to store images

#### more options

- `-p`,`--proxy`: proxy port to socks5(eg. **127.0.0.1**:8082, place **8082** after tag).

### Supported Sites

- [x] ArtStation

- [ ] Pixiv

make a issue if you want more...

### Requirements

- requests
