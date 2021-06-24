#!/bin/bash
cd (~/Project/bot)
git pull

cron */5 * * * * ~/Project/bot/test.sh