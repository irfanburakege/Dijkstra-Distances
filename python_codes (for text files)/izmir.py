# Define the district index mapping
district_index = {
    "ALİAĞA": 0, "BALÇOVA": 1, "BAYINDIR": 2, "BAYRAKLI": 3, "BERGAMA": 4,
    "BEYDAĞ": 5, "BORNOVA": 6, "BUCA": 7, "ÇEŞME": 8, "ÇİĞLİ": 9,
    "DİKİLİ": 10, "FOÇA": 11, "GAZİEMİR": 12, "GÜZELBAHÇE": 13, "KARABAĞLAR": 14,
    "KARABURUN": 15, "KARŞIYAKA": 16, "KEMALPAŞA": 17, "KINIK": 18, "KİRAZ": 19,
    "KONAK": 20, "MENDERES": 21, "MENEMEN": 22, "NARLIDERE": 23, "ÖDEMİŞ": 24,
    "SEFERİHİSAR": 25, "SELÇUK": 26, "TİRE": 27, "TORBALI": 28, "URLA": 29
}

# Initialize the distance matrix with None or a placeholder value
districtDistances = [[None for _ in range(30)] for _ in range(30)]

# Read and parse the file
with open("izmirilce2.txt", "r", encoding="utf-8") as file:
    for line in file:
        # Split each line into components
        parts = line.split()
        
        # Ensure the line has the expected structure
        if len(parts) >= 2:
            # Identify the start and destination districts
            start_district = parts[0]
            destination_district = parts[1]
            
            # Get the distance value (last element after joining possible decimal parts)
            distance = float(parts[2].replace(",", "."))
            
            # Use the district index mapping to get indices
            start_index = district_index.get(start_district)
            destination_index = district_index.get(destination_district)
            
            # Assign the distance to the matrix if indices are found
            if start_index is not None and destination_index is not None:
                districtDistances[start_index][destination_index] = distance

# Print the matrix
for i in range(30):
    print(f"districtDistances[{i}] = new double {{",end="")
    for j in range(30):
        if districtDistances[i][j] is not None:
            print(f"new double {districtDistances[i][j]}, ",end="")
        elif districtDistances[i][j] is None:
            print("0, ",end="")
        
    print("};")
