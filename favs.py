import sqlite3
import webbrowser

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('favs.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS favorites (title TEXT, url TEXT)''')
#c.execute('''INSERT INTO favorites (title, url) VALUES ('cb', 'https://mail.google.com/mail/u/0/#inbox')''')
conn.commit()

def get_fav(title):
    c.execute('''SELECT * FROM favorites WHERE title = ?''', (title,))
    return c.fetchone()

def get_favs():
    c.execute('''SELECT * FROM favorites''')
    return c.fetchall()

def add_fav(title, url):
    c.execute('''INSERT INTO favorites (title, url) VALUES (?, ?)''',(title, url))
    conn.commit()
    
def del_fav(title):
    c.execute('''DELETE FROM favorites WHERE title = ?''', (title,))
    conn.commit()

while True:
    
    response = input('Hello boss, please type\n v to launch your website\n l to show all your favs\n + to add a new fav\n - to remove a fav\n q to quit\n so what is it going to be?  ')
    
    if response == 'v':
        print('Loading....')
        shortcut = input("What is the shortcut?: ")
        record = get_fav(shortcut)
        
        try:
            webbrowser.open(record[1])
        except:
            print('Website unavailable')
            
    elif response == 'l':
        print('Showing....')
        print(get_favs())
        
    elif response == '+':
        destination = input('Where do you want this shortcut to go?: ')
        shortcut = input('What is the shortcut?: ')
        print('Adding....')
        add_fav(shortcut, destination)
        print('Done')
        
    elif response == '-':
        shortcut = input('What is the shortcut?: ')
        print('Deleting....')
        del_fav(shortcut)
        print('Done')
    elif response == 'q':
        print('Quitting....')
        break