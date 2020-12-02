Secret Santa is a program written in python that simulates drawing random names out of a hat for a [secret santa gift exchange](https://en.wikipedia.org/wiki/Secret_Santa) and then sends an email to each person participating notifying them who their secret recipient is. 

The only default rule in place is that a person can not get themself as a recipient. Other rules can easily be created in the config. Here are some common situations that can be accommodated:
- Preventing a significant other as a recipient [example](examples/examples/prevent_significant_others.yaml)
- Preventing the same recipient you got last year [example](examples/prevent_previous_years_recipient.yaml)

# Getting Started
## Create a Python Virtual Environment. (Optional)
First create a python virtual environment. This is optional, but it is always recommended to keep project dependencies separate.
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
The [config.yaml](config.yaml) defines how the script should run. There are required and optional fields. Any optional fields can be commented out or removed if you don't need them for your use case.

All of the fields are defined below:
- `dry_run`: bool (optional) - if true a test run is initiated. No emails are sent and instead the results are output to the console.
- `smtp`: object (optional) - encapsulates all smtp settings. If this it not present, it's equivalent to running with `dry_run: true`.
    - `host`: string (required) - the smtp host server
    - `port`: int (required) - the smtp port
    - `username`: string (optional) - the user to authenticate as
    - `password`: string (optional) - the password to authenticate with
    - `tls`: bool (optional) - if true tls is enabled when communicating to the smtp server
- `email`: object (required) - encapsulates all email settings
    - `from`: string (required) - the email to send from
    - `subject`: string (required) - the email subject line
    - `message`: string (required) - the html formatted email message template. The code will replace instances of `{name}` and `{recipient}` with the correct values.
- `participants`: list\[objects\] (required) - a list of participant objects. these define everyone playing
    - `name`: string (required) - name of the person
    - `email`: string (required) - this persons email to send the notification to
    - `excludes`: list\[string\] (optional) - list of names to exclude this person from getting as a recipient

# Examples
See example configs in [examples/](examples/).