class File():
    def __init__(self):
        with open("images.txt", "r") as f:
            images_data = f.readlines()

        with open("music.txt", "r") as g:
            sounds_data = g.readlines()

        self.images_dictionary = {}
        self.points_dictionary = {}
        self.sounds_dictionary = {}
    
        for line in images_data:
            words = line.split(",")
            key = words[0]
            value = words[1]
            points_value = words[2]
            self.images_dictionary[key] = value
            self.points_dictionary[key] = points_value

        for line in sounds_data:
            words = line.split(",")
            key = words[0]
            value = words[1]
            self.sounds_dictionary[key] = value
    


