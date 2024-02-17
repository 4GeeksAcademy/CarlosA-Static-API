"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{'id': self._generate_id(),
            'first_name': 'John',
                          'last_name': self.last_name,
                          'age': 33,
                          'lucky_numbers': [7, 13, 12]},
                         {'id': self._generate_id(),
                          'first_name': 'Jane',
                          'last_name': self.last_name,
                          'age': 35,
                          'lucky_numbers': [10, 14, 13]},
                         {'id': self._generate_id(),
                          'first_name': 'Jimmy',
                          'last_name': self.last_name,
                          'age': 5,
                          'lucky_numbers': [1]}]  # example list of members

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member['id'] = self._generate_id()
        member['last_name'] = self.last_name
        self._members.append(member)
        return str(member['id']) + ' created succesfully'

    def delete_member(self, id):
        if any(member['id'] == id for member in self._members): # Verificar si al menos un miembro tiene el mismo 'id' que el proporcionado.
            self._members = [member for member in self._members if id != member['id']]
            return 0
        return None

    def get_member(self, id):
        return [member for member in self._members if id == member['id']]

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
