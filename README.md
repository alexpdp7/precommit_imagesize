```
$ cat .pre-commit-config.yaml
---
repos:
  - repo: https://github.com/alexpdp7/precommit_imagesize.git
    rev: v0.1.0
    hooks:
      - id: imagesize
        args: ["--max-width=10", "--max-height=10"]
```

By default this will just check `.png` images.

```
$ pre-commit run imagesize -a
checks image size........................................................Failed
- hook id: imagesize
- exit code: 1

image foo.png is 900 pixels wide, maximum is 10
image bar.png is 350 pixels tall, maximum is 10
```
