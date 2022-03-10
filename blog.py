class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None
        
    def create_new_user(self):
        username = input('Please enter a username ')
        password = input('Please enter a password ')
        new_user = User(username, password)
        self.users.append(new_user)
        print(f"{new_user} has been created")
    
    def log_user_in(self):
        username = input('What is your username? ')
        password = input('What is your password? ')
        for user in self.users:
            if username == user.username and user.check_password(password):
                self.current_user = user
                print(f"{user} has been logged in")
                break
        else:
            print('Username and/or Password is incorrect')
    
    def log_user_out(self):
        self.current_user = None
        print("You have successfully logged out.")



class User:
    
    id_counter = 1
    
    def __init__(self, username, password):
        self.id = User.id_counter
        User.id_counter += 1
        self.username = username
        self.password = password
        
    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f"<User {self.id}|{self.username}>"
    
    def check_password(self, password):
        return self.password == password


class Post:
    pass



def run_blog():
    my_blog = Blog()
    while True:
        if not my_blog.current_user:
            print("1. Sign Up\n2. Log In\n3. Quit")
            to_do = input('Which option which you like to do? ')
            while to_do not in {'1', '2', '3'}:
                to_do = input('Please choose either 1, 2, or 3')
            if to_do == '3':
                break
            elif to_do == '1':
                my_blog.create_new_user()
            elif to_do == '2':
                my_blog.log_user_in()
        else:
            print("1. Log Out")
            to_do = input('Which option which you like to do? ')
            while to_do not in {'1'}:
                to_do = input('Please choose 1')
            if to_do == '1':
                my_blog.log_user_out()
                
run_blog()   