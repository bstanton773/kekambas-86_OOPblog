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

    def edit_post(self, post_id):
        post = self._get_post_from_id(post_id)
        # Check if the post exists
        if post:
            # Check is the user is logged in AND the logged in user is the author of the post
            if self.current_user and self.current_user == post.author:
                print(post)
                edit_part = input('Would you like to edit the title, body, or quit? ')
                while edit_part not in {'title', 'body', 'both', 'quit'}:
                    edit_part = input('Would you like to edit the title, body, or quit? ')
                if edit_part == 'quit':
                    return
                elif edit_part == 'both':
                    new_title = input('Enter the new title: ')
                    new_body = input('Enter the new body: ')
                    post.update(title=new_title, body=new_body)
                elif edit_part == 'title':
                    new_title = input('Enter the new title: ')
                    post.update(title=new_title)
                elif edit_part == 'body':
                    new_body = input('Enter the new body: ')
                    post.update(body=new_body)
                print(f"{post.title} has been updated")
            # If not author but user is logged in 
            elif self.current_user:
                print(f"You do not have permission to update this post")
            # If not logged in at all
            else:
                print('You must be logged in to perform this action')
        # If the post does NOT exist
        else:
            print(f"Post with an id of {post_id} does not exist.")

    def delete_post(self, post_id):
        post_to_delete = self._get_post_from_id(post_id)
        if post_to_delete:
            if self.current_user and self.current_user == post_to_delete.author:
                self.posts = [post for post in self.posts if post != post_to_delete]
                print(f"{post_to_delete.title} has been deleted")
            elif self.current_user:
                print('You do not have permission to delete this post')
            else:
                print('You must be logged in to perform this action')
        else:
            print(f"Post with an id of {post_id} does not exist")
        


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

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in {'title', 'body'}:
                setattr(self, key, value)



def run_blog():
    # Create an instance of the Blog class
    my_blog = Blog()
    while True:
        # if there is currently no user logged in
        if not my_blog.current_user:
            print("1. Sign Up\n2. Log In\n3. View All Posts\n4. View Single Post\n5. Quit")
            to_do = input('Which option which you like to do? ')
            while to_do not in {'1', '2', '3', '4', '5'}:
                to_do = input('Please choose either 1, 2, 3, 4, or 5')
            if to_do == '5':
                break
            elif to_do == '1':
                my_blog.create_new_user()
            elif to_do == '2':
                my_blog.log_user_in()
            elif to_do == '3':
                my_blog.view_posts()
            elif to_do == '4':
                post_id = int(input('What is the id of the post you would like to view? '))
                my_blog.view_post(post_id)
        # if there is a user logged in
        else:
            print("1. Log Out\n2. Create a Post\n3. View All Posts\n4. View Single Post\n5. Edit a Post\n6. Delete a Post")
            to_do = input('Which option which you like to do? ')
            while to_do not in {'1', '2', '3', '4', '5', '6'}:
                to_do = input('Please choose 1, 2, 3, 4, 5 or 6')
            if to_do == '1':
                my_blog.log_user_out()
            elif to_do == '2':
                my_blog.create_a_post()
            elif to_do == '3':
                my_blog.view_posts()
            elif to_do == '4':
                post_id = int(input('What is the id of the post you would like to view? '))
                my_blog.view_post(post_id)
            elif to_do == '5':
                post_id = int(input('What is the id of the post you would like to edit? '))
                my_blog.edit_post(post_id)
            elif to_do == '6':
                post_id = int(input('What is the id of the post you would like to delete? '))
                my_blog.delete_post(post_id)
                
run_blog()   