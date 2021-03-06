def input_number_check(prompt: str) -> int:
    while True:
        response = input(prompt)
        if response.isdigit():
            response = int(response)
            if response >= 0:
                return response
        print("Please provide a valid input.")


class Rooms:
    def __init__(self, name):
        descriptions = {
            "Studio Suite": "Featuring a plush bed and living space with extra seating, a sleeper sofa, and a TV that can be seen from every angle of the suite. Each studio suite includes a workstation, a wet bar, a refrigerator, and a microwave.      $149",
            "One-Bedroom Suite": "Including a separate living room with sleeper sofa and a bedroom with a TV in both spaces. Each one-bedroom suite features a workstation, a wet bar, a refrigerator, and a microwave.      $99",
            "Two-Bedroom Suite": "Spread out in the separate living room with sleeper sofa and two bedrooms with a TV in all three spaces. Each two-bedroom suite includes a workstation, a wet bar, a refrigerator, and a microwave.      $154",
            "Presidential Suite": "Experience even more space and comfort in our Presidential Suite. Some hotels’ Presidential Suites feature an espresso machine, fireplace, a luxury bathroom feature like whirlpool tubs, or a conference table with seating for up to eight.      $259",
            "Premium Suite": "Offering the same experience as our popular one-bedroom suites, Premium Suites include additional upgrades of Premium WiFi, a Keurig coffee brewer, plus snacks and drinks which are replenished daily.      $324",
        }
        self.name = name
        # self.type = room_type
        self.description = descriptions[name]
        # self.price = price

    def __repr__(self):
        return repr(self.description)


class PAYMENT:
    def __init__(self, method, charge):
        self.method = method
        self.charge = charge
