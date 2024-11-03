class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            return True

class Blog:
    def __init__(self, address, name):
        self.address = address
        self.name = name
        self.content_list = []
        self.user_access=[]

    def  add_content(self, content):
        if not isinstance(content, list):
            content = [content]
        self.content_list.extend(content)

    def add_user(self, user):
        self.user_access.append(user)


class Content:
    def __init__(self, title, creator):
        self.title = title
        self.creator = creator

def access_content(func):
    def wrapper(user,blog):
        if user in blog.user_access:
            username = input("please enter your username: ")
            password = input("please enter your password: ")
            if user.login(username,password):
                return blog.content_list
            else:
                print("wrong username or password")
        else:
            print("please register")
        return
    return wrapper

@access_content
def user_access(user,blog):
    return


if __name__ == '__main__':
    blog = Blog('http://www.blog.com','blog')
    c1 = Content('python learning', 'mohsen')
    c2 = Content('django', 'ali')
    c3 = Content('design patterns', 'reza')

    blog.add_content(c1)
    blog.add_content([c2,c3])

    user1 = User('mohsen', '123')
    blog.add_user(user1)
    user2 = User('ali', '123')

    contents= user_access(user1,blog)
    print(contents)
    print("="*10 +"user2"+ "="*10)
    user_access(user2,blog)

