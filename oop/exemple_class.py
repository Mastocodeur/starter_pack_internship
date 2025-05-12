import typing as t
from typing import Optional
from IPython import embed
from functools import cache

@cache
def f(x):
    return x**2

class Datacrafter:
    def __init__(self, prenom: str, nom: str, entreprise: str, interets: Optional[t.List[str]] = None, mail: Optional[str] = None) -> "Datacrafter":
        self.prenom = prenom
        self.nom = nom
        self.mail = mail
        self.entreprise = entreprise
        self.interets = interets if interets is not None else []

    def __repr__(self) -> str:
        return f"{self.prenom} {self.nom}"

    def _get_mail(self) -> Optional[str]:
        if self.entreprise == "datacraft":
            return f"{self.prenom.lower()}.{self.nom.lower()}@datacraft.paris"
        return None

    @property
    def nom_complet(self) -> str:
        return f"{self.prenom} {self.nom}"

    @staticmethod
    def greet() -> str:
        return "Bienvenue"


class DatacraftManager(Datacrafter):
    def __init__(self, prenom: str, nom: str, entreprise: str, interets: Optional[t.List[str]] = None, mail: Optional[str] = None, stagiaires: Optional[t.List[Datacrafter]] = None):
        super().__init__(prenom=prenom, nom=nom, mail=mail, entreprise=entreprise, interets=interets)
        self.stagiaires = {stagiaire.prenom: stagiaire for stagiaire in stagiaires} if stagiaires else None

    def __repr__(self) -> str:
        stagiaire_list = " - ".join(list(self.stagiaires.keys())) if self.stagiaires else "Aucun stagiaire"
        return f"{super().__repr__()} - Stagiaires: {stagiaire_list}"

    def print_stagiaires(self):
        if self.stagiaires:
            for _, stagiaire in self.stagiaires.items():
                print(stagiaire)
        else:
            print("Aucun stagiaire")


class Membre:
    def __init__(self, prenom: str, nom: str, entreprise: str, poste: str, numero: str, mail: str) -> "Membre":
        self.prenom = prenom
        self.nom = nom
        self.entreprise = entreprise
        self.poste = poste
        self.numero = numero
        self.mail = mail

    def __repr__(self) -> str:
        return f"{self.prenom} {self.nom}, {self.poste} chez {self.entreprise}"

    @property
    def contact_details(self) -> str:
        return f"Email: {self.mail}, Téléphone: {self.numero}"


class Freelance(Membre):
    def __init__(self, prenom: str, nom: str, numero: str, profession: str, mail: str, specialite: str, client: str):
        super().__init__(prenom=prenom, nom=nom, entreprise=client, poste=profession, numero=numero, mail=mail)
        self.specialite = specialite

    def __repr__(self) -> str:
        return f"{self.prenom} {self.nom}, {self.poste}, Spécialité: {self.specialite}, Client: {self.entreprise}"


def main():
    remy = Datacrafter(prenom="Remy", nom="Gasmi", entreprise="datacraft")
    thais = Datacrafter(prenom="Thais", nom="Denoyelle", entreprise="datacraft")
    raphael = DatacraftManager(prenom="Raph", nom="Vienne", entreprise="datacraft", stagiaires=[remy, thais])

    alex = Freelance(prenom="Alex", nom="Martin", numero="0601020304", profession="Développeur", mail="alex.martin@mail.com", specialite="Python", client="TechCorp")
    julie = Membre(prenom="Julie", nom="Dupont", entreprise="TechCorp", poste="CTO", numero="0605060708", mail="julie.dupont@techcorp.com")

    embed()
    return remy, thais, raphael, alex, julie

if __name__ == '__main__':
    main()
