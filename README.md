# quantum-sg

A command line tool that generates a cryptographically secure quantum-level secrets using ANU QRNG.

## Usage

This function generates a random set of secrets using the quantumrandom library. The parameters population, number and length are optional.

```python
from string import digits
from quantum_sg import rand

rand(length=24, number=2, population=digits)
```

## Usage as CLI

```bash
$ pip install quantum-sg
$ quantum-sg -l 24 -n 2
> 4HOpcSlzrP1JA5pFROUJLi7V
> FkEKjlgm08Ey17HrAeeKKRl4
```

### Options

This command line utility can be used to generate secure secrets of specified length and complexity.

The `-h` or `--help` flag will display a help message to the user with instructions on how to use the utility.

The `-n` or `--number` flag will allow the user to specify the number of secrets to generate. By default, the utility will generate one secret.

The `-l` or `--length` flag will allow the user to specify the length of each generated secret. By default, this length is 24 characters.

The `-wd`, `--digits`, `-wl`, `--lowercase`, `-wu`, `--uppercase`, `-wp` and `--punctuation` flags will allow the user to specify which types of characters should be included in the generated secrets. By default, digits, lowercase characters, and uppercase characters are included.

## License

The MIT License (MIT)

Copyright (c) 2025 Alexander Shelepenok

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
