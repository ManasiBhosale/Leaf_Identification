# plant.py
import pandas as pd
import sys

pd.options.display.max_colwidth = 10000

arg = sys.argv[1]


info = pd.read_csv("PLANT_INFO.csv")
ans = info[info['Plant_Name'] == arg]

if ans.empty:
    print("Plant not found.")
else:
    # Create the output in the expected format with "+" separating the fields
    plant_name = ans['Plant_Name'].values[0]
    bot_name = ans['Bot_name'].values[0]
    local_name = ans['Local_name'].values[0]
    med_uses = ans['Med_uses'].values[0]
    location = ans['Location'].values[0]
    
    # Combine all fields into a single string with "+" separating them
    output = f"{plant_name}+{bot_name}+{local_name}+{med_uses}+{location}"
    
    print(output)
