#!/bin/bash

# Args
git_dir="$HOME/gh"
filename=".autopull"

# Sort 
listfile="$git_dir/$filename"
sort -o $listfile $listfile

while read -r line; do

    local_repo="${git_dir}/${line}"
    if [ -d "${local_repo}" ]; then
        # Pull --rebase
        cd "${local_repo}"
        echo "Starting git pull for repo: ${line}"
        echo "Current branch: $(git branch | grep \* | cut -d ' ' -f2)"
        git pull --rebase
        echo ""
    else
        # Clone
        cd "${git_dir}"
        repo="git@github.com:blacklane/$line.git"
        echo "Starting git clone for repo: $line assuming $repo"
        git clone $repo
        echo ""
    fi
done < "$listfile"