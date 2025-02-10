import random

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}  # HashMap to store value -> index mapping
        self.values = []  # List to store actual values

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False  # Value already exists, cannot insert
        self.val_to_index[val] = len(self.values)  # Store index of new value
        self.values.append(val)  # Append new value to the list
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False  # Value does not exist, cannot remove
        
        # Get index of the value to remove
        idx_to_remove = self.val_to_index[val]
        last_element = self.values[-1]  # Get the last element in the list

        # Swap the last element with the element to remove
        self.values[idx_to_remove] = last_element
        self.val_to_index[last_element] = idx_to_remove

        # Remove the last element
        self.values.pop()
        del self.val_to_index[val]  # Delete from hashmap
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)  # Get a random element
