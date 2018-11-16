# TODO 11.1 Introduction to Inheritance
# You are going to create a Dwelling class based on the Automobile
# Sample from the chapter


# create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors
class Dwelling:

    def __init__(self, number_of_rooms, square_feet, floors):

        # add the mutators for all of the data attributes (number_of_rooms, square_feet, floors)

        self.number_of_rooms = number_of_rooms
        self.square_feet = square_feet
        self.floors = floors


# add the accessors for all of  the data attributes

    def get_number_of_rooms(self):
        return self.number_of_rooms

    def get_square_feet(self):
        return self.square_feet

    def get_floors(self):
        return self.floors

# Create the class Single_family_home as a sub class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size


class Singlefamilyhome(Dwelling):
    def __init__(self, number_of_rooms, square_feet, floors, garage_type, yard_size):

        # call the superclass of Dwelling and pass the required arguments, remember to include self
        Dwelling.__init__(self, number_of_rooms, square_feet, floors)

# initialize the garage_type and yard_size attributes
        self.garage_type = garage_type
        self.yard_size = yard_size
# create the mutator and accessor methods for the garage_type and yard_size attributes

    def set_garage_type(self, garage_type):
        self.garage_type = garage_type

    def set_yard_size(self, yard_size):
        self.yard_size = yard_size

    def get_garage_type(self):
        return self.garage_type

    def get_yard_size(self):
        return self.yard_size


# denonstrate the Single_family_home class, no need to import because you are in the same file

# create an object from the Single_family_home class with the following information:
# 6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres
# Display the data using the accessor methods

family_home = Singlefamilyhome(6, 1200, 1, "Single car garage", ".25 Acres")


# create the main function
def main():
    print("Number of rooms:", family_home.get_number_of_rooms())
    print("Square feet:",family_home.get_square_feet())
    print("Number of floors:",family_home.get_floors())
    print("Garage type:",family_home.get_garage_type())
    print("Yard size:",family_home.get_yard_size())
# call the main function
main()
