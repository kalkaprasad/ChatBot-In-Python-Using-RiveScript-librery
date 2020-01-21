from rivescript import RiveScript
import os.path

file = os.path.dirname(__file__)
brain = os.path.join(file,'brain') 
bot = RiveScript()
bot.load_directory(brain)
bot.sort_replies()
while True:
    msg = input(str('You> '))
    if msg == 'q':
        quit()
        
    else:
        print('Bot>'+bot.reply('localuser', msg))
       
