# import pandas as pd

# filepath = 'shared/onsite/RESULT_LIST_ANONYM_CAPACITY_MARKET_FCR_2025-05-20_2025-05-20.xlsx'
# df_market_capacity = pd.read_excel(filepath)

# my_pivot_table = pd.pivot_table(data=df_market_capacity,
#                                 values='ALLOCATED_CAPACITY_[MW]',
#                                 index='PRODUCT',
#                                 columns='COUNTRY',
#                                 fill_value=0.0,
#                                 aggfunc='sum')
# print(my_pivot_table)

# Získání věty od uživatele
veta = input("Napiš nějakou větu: ")

# Rozdělení věty na slova
slova = veta.split()

# Pro každé slovo zpracuj informace
for slovo in slova:
    delka = len(slovo)
    zacina_velkym = slovo.istitle()  # začíná velkým písmenem?
    male_slovo = slovo.lower()
    
    # Výpis informací
    print(f"Slovo: '{slovo}'")
    print(f" - Délka: {delka}")
    print(f" - Začíná velkým písmenem? {zacina_velkym}")
    print(f" - Malá písmena: {male_slovo}")
