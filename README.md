# Mass Trackmania TAS Validator
This is a simple script that will automatically validate any replays found in a directory on your computer. This can be used for people looking to ensure fair play in any sort of competition involving offline replays.

⚠**This tool only checks for [TMInterface](https://donadigo.com/tminterface/), players can still cheat via other methods**

## Installation
```shell
> git clone https://github.com/ByroBuff/tm-mass-validator
> cd tm-mass-validator
> pip install -r requirements.txt
```

## Usage
Simple usage
```shell
> python main.py
```
Advanced Usage
```shell
> python main.py [-h] [-d custom/directory] [-v]

-h (--help) : help message
-d (-dir) : custom directory
-v (-verbose) : verbose (show valid replays as well)
```
