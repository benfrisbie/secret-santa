Secret Santa is a program written in python that simulates drawing random names out of a hat for a [secret santa gift exchange](https://en.wikipedia.org/wiki/Secret_Santa). It also sends an email to each person participanting to notify them who their secret recipient is. The only default rule in place is that a person can not get themself as a recipient.

# How to run
## Create a python virtual environment. (Optional)
First create a python virtual environment. This is optional, but it is always recommended to keep project dependencies seperate.
```
python -m venv /path/to/new/virtual/environment
source /path/to/new/virtual/environment/bin/activate
```
This creates a virtual environment at the path `/path/to/new/virtual/environment` and then activates it. 

Check out https://docs.python.org/3/library/venv.html for more info on virtual environments.

## Install dependencies
Install all of this projects package dependencies.
```
pip install -r requirements.txt
```

## Modify config.yaml
Modify config.yaml with your desired settings. Check out the [Config YAML](#Config-YAML) section for help with that.

## Run the script
```
python secret-santa.py
```
or
```
python secret-santa.py --config_path <path_to_config_yaml>
```

# Config YAML
TODO

# Examples
See the config examples in [examples/](examples/).