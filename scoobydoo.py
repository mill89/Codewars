villains = ["Black Knights", "Puppet Master", "Ghost Clowner", "Witch Doctors",
            "Waxed Phantom", "Manor Phantom", "Ghost Bigfoot", "Haunted Horse", "Davy Crockett",
            "Captain Injun", "Greens Gloobs", "Ghostly Manor", "Netty Crabbes", "King Katazuma",
            "Gators Ghouls", "Headless Jack", "Mambas Wambas", "Medicines Man", "Demon Sharker",
            "Kelpy Monster", "Gramps Vamper", "Phantom Racer", "Skeletons Men", "Moon Monsters"]


# def scoobydoo(villian, villians):
#     return villians[[word.lower().replace(' ', '')[-6::-6]
#                      for word in villians].index(villian[::6][:3])]

def scoobydoo(villian: str, villians: list) -> str:
    for name in villians:
        if sorted(name.lower().replace(' ', '')[::2]) == sorted(villian[::2]):
            return name

# символы через 1
# sorted(f[::2]) == sorted(d[::2])

if __name__ == '__main__':
    print(scoobydoo("oyhxtdwnrjtx", villains))

    assert scoobydoo("ndcddzmiahsz", villains) == "Medicines Man"
    assert scoobydoo("ooegefsiehsi", villains) == "Skeletons Men"
    assert scoobydoo("oyhxtdwnrjtx", villains) == "Witch Doctors"
