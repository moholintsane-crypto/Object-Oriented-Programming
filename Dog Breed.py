class Dog:
    # Constructor to initialize name and breed
    "A simple model of a dog and its breed."
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.description = f"{self.name} are the {self.breed}."

    # Method to describe the dog
    def describe_or_display_info(self):
        print(self.description)
        print(f"{self.name} are the loyal and friendly companions.")
        print(f"{self.name} are the best friends of humans.")
        print(f"{self.name} are the most popular pets in the world.")

    # Method for behavior
    def bark(self):
        print(f"{self.name} says: Woof! and Bark!")
        print(f"{self.name} are barking loudly!")
        print(f"{self.name} are excited and happy!")    
        print(f"{self.name} are ready to play and have fun!")

# --- Using the Class ---
# Create an instance (object)
my_dogs = Dog("Rex and Buddy", "German Shepherd and Golden Retriever")

# Access methods
my_dogs.describe_or_display_info()
my_dogs.bark()
