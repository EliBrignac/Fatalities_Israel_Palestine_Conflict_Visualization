import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv(r'C:\Users\Eli Brignac\OneDrive\Desktop\Israel_Data_Visualization\Fatalities_Israel_Palestine_Conflict_Visualization\app\data\fatalities_isr_pse_conflict_2000_to_2023.csv')

def weapon_propotions(df):

    df['ammunition'] = df['ammunition'].fillna('Unknown')
    #df['ammunition'] = df['ammunition'].dropna()


    # Count the frequency of each unique value
    value_counts = df['ammunition'].value_counts()

    for value, count in value_counts.items():
        print(f'{value}: {count}')

    # Filter categories with less than 10 instances and combine into "Other"
    threshold = 40
    other = list(value_counts[value_counts < threshold].index)
    df['ammunition'] = df['ammunition'].apply(lambda x: 'Other' if x in other else x)

    filtered_value_counts = df['ammunition'].value_counts()
    for value, count in filtered_value_counts.items():
        print(f'{value}: {count}')

    plt.figure(figsize=(8, 8))
    plt.pie(filtered_value_counts, labels=filtered_value_counts.index, 
            autopct='%1.1f%%', startangle=140, textprops={'fontsize': 10})
    plt.title('Ammunition Distribution')
    plt.show()





