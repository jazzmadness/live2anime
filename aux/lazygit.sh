function lazygit -d 'adds all files in repository, commits, and pushes to current branch' -a message
    set -q message[1]
    and set message -m $message
    git add .;git commit $message;git push;
end
funcsave lazygit
