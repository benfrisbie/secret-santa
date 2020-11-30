Secret Santa is a program written in python that simulates drawing random names out of a hat for a [secret santa gift exchange](https://en.wikipedia.org/wiki/Secret_Santa). It also sends an email/text to each person participanting to notify them who their secret reciepient is. The only stipulation in place is that a person can not get themself as a recipient.

# Command Line Options
## `--csv`
**Type:** str\
**Description:** Path to a CSV file that contains all participants' information. The CSV file should contain each person's information on a new line. A person's information consists of the following values in this order seperated by commas (`,`):
- name : The person's name. Example: "Bob"
- email : The person's email address. This can be a typical email address or a mobile phone number with carrier email address. Examples: "bob@gmail.com" or "1234567890@vtext.com". Here is a [list of all mobile carrier email addresses](https://resources.voyant.com/en/articles/3107728-sending-emails-to-sms-or-mms).

**Example:**
```
--csv /path/to/csv
```
Where `/path/to/csv` would be a file that looks like this:
```
Ben,ben@gmail.com
Tom,tom@yahoo.com
Bob,1234567890@vtext.com
```

## `--dry_run`
**Description:** Perform a dry test run and print the notifications that would be sent to each person to the console instead.\
**Example:**
 ```
 --dry_run
 ```

## `--email_sender`
**Type:** str\
**Description:** email address to send from\
**Example:"**
```
--email_sender bob@gmail.com
```

## `--email_subject`
**Type:** str\
**Description:** email subject line\
**Example:"**
```
--email_subject 'Secret Santa Subject Line'
```

## `--email_message_template`
**Type:** str\
**Description:** message template to use. The values that will be formatted by the code are `{name}` and `{recipient}`.\
**Example:"**
```
--email_message_template '<html><body>Hello {name},<br><br>You got {recipient} for the Secret Santa gift exchange.<br><br>The price limit is $25.<br><br>Merry Christmas!</body></html>
```

## `--smtp_host`
**Type:** str\
**Description:** host of the smtp server\
**Example:"**
```
--smtp_host smtp.gmail.com
```

## `--smtp_port`
**Type:** int\
**Description:** port of the smtp server\
**Example:"**
```
--smtp_port 587
```

## `--smtp_tls`
**Description:** use tls when talking to smtp server\
**Example:"**
```
--smtp_tls
```

## `--smtp_username`
**Type:** str\
**Description:** user to authenticate to the smtp server\
**Example:"**
```
--smtp_username bob@gmail.com
```

## `--smtp_password`
**Type:** str\
**Description:** password to authenticate to the smtp server\
**Example:"**
```
--smtp_password password123
```

# Examples
## Sending from gmail smtp server with authentication
```
python secret-santa.py \
--email_sender bob@gmail.com \
--smtp_host smtp.gmail.com \
--smtp_port 587 \
--smtp_username bob@gmail.com \
--smtp_password password123 \
--smtp_tls \
--csv test.csv \
--email_message_template '<html><body>Hello {name},<br><br>You got {recipient} for the Secret Santa gift exchange.<br><br>The price limit is $25.<br><br>Merry Christmas!</body></html>'
```