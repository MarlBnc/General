import numpy as np

numbers = np.arange(151)
proba = {
    'common' : (0.749, 90),
    'rare' : (0.15, 35),
    'epique' : (0.075, 15),
    'legendaire' : (0.025, 10),
    'ultime' : (0.001, 1)
}
PRICE = 450
N_CARD_PER_PACK = 4
N_SIMU = 2000

card_vect = [[name]*n[1] for name,n in proba.items()]
card_vect = np.hstack(card_vect)
proba_vect =  [[p/n]*n for p,n in proba.values()]
proba_vect = np.hstack(proba_vect)

results = {}
for l in proba.keys():
    results[l] = []
results['cartes'] = []



for simu in range(N_SIMU):
    unique_pick = []
    found = []
    n_packs = []
    i = 0
    while len(unique_pick) != len(numbers):
        i += 1
        pack = np.random.choice(numbers, N_CARD_PER_PACK, replace=False, p=proba_vect)
        for n in pack:
            if n not in unique_pick:
                unique_pick.append(n)
        unique_values, counts = np.unique(card_vect[unique_pick], return_counts=True)
        tirage = {}
        for l, c in zip(unique_values, counts):
            tirage[l] = c
        for level in unique_values:
            if proba[level][1] == tirage[level] and level not in found:
                found.append(level)
                n_packs.append(i)
                # print(f'Toutes les {level} ont été obtenus en {i} pack')
    found.append('cartes')
    n_packs.append(i)
    # print(f'toutes les cartes ont été trouvées en {i} paquet\n')

    for l, n in zip(found,n_packs):
        results[l].append(n)

for l, v in results.items():
    print(f'Toutes les {l} ont été obtenus en {np.mean(v):.3g} packs en moyennne : {round(np.mean(v))*PRICE}$')




