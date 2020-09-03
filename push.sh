USER='MachineThing'
echo "What is the password for $USER?"
read -s PASSWORD
git push https://$USER:$PASSWORD@github.com/machinething/picoctf.git
git push https://$USER:$PASSWORD@github.com/machinething/picoctf.git --tags
git fetch # solve Atom problem
