
class Pokemon:
    def __init__(self, pokedex_entry, experience_points):
        self.__dict__.update(pokedex_entry)
        self.experience_points = experience_points
        self.level, self.current_experience = self.get_level()
        self.get_stats()
    
    def print_stats(self):
        print(
            f"lvl : {self.level}",
            f"exp totale : {self.experience_points}",
            f"exp actuelle : {self.current_experience}",
            f"atk : {self.attack}, def : {self.defense}, pv : {self.health_points}",
            sep="\n")

    def get_stats(self):
        self.attack = ((self.puissance_d_attaque * 2) * self.level) / 100 + 5
        self.defense = ((self.défense * 2) * self.level) / 100 + 5
        self.health_points = ((self.point_de_vie * 2) * self.level) / 100 + self.level + 10
    
    def gain_experience(self, gained_experience):
        self.experience_points += gained_experience
        self.current_experience += gained_experience
        self.level_up()

    def evolve(self):
        # condition if level and evolve level
        # self.__init__(self.evolution, self.experience_points)
        pass
    
    def level_up(self):
        if self.level == 1:
            consummed_experience = 8
        else:
            consummed_experience = ((self.level+1) ** 3) - (self.level ** 3)
        if self.current_experience > consummed_experience:
            self.level += 1
            self.current_experience = self.current_experience - consummed_experience
            self.get_stats()
            self.level_up()
    
    def get_level(self):
        for level in range (1,101):
            level_experience = level ** 3
            if level_experience > self.experience_points:
                pokemon_level = level-1
                current_experience = self.experience_points - (pokemon_level**3)
                break
        return pokemon_level, current_experience

pokemon_entry = {
      "Ndex": "#0001",
      "nom": "Bulbasaur",
      "type": ["Grass", "Poison"],
      "défense": 49,
      "puissance_d_attaque": 49,
      "point_de_vie": 45,
      "evolution_level" : 16,
      "evolution" : "#0002",
      "yield_experience" : 64,
      "images": {
        "front": "img/001/front.png",
        "back": "img/001/back.png"
      }
    }
gained_experience = round((pokemon_entry['yield_experience']*54) / 7 * 1.5, 0)
pokemon1 = Pokemon(pokemon_entry, 0)
pokemon1.gain_experience(gained_experience)
pokemon1.print_stats()
pokemon1.gain_experience(gained_experience)
pokemon1.print_stats()
pokemon1.gain_experience(gained_experience)
pokemon1.print_stats()