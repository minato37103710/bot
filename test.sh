#!/bin/bash
cd (~/Project/bot)
git pull

cron */5 * * * * ~/git_pull.sh