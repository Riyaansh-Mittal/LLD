from parking_lot import Solution

class Helper:
    def get_spot_id(self, floor, row, col):
        return f"{floor}-{row}-{col}"

    def get_spot_location(self, spot_id):
        try:
            floor, row, col = map(int, spot_id.split('-'))
            return floor, row, col
        except ValueError:
            return -1, -1, -1  # Invalid spot ID

# Instantiate the parking structure for testing purposes
parking_structure = [
    [["2-1", "2-1", "4-1"], ["4-0", "4-1", "4-0"]],
    [["2-1", "2-0", "4-1"], ["4-1", "4-0", "2-0"]]
]

# Initialize the Solution with the helper and parking structure
helper = Helper()
solution = Solution()
solution.init(helper, parking_structure)

# Test parking vehicles
print("Parking vehicle (type 2) with number ABC123:")
print("Assigned Spot ID:", solution.park(2, "ABC123", "TICKET123"))

print("Parking vehicle (type 4) with number XYZ789:")
print("Assigned Spot ID:", solution.park(4, "XYZ789", "TICKET456"))

# Test removing a vehicle
print("Removing vehicle ABC123:")
print("Status Code:", solution.remove_vehicle("0-0-0", "ABC123", "TICKET123"))

# Test counting free spots
print("Free spots for type 2 on floor 0:", solution.get_free_spots_count(0, 2))
print("Free spots for type 4 on floor 1:", solution.get_free_spots_count(1, 4))

# Test searching for a vehicle
print("Searching for vehicle XYZ789:")
print("Spot ID:", solution.search_vehicle("XYZ789", "TICKET456"))
