# echo "Top 5 IP addresses with the most requests:" 
# awk '{print $1}' sample-nginx-log.txt | sort | uniq -c | sort -nr | head -n 5 | awk '{printf "%s - %d requests\n", $2, $1}'
# echo "" 
# echo "Top 5 most requested paths"
# awk '{print $7}' sample-nginx-log.txt | sort | uniq -c | sort -nr | head -n 5 | awk '{printf "%s - %d requests\n", $2, $1}'
# echo ""
# echo "Top 5 most requested status "
# awk ' {if (NF == 10) print $7; else print $9;}' sample-nginx-log.txt | sort | uniq -c | sort -nr | head -n 10 | awk '{printf "%s - %d requests\n", $2, $1}'
# echo ""
# echo "Top 5 most requested user agents\n"
# awk '{for (i=12; i<=NF; i++) printf "%s ", $i; print ""}' sample-nginx-log.txt | sort | uniq -c | sort -nr | head -n 5 | awk '{printf "%s - %d requests\n", $2, $1}'
# awk '{print $1}' sample-nginx-log.txt : Sẽ loc và lấy toàn bộ cột 1 
# sort : sắp xếp mặc định theo thứ tự a-->z 
# uniq -c sẽ lọc các dự liệu trùng lặp và trả về số lần xuất hiện của nó
# sort -nr : tùy chọn -n sắp xếp theo thứ tự Số | tùy chọn -r sắp xếp ngược lại từ lớn đến bé
# head -n 5 : -n cho phép đọc 5 dòng đầu tiên của đầu vào . 
# awk '{print NF}' sample-nginx-log.txt
