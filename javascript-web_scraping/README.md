# 0x11. JavaScript - Web scraping

Scripts written in JavaScript (Node.js) for the **ALU Higher Level
Programming** — Web scraping project.

## Files

| File                 | Description                                                                          |
| -------------------- | ------------------------------------------------------------------------------------ |
| `0-readme.js`        | Reads the file given as the first argument as utf-8 and prints it, or the error object |
| `1-writeme.js`       | Writes the second argument as utf-8 to the file given as the first argument            |
| `2-statuscode.js`    | Prints the status code of a GET request as `code: <status code>` using `request`      |
| `3-starwars_title.js`| Prints the title of the Star Wars film matching the given movie id                    |
| `4-starwars_count.js`| Prints the number of films where Wedge Antilles (character id 18) is present           |

## Setup

```console
$ npm install request
```

## Usage

```console
$ ./0-readme.js cisfun
C is super fun!
$ ./0-readme.js doesntexist
Error: ENOENT: no such file or directory, open 'doesntexist'
$ ./1-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt; echo ""
Python is cool
$ ./2-statuscode.js https://alu-intranet.hbtn.io/status
code: 200
$ ./2-statuscode.js https://alu-intranet.hbtn.io/doesnt_exist
code: 404
$ ./3-starwars_title.js 1
A New Hope
$ ./3-starwars_title.js 5
Attack of the Clones
$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
```