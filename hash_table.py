class Contact:
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size: int = 10):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key: str) -> int:
        return sum(ord(char) for char in key) % self.size

    def insert(self, key: str, number: str):
        contact = Contact(key, number)
        index = self.hash_function(key)
        current = self.data[index]

        if current is None:
            self.data[index] = Node(key, contact)
            return

        while current:
            if current.key == key:
                current.value = contact  # Update existing contact
                return
            if current.next is None:
                break
            current = current.next

        current.next = Node(key, contact)

    def search(self, key: str) -> Contact | None:
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for i, node in enumerate(self.data):
            print(f"Index {i}:", end=" ")
            current = node
            if not current:
                print("Empty")
            else:
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


# 🧪 Test the HashTable
if __name__ == "__main__":
    table = HashTable(10)

    print("Initial table:")
    table.print_table()

    print("\nAdding contacts...")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\nSearching for John:")
    contact = table.search("John")
    print("Search result:", contact)

    print("\nTesting collisions...")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")  # May may collide with Amy
    table.print_table()

    print("\nUpdating Rebecca's number...")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    print("\nSearching for Chris (not in table):")
    print("Search result:", table.search("Chris"))  # None


    # A hash table is the right structure for fast lookups because a hash table offers average-case constant-time lookup, insertion, and deletion because it maps keys to array indices using a hash function.
    #  This direct indexing avoids linear scans and reduces the number of comparisons to any near-constant for well distributed hashes. 
    # Hash tables also provide efficient average performance for workloads where exact-key access is the primary operation.

# Collisions were handled with separate chaining using linked lists (or dynamic arrays) at each bucket. 
# On insertion, the key's hash determines the bucket and the bucket is scanned for an existing key if none is found, the new entry is appended.
#  Lookups scan the bucket for a matching key and return the associated value, while deletions remove the matching node. 
# The implementation monitors the load factor and triggers resizing (typically doubling the bucket array)
#  when the load factor exceeds a threshold to keep average bucket length low and maintain constant time behavior.

# Choose a hash table when primary operations are exact key lookup, insertion, and deletion and predictable average-case speed is required. 
# Prefer a hash table over a list when O(1) average access is needed instead of O(n) scans. 
# Prefer it over a balanced tree when ordering is unnecessary and constant-time average operations are more important than guaranteed O(log n) worst-case bounds.
#  Avoid hash tables when ordered iteration, range queries, or strict worst-case guarantees are required in those cases, balanced trees are the better choice.


