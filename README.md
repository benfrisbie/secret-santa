Secret Santa is a program written in python that simulates drawing random names out of a hat for a [secret santa gift exchange](https://en.wikipedia.org/wiki/Secret_Santa). It also sends an email to each person participanting to notify them who their secret recipient is. The only default rule in place is that a person can not get themself as a recipient.

# Getting Started
## Create a Python Virtual Environment. (Optional)
First create a python virtual environment. This is optional, but it is always recommended to keep project dependencies seperate.
```
python -m venv venv
source venv/bin/activate
```
This creates a virtual environment named `venv` in the current working directory and then activates it. 

Check out https://docs.python.org/3/library/venv.html for more info on python virtual environments.

## Install Dependencies
Install all of the project's package dependencies.
```
pip install -r requirements.txt
```

## Modify Config YAML
Modify `config.yaml` with your desired settings. Check out the [Config YAML](#Config-YAML) section for help.

## Run the Script
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
See example configs in [examples/](examples/).