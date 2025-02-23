echo "[+] Setting it up for you :)"
sleep 0.2

wget https://assets.01-edu.org/stats-projects/stat-bin-dockerized.zip
unzip stat-bin-dockerized.zip

sleep 0.1

echo "[*] Here is our program results:"
python main.py data.txt
echo "--------------------------------------------------------------------------"
sleep 0.2
echo "--------------------------------------------------------------------------"

echo "[*] Here is reb00t program results:"
./stat-bin/bin/linear-stats data.txt
