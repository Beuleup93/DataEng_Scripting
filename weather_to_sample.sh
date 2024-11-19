# Print start time
echo "Script started at: $(date)"

# Remove Loud Cover column
awk -F, -v OFS=',' '{print $1,$2,$3,$4,$5,$6,$7,$8,$9,$11,$12}' weatherHistory.csv > new_weatherHistory.csv  

# Filter rows with humidity >= 0.85
awk -F, '$6 >= 0.85' new_weatherHistory.csv > high_humidity.csv   

# Sample 10% of high humidity rows
python sample_csv.py high_humidity.csv sample_high_humidity.csv

# Print end time
echo "Script completed at: $(date)"