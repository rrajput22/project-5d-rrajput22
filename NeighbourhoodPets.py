# Author: Rajvi Rajput
# GitHub username: rrajput22
# Date: 10/31/2023
# Description: Program manages pets in neighbourhood by allowing adding, deleting and searching for owners through JSON
# files and also raises an exception for duplicate pet names


import json


class DuplicateNameError(Exception):
    """exception for duplicate pet names"""
    pass


class Pet:
    def __init__(self, name, species, owner):
        """initializes a pet object with name, species and owner"""
        self._name = name
        self._species = species
        self._owner = owner

    def get_name(self):
        """gets the name of the pet"""
        return self._name

    def get_species(self):
        """gets the name of the pet species"""
        return self._species

    def get_owner(self):
        """gets the name of the pet owner"""
        return self._owner


class NeighborhoodPets:
    def __init__(self):
        """initializes class with an empty set of pets"""
        self._pets = set()

    def add_pet(self, name, species, owner):
        """adds new pet to the neighbourhood after checking for duplicates"""
        new_pet = Pet(name, species, owner)
        if any(pet.get_name() == name for pet in self._pets):
            raise DuplicateNameError("A pet with the same name already exists.")
        self._pets.add(new_pet)

    def delete_pet(self, name):
        """deletes pet from neighbourhood"""
        self._pets = {pet for pet in self._pets if pet.get_name() != name}  # makes sure that only pets with different
        # name are included in new set

    def get_owner(self, name):
        """gets pet owner for a specific pet"""
        for pet in self._pets:
            if pet.get_name() == name:
                return pet.get_owner()
        return "No pet found"  # returns No pet found if pet not found

    def save_as_json(self, file_name):
        """saves pet data to a JSON file"""
        with open(file_name, 'w') as json_file:
            # creates a list of dictionaries 'pet_data' with the name, species, owner keys
            pet_data = [{'name': pet.get_name(), 'species': pet.get_species(), 'owner': pet.get_owner()} for pet
                        in self._pets]

    def read_json(self, file_name):
        """reads pet data from JSON file and then replaces current data"""
        with open(file_name, 'r') as json_file:
            pet_data = json.load(json_file)  # reads JSON file and passes to object
            self._pets = {Pet(pet['name'], pet['species'], pet['owner']) for pet in pet_data}

    def get_all_species(self):
        """gets set of all pet species in neighbourhood"""
        return {pet.species for pet in self._pets}

# Example usage:


# np = NeighborhoodPets()
# try:
#    np.add_pet("Fluffy", "gila monster", "Oksana")
#    np.add_pet("Tiny", "stegasaurus", "Rachel")
#    np.add_pet("Spot", "zebra", "Farrokh")
# except DuplicateNameError as e:
#    print(f'Error: {e}')

# np.save_as_json("pets.json")
# np.delete_pet("Tiny")
# spot_owner = np.get_owner("Spot")
# np.read_json("other_pets.json")  # Replace with an actual file you saved in some previous session
# species_set = np.get_all_species()

# Testing the functionality
# print("Spot's owner after reading from other_pets.json:", spot_owner)
# print("All species:", species_set)
