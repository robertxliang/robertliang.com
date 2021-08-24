# robertliang.com

Personal website for Robert Liang, using Vue.

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Generate QR code
To generate a QR code for your phone's lock screen, update the constants in generate_qr_code_wallpaper.py and run
```
python generate_qr_code_wallpaper.py
```

Requires Python >=3.6 and the library `qrcode`
```
python -m pip install qrcode[pil]
```
