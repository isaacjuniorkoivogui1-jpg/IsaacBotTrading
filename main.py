def analyse_marche(prix_actuel, support, resistance):
    
    if prix_actuel <= support:
        decision = "BUY 📈"
        confiance = "82%"
        
    elif prix_actuel >= resistance:
        decision = "SELL 📉"
        confiance = "84%"
        
    else:
        decision = "ATTENDRE ⏳"
        confiance = "50%"
    
    print("=== IsaacBotTrading ===")
    print("Prix actuel :", prix_actuel)
    print("Support :", support)
    print("Résistance :", resistance)
    print("Décision :", decision)
    print("Confiance :", confiance)


# Exemple test
analyse_marche(
    prix_actuel=105,
    support=100,
    resistance=110
  )
