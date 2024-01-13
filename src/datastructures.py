# – update this file to implement the following already declared methods:
# - add_member: Should add a member to the self._members list
# - delete_member: Should delete a member from the self._members list
# - update_member: Should update a member from the self._members list
# - get_member: Should return a member from the self._members list


from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # If 'id' is not in the member dictionary, generate a new id
        if 'id' not in member:
            member['id'] = self._generateId()
        member['last_name'] = self.last_name  # Ensure the last name is set correctly
        self._members.append(member)

    def delete_member(self, id):
        # Delete a member by id
        self._members = [member for member in self._members if member['id'] != id]

    def get_member(self, id):
        # Return a member by id
        return next((member for member in self._members if member['id'] == id), None)

    def update_member(self, id, member):
        # Update a member by id
        for m in self._members:
            if m['id'] == id:
                m.update(member)
                break

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
