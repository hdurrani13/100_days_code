class User:

    def __init__(self, user_id, username):
        '''Used to initilize attributes'''
        self.id = user_id
        self.username = username 
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
    
    

user_1 = User("001", "Hamza13")
user_2 = User("002", "John101")
# user_1.id = "001"
# user_1.username = "hamza13"

# print(user_1.id,user_1.username)
# print(user_2.id,user_2.username)

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.following)
print(user_2.followers)

