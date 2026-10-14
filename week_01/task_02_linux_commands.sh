#!/usr/bin/env bash
# Task 2: Practice Linux commands.
# Everything runs inside a throw-away folder (~/linux_practice) so nothing important is touched.
# Run with:  bash task_02_linux_commands.sh
# Destructive commands (shutdown, restart, kill, dpkg) are shown as safe examples only.

step() { echo; echo "=== $1 ==="; }

step "pwd (print working directory)"
pwd

step "mkdir, cd, ls"
mkdir -p ~/linux_practice && cd ~/linux_practice
pwd
ls -la

step "touch (create empty files) and redirection (> and >>)"
touch empty.txt
echo "Hello Linux" > hello.txt          # overwrite
echo "Second line"  >> hello.txt        # append
printf "apple\nbanana\ncherry\ndate\nelderberry\n" > fruits.txt

step "cat (show a file)"
cat hello.txt

step "head, more, less"
head -n 3 fruits.txt
more fruits.txt < /dev/null || true     # 'more' and 'less' are interactive pagers
echo "(use 'less fruits.txt' interactively; press q to quit)"

step "file (identify file type)"
file hello.txt
file /bin/ls

step "cp, mv, mkdir, rm, rmdir"
cp hello.txt copy_of_hello.txt
mv copy_of_hello.txt renamed.txt
mkdir backup && cp renamed.txt backup/
ls -R
rm renamed.txt
rm backup/renamed.txt
rmdir backup
ls

step "alias"
alias ll='ls -la'
alias
echo "(aliases last for the current shell; put them in ~/.bashrc to make them permanent)"

step "chmod (change permissions)"
echo 'echo "I am a script"' > myscript.sh
ls -l myscript.sh
chmod +x myscript.sh
ls -l myscript.sh
./myscript.sh

step "bash and sh (run scripts with a shell)"
bash myscript.sh
sh myscript.sh

step "ps and kill"
sleep 60 &
PID=$!
ps -p $PID
kill $PID
sleep 0.2
echo "process $PID killed"

step "man (manual pages)"
man ls 2>/dev/null | head -n 5 || echo "man pages not installed here; try: man ls"

step "sudo (run as administrator). Example only"
echo "Example: sudo apt update   (needs admin rights, not executed here)"

step "nano (text editor). Example only"
echo "Example: nano notes.txt    (Ctrl+O save, Ctrl+X exit)"

step "dpkg (Debian package manager). Safe read-only use"
dpkg --version 2>/dev/null | head -n 1 || echo "dpkg not available"
dpkg -l 2>/dev/null | head -n 5 || true
echo "Example: sudo dpkg -i package.deb   (install a .deb file)"

step "shutdown and restart. Examples only, NOT executed"
echo "sudo shutdown now"
echo "sudo shutdown -r now   (or: sudo reboot)"

step "Cleanup"
cd ~ && rm -rf ~/linux_practice
echo "Done. Practice folder removed."
