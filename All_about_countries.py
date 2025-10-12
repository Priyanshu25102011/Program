class Japan():
    def capital(self):
        print("Tokyo is the capital of Japan.")
    def language(self):
        print("Japanese is the most widely spoken language of Japan.")
    def type(self):
        print("Japan is a Developed country.")

class China():
    def capital(self):
        print("Beijing is the capital of China.")
    def language(self):
        print("Chinese is the primary language of China.")
    def type(self):
        print("China is a Developed country.")

obj_japan = Japan()
obj_China = China()

for country in (obj_japan, obj_China):
    country.capital()
    country.language()
    country.type()