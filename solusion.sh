echo "Top 5 IP addresses with the most requests:" 
awk '{print $1}' sample-nginx-log.txt | sort | uniq -c | sort -nr | head -n 5
echo "Top 5 most requested paths"
awk '{print $7}' sample-nginx-log.txt | sort | uniq -c | sort -nr | head -n 5
echo "Top 5 most requested paths"
awk '{print $7}' sample-nginx-log.txt | sort | uniq -c | sort -nr | head -n 5


sort sample-nginx-log.txt | uniq -c | awk '{printf "%-10s %s\n", $2, $1}' | sort -nr | head -n 5

