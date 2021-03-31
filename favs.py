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
    
    response = input('v to visit favourites, ls for list, add for new, d to delet, q to quit: ')
    
    if response == 'v':
        print('Loading....')
        shortcut = input("What is the shortcut?: ")
        record = get_fav(shortcut)
        
        try:
            webbrowser.open(record[1])
        except:
            print('Website unavailable')
            
    elif response == 'ls':
        print('Listing....')
        print(get_favs())
        
    elif response == 'add':
        destination = input('Where do you want this shortcut to go?: ')
        shortcut = input('What is the shortcut?: ')
        print('Adding....')
        add_fav(shortcut, destination)
        print('Done')
        
    elif response == 'd':
        shortcut = input('What is the shortcut?: ')
        print('Deleting....')
        del_fav(shortcut)
        print('Done')
    elif response == 'q':
        print('Quitting....')
        break