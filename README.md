<div align="center">
  <img src="https://github.com/Qu1nel/TicTacToe/blob/git-page/git-source/tictactoe_logo.png" alt="logo" width="200px" height="auto" />
  <h1>Tic Tac Toe</h1>

  <p>
    Memorable first draft of the OOP
  </p>

<!-- Badges -->
<p>
  <a href="https://github.com/Qu1nel/TicTacToe/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Qu1nel/TicTacToe" alt="contributors" />
  </a>
  <a href="https://github.com/Qu1nel/TicTacToe/commits/main">
    <img src="https://img.shields.io/github/last-commit/Qu1nel/TicTacToe" alt="last update" />
  </a>
  <a href="https://github.com/Qu1nel/TicTacToe/network/members">
    <img src="https://img.shields.io/github/forks/Qu1nel/TicTacToe" alt="forks" />
  </a>
  <a href="https://github.com/Qu1nel/TicTacToe/stargazers">
    <img src="https://img.shields.io/github/stars/Qu1nel/TicTacToe" alt="stars" />
  </a>
  <a href="https://github.com/Qu1nel/TicTacToe/issues/">
    <img src="https://img.shields.io/github/issues/Qu1nel/TicTacToe" alt="open issues" />
  </a>
</p>

<p>
  <a href="https://www.python.org/downloads/release/python-3110/" >
    <img src="https://img.shields.io/badge/Python-3.11%2B-blueviolet" alt="python Version" />
  <a>
  <a href="https://github.com/Qu1nel/TicTacToe/releases/">
    <img src="https://img.shields.io/github/v/release/Qu1nel/TicTacToe" alt="project version" />
  <a>
  <a href="https://github.com/Qu1nel/TicTacToe/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Qu1nel/TicTacToe?color=g" alt="license" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/actions/workflow/status/Qu1nel/TicTacToe/python_linting.yml" alt="linting" />
  </a>
</p>
  
<h4>
  <a href="#view-demo">View Demo</a>
  <span> · </span>
  <a href="#documentation">Documentation</a>
  <span> · </span>
  <a href="https://github.com/Qu1nel/TicTacToe/issues/">Report Bug</a>
  <span> · </span>
  <a href="https://github.com/Qu1nel/TicTacToe/issues/">Request Feature</a>
</h4>
</div>

<br />

<!-- Table of Contents -->
# Contents

- [About the Project](#about-tictactoe)
  * [Demo](#view-demo)
  * [Screenshots](#screenshots)
- [Installation](#installation)
  * [Requirements](#requirements)
- [Getting started](#getting-started)
  * [Windows](#windows)
  * [Linux](#linux)
- [Documentation](#documentation)
- [Developers](#developers)
- [License](#license)

## About TicTacToe

The first OOP python project 💜

<details>
  <summary><h3 id="view-demo">View demo</h3></summary>
  <div align="center">
    <img src="https://github.com/Qu1nel/TicTacToe/blob/git-page/git-source/view_demo.gif" alt="gif_demo" width="500px" />
  </div>
</details>

<details>
  <summary><h3 id="screenshots">Screenshots</h3></summary>
  <div align="center">
    <img src="https://github.com/Qu1nel/TicTacToe/blob/git-page/git-source/preview_1.png" alt="preview_1" width="350px" />
    <img src="https://github.com/Qu1nel/TicTacToe/blob/git-page/git-source/preview_2.png" alt="preview_2" width="350px" />
  </div>
</details>

## Installation

Clone the repository and run the file `run.py`.
Make sure that all [requirements](#requirements) are met.


### Requirements

_The Python interpreter version 3.11+_

All python dependencies specified in the file [requirements.txt](./requirements.txt)

```bash
pip install -r requirements.txt
```

Install requirements with make:

```bash
make install-requirements
```

## Getting started

Clone this repository and navigate to it with the command:

```bash
git clone https://github.com/Qu1nel/TicTacToe.git
cd TicTacToe/
```

If you have the `make` installed, you can immediately create, activate the virtual environment and run the game with the command:

```bash
make init
source .venv/bin/activate
make install-requirements
make run
```

Or you can simply run `run.py` using the python interpreter

#### Windows

```powershell
python run.py
```

#### Linux

```bash
python3 run.py
```

## Documentation

There is a <u>*[settings.txt](./src/settings.txt)*</u> file in the file directory, in which you can change the game settings. such as:

1. Screen width
2. Who goes first (player or computer)
3. What is the player's shape (circle or cross)

To restart the game you need to press '**R**'

For full help with make commands, you can use the command:

```bash
make help
```

## Developers

- [Qu1nel](https://github.com/Qu1nel)

## License

This Project Qu1nel.TicTacToe in distributive under the **[MIT License](./LICENSE)**, and it also uses those codes that are distributed under the **[MIT License](./LICENSE)**.
