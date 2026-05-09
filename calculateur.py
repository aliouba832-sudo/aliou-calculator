try:
    # 1. On récupère l'entrée
    annee_texte = input("Quelle est ton année de naissance ? ")
    annee = int(annee_texte)
    
    # 2. On vérifie la cohérence
    if annee < 1900:
        print("Oula, tu es un voyageur du temps ? 🚀")
    elif annee > 2026:
        print("Attends... tu n'es pas encore né ! 🤔")
    else:
        # 3. Calcul
        age = 2026 - annee
        if age < 18:
            print(f"Tu as {age} ans. Tu es mineur ! 🎮")
        elif age > 100:
            print(f"Tu as {age} ans. Respect l'ancien ! -_-")
        else:
            print(f"Tu as {age} ans. Tu es un adulte ! ✅")

except ValueError:
    print("Erreur : Aliou, tape un nombre stp ! Pas de lettres. ❌")