import click

# Email command
@click.group()
def email():
    pass

@email.command('holehe')
@click.option('--email', required=True, help='Email address')
def email_holehe(email):
    print(f"Running email holehe with email: {email}")

@email.command('specific/chess_com')
@click.option('--email', required=True, help='Email address')
def email_chess_com(email):
    print(f"Running email specific/chess_com with email: {email}")

@email.command('specific/instagram')
@click.option('--email', required=True, help='Email address')
def email_instagram(email):
    print(f"Running email specific/instagram with email: {email}")

@email.command('specific/twitter')
@click.option('--email', required=True, help='Email address')
def email_twitter(email):
    print(f"Running email specific/twitter with email: {email}")

@email.command('specific/spotify')
@click.option('--email', required=True, help='Email address')
def email_spotify(email):
    print(f"Running email specific/spotify with email: {email}")


# Password command
@click.group()
def password():
    pass

@password.command('pastebin')
@click.option('--password', required=True, help='Password')
def password_pastebin(password):
    print(f"Running password pastebin with password: {password}")

@password.command('haveibeenpwned/breach_info')
@click.option('--breach', required=True, help='Breach identifier')
def password_breach_info(breach):
    print(f"Running password haveibeenpwned/breach_info with breach: {breach}")

@password.command('haveibeenpwned/check')
@click.option('--password', required=True, help='Password')
def password_haveibeenpwned(password):
    print(f"Running password haveibeenpwned/check with password: {password}")


# Phonenumber command
@click.group()
def phonenumber():
    pass

@phonenumber.command('phoneinfoga/dorks')
@click.option('--number', required=True, help='Phone number')
def phonenumber_dorks(number):
    print(f"Running phonenumber phoneinfoga/dorks with number: {number}")

@phonenumber.command('phoneinfoga/search')
@click.option('--number', required=True, help='Phone number')
def phonenumber_search(number):
    print(f"Running phonenumber phoneinfoga/search with number: {number}")


# Username command
@click.group()
def username():
    pass

@username.command('search/lookup')
@click.option('--username', required=True, help='Username')
def username_lookup(username):
    print(f"Running username search/lookup with username: {username}")

@username.command('search/directory')
@click.option('--username', required=True, help='Username')
def username_directory(username):
    print(f"Running username search/directory with username: {username}")

@username.command('specific/amazon')
@click.option('--username', required=True, help='Username')
def username_amazon(username):
    print(f"Running username specific/amazon with username: {username}")

@username.command('specific/github')
@click.option('--username', required=True, help='Username')
def username_github(username):
    print(f"Running username specific/github with username: {username}")


if __name__ == '__main__':
    # Define the top-level group, which combines all commands
    @click.group()
    def stalker():
        pass

    stalker.add_command(email)
    stalker.add_command(password)
    stalker.add_command(phonenumber)
    stalker.add_command(username)

    stalker()
