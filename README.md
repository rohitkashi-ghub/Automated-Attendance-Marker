# Automated-Attendance-Marker

Bot to automate marking attendance on the PSD LMS portal using Python with Selenium, and schedule it to run everyday using cronjobs

1. What did I use?

Python, Selenium, Environment Variables (In a file -> for scheduling, in bash_profile for program without scheduling), cronjob, loggers.

2. How to use environment variables?

Import os
os.environ.get(‘env_var_name’).
If you want to use cron, you need to define the env variables (and path, if you don’t want to use && in cron) in a .sh file
If you’re not scheduling, do the following:
(Refer to: https://www.youtube.com/watch?v=5iWhQWVXosU)


