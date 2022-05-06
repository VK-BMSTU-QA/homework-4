# homework-4

For configuring testing environment run:
```bash
make test ARCH=x64 CHROME_VERSION=101
```

Use the variable `CHROME_VERSION` to specify Google Chrome version you have.
Possible versions are `99`, `100`, `101`, `102`
It set to `99` by default.

Use the variable `ARCH` to set your architecture. Possible values are
`arm` and `x64`. It is set to `arm` by default.

Use the variable `PLATFORM` to set your architecture. The only possible value is
`MACOS`. Sorry for that.
