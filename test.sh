#!/bin/sh

*/5 * * * * /root/gitpull.sh
service crond restart

cd (/~/Project/bot)
git fetch
git reset --hard origin/master
git merge origin/master
