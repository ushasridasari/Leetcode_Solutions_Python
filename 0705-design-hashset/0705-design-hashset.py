class MyHashSet:
    
    def __init__(self):
        #Creates a list with 1,000,001 elements
        self.data = [False] *1000001
    def add(self, key: int) -> None:
        #Sets it to True it means key is added to the set
        self.data[key] = True

    def remove(self, key: int) -> None:
        #Sets it to False it means key is removed from the set
        self.data[key] = False

    def contains(self, key: int) -> bool:
        #Looks at index key an returns true if key exists else false
        return self.data[key]
    



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)