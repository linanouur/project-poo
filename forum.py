class Forum:
    def __init__(self, id, nom, description=""):
        self.id = id
        self.nom = nom
        self.description = description
        self.publications = []  

    def __str__(self):
        return f"Forum(id={self.id}, nom='{self.nom}', description='{self.description}')"
