def create_list(quantity):
    sites = []
    # cria a lista de sites
    for i in range(quantity):
        item = input(f"digite o site {i+1}: ")
        if item == "":
            item = input(f"Voce não inseriu o site numero {i+1}: ")
            sites.append(item)

        else:
            sites.append(item)
    return sites