# 0x11. JavaScript - Web scraping

Scripts written in JavaScript (Node.js) for the **ALU Higher Level
Programming** — Web scraping project.

## Files

| File             | Description                                                                          |
| ---------------- | ------------------------------------------------------------------------------------ |
| `0-readme.js`    | Reads the file given as the first argument as utf-8 and prints it, or the error object |
| `1-writeme.js`   | Writes the second argument as utf-8 to the file given as the first argument            |

## Usage

```console
$ ./0-readme.js cisfun
C is super fun!
$ ./0-readme.js doesntexist
Error: ENOENT: no such file or directory, open 'doesntexist'
$ ./1-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt; echo ""
Python is cool
```