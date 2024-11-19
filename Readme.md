**Filtrer les colonnes/Projection**
- awk -F',' -v OFS=',' '{print $1,$2,$3,$4,$5,$6,$7,$8,$9,$11,$12}' weatherHistory.csv > new_weatherHistory.csv

**Filtrer les lignes**
- awk -F',' '$5 >= 0.85' new_weatherHistory.csv
- awk -F , '$6 >= 0.85' new_weatherHistory.csv > high_humidity.csv

**Creation d'un script shell**
- #!/bin/bash : permet de dire au system que c'est un script bash
- chmod +x weather_process.sh : permet de rendre le script executable

**Script python pour l'echantillonnage**
- python sample_csv.py .\high_humidity.csv sampled_high_humidity.csv
- cat sampled_high_humidity.csv | wc -l : permet de compter le nombre de ligne
