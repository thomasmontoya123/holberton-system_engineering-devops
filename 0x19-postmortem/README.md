# Postmortem

## Issue Summary

From 6:26 PM to 7:58 PM PT, requests to http://28f7e16cc698.44.hbtn-cod.io resulted in 500 error response messages. The root cause of this outage was a typo on the /var/www/html/wp-settings.php file.

## Timeline (PT)
- 6:19 PM: Outage notification
- 6:26 PM: Strace run
- 6:54 PM: Typo found
- 7:15 PM: Typo fixed
- 7:19 PM: Server restarts begin
- 7:58 PM: back online

## Root Cause
A configuration change was inadvertently released to our production environment without first being released to the testing environment. The typo was one extra "p" on one of the file extensions in the file /var/www/html/wp-settings.php

## Resolution
At 6:54 PM, The typo was founded reading the Strace log.
At 7:15 PM, The correction was implemented using Puppet.

## Corrective and Preventive measures
In the last two days, we’ve conducted an internal review and analysis of the outage. The following are actions we are taking to address the underlying causes of the issue and to help prevent recurrence and improve response times:
- Disable the current configuration release mechanism until safer measures are implemented. (Completed.)
- Test on local before deploy.
- Run the E2E tests before deploy.


#### Author
Thomas Montoya