
sudo apt-get update -y

sudo apt-get install -y python3 python3-venv

cd /home/ubuntu/

source myenv/bin/activate

python3 my_script.py > /home/ubuntu/my_script.log 2>&1 &

python3 my_scriptPia.py > /home/ubuntu/my_scriptPia.log 2>&1 &
