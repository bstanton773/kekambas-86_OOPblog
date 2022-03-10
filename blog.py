class Blog:
    def __init__(self):
        self.users = []
        self.posts = []
        self.current_user = None

    def _get_post_from_id(self, post_id):
        for post in self.posts:
            if post.id == post_id:
                return post
        
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

    def create_a_post(self):
        if self.current_user:
            title = input('What is the title of your post? ').title()
            body = input('What is the body of your post? ')
            new_post = Post(title, body, self.current_user)
            self.posts.append(new_post)
            print(f"{new_post.title} has been created.")
        else:
            print('You must be logged in to perform this action')
    
    def view_posts(self):
        if self.posts:
            for post in self.posts:
                print(post)
        else:
            print('There are currently no posts for this blog :(')

    def view_post(self, post_id):
        post = self._get_post_from_id(post_id)
        if post:
            print(post)
        else:
            print(f"Post with an id of {post_id} does not exist.")
        


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
    
    id_counter = 1

    def __init__(self, title, body, author):
        """
        PARAMS:
        title  -> str
        body   -> str
        author -> User
        """
        self.id = Post.id_counter
        Post.id_counter += 1
        self.title = title
        self.body = body
        self.author = author

    def __str__(self):
        formatted_post = f"""
        {self.id} - {self.title.title()}
        By: {self.author}
        {self.body}
        """
        return formatted_post

    def __repr__(self):
        return f"<Post {self.id}|{self.title} by {self.author}>"



def run_blog():
    # Create an instance of the Blog class
    my_blog = Blog()
    while True:
        # if there is currently no user logged in
        if not my_blog.current_user:
            print("1. Sign Up\n2. Log In\n3. View All Posts\n4. Quit")
            to_do = input('Which option which you like to do? ')
            while to_do not in {'1', '2', '3', '4'}:
                to_do = input('Please choose either 1, 2, 3, or 4')
            if to_do == '4':
                break
            elif to_do == '1':
                my_blog.create_new_user()
            elif to_do == '2':
                my_blog.log_user_in()
            elif to_do == '3':
                my_blog.view_posts()
        # if there is a user logged in
        else:
            print("1. Log Out\n2. Create a Post\n3. View All Posts\n4. View Single Post")
            to_do = input('Which option which you like to do? ')
            while to_do not in {'1', '2', '3', '4'}:
                to_do = input('Please choose 1, 2, 3, or 4')
            if to_do == '1':
                my_blog.log_user_out()
            elif to_do == '2':
                my_blog.create_a_post()
            elif to_do == '3':
                my_blog.view_posts()
            elif to_do == '4':
                post_id = int(input('What is the id of the post you would like to view? '))
                my_blog.view_post(post_id)
                
run_blog()   