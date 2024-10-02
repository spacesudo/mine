import telebot
from telebot.util import antiflood, quick_markup ,extract_arguments
from dotenv import load_dotenv
import os
from db import Users

load_dotenv()


Token = os.getenv('TOKEN')

bot = telebot.TeleBot(Token, parse_mode='Markdown', disable_web_page_preview=True)

db_user = Users()
db_user.setup()

@bot.message_handler(commands=['broadcast'])
def broadcast(message):
    print(message.from_user.id)
    messager = message.chat.id
    if str(messager) == "7034272819" or str(messager) == "6219754372":
        send = bot.send_message(message.chat.id,"Enter message to broadcast")
        bot.register_next_step_handler(send,sendall)

    else:
        bot.reply_to(message, "You're not allowed to use this command")



def sendall(message):
    users = db_user.get_users()
    for chatid in users:
        try:
            msg = antiflood(bot.send_message, chatid, message.text)
        except Exception as e:
            print(e)

    bot.send_message(message.chat.id, "done")


@bot.message_handler(commands=['userno'])
def userno(message):
    print(message.from_user.id)
    messager = message.chat.id
    if str(messager) == "7034272819" or str(messager) == "6219754372":
        x = db_user.get_users()
        bot.reply_to(message,f"Total bot users: {len(x)}")
    else:
        bot.reply_to(message, "admin command")


@bot.message_handler(commands=['start'])
def start(message):
  owner = message.chat.id
  db_user.add_user(owner)
  msg = """Welcome to Blockchain Miner AI bot!!!
We handle all the stress of GPU mining and blockchain consensus with our high powered miners for your benefit.

Select your prefered choice below.
"""
  markup = quick_markup({
    'Blockchain Consensus': {'callback_data': 'consensus'},
    'Mining': {'callback_data': 'mining'}, 
  })
  bot.send_message(owner, msg, reply_markup = markup )
  
  
@bot.callback_query_handler(func= lambda call: True)
def call_back(call):
    owner = call.message.chat.id
    
    if call.data == "consensus":
      markup = quick_markup({
        "Purchase" : {"callback_data": "purchase"}
      })
      bot.send_message(owner, "With the help of Post method we currently provide mix hard disk of 11584 gb", reply_markup=markup)
      
    elif call.data == "mining":
        msg = """Select the Asset to mine
        
Chia (XCH)
Actual Price: $27.50 per XCH
Coins per Hour: 4.40 XCH ($121.00)
Coins per Week: 30.80 XCH ($847.00)
Coins per Month: 105.45 XCH ($2,900)

"""

        markup = quick_markup({
            'Previous' : {'callback_data' : 'next9'}, 
            'Purchase' : {'callback_data' : 'select'},
            'Next' : {'callback_data' : 'next1'},
        }, 3)
        bot.edit_message_text(msg, owner, call.message.message_id, reply_markup=markup)
        
        
    elif call.data == 'next1':
        msg = """Select the Asset to mine
        
Burstcoin (BURST)
Actual Price: $0.0045 per BURST
Coins per Hour: 25,000 BURST ($112.50)
Coins per Week: 175,000 BURST ($787.50)
Coins per Month: 600,000 BURST ($2,700)

"""

        markup = quick_markup({
            'Previous' : {'callback_data' : 'mining'}, 
            'Purchase' : {'callback_data' : 'select'},
            'Next' : {'callback_data' : 'next2'},
        }, 3)
        bot.edit_message_text(msg, owner, call.message.message_id, reply_markup=markup)
        
        
    elif call.data == 'next2':
        msg = """Select the Asset to mine

Storj (STORJ)
Actual Price: $0.38 per STORJ
Coins per Hour: 4.00 STORJ ($1.52)
Coins per Week: 28.00 STORJ ($10.64)
Coins per Month: 7,013 STORJ ($2,670)

"""

        markup = quick_markup({
            'Previous' : {'callback_data' : 'next1'}, 
            'Purchase' : {'callback_data' : 'select'},
            'Next' : {'callback_data' : 'next3'},
        }, 3)
        bot.edit_message_text(msg, owner, call.message.message_id, reply_markup=markup)
    
    
    elif call.data == 'next3':
        msg = """Select the Asset to mine

SiaCoin (SC)
Actual Price: $0.0025 per SC
Coins per Hour: 50,000 SC ($125.00)
Coins per Week: 350,000 SC ($875.00)
Coins per Month: 1,044,000 SC ($2,610)

"""

        markup = quick_markup({
            'Previous' : {'callback_data' : 'next2'}, 
            'Purchase' : {'callback_data' : 'select'},
            'Next' : {'callback_data' : 'next4'},
        }, 3)
        bot.edit_message_text(msg, owner, call.message.message_id, reply_markup=markup)
    
    
    elif call.data == 'next4':
        msg = """Select the Asset to mine

Filecoin (FIL)
Actual Price: $3.80 per FIL
Coins per Hour: 1.00 FIL ($3.80)
Coins per Week: 7.00 FIL ($26.60)
Coins per Month: 684.21 FIL ($2,600)

"""

        markup = quick_markup({
            'Previous' : {'callback_data' : 'next3'}, 
            'Purchase' : {'callback_data' : 'select'},
            'Next' : {'callback_data' : 'next5'},
        }, 3)
        bot.edit_message_text(msg, owner, call.message.message_id, reply_markup=markup)
        
    elif call.data == 'next5':
        msg = """Select the Asset to mine

MaidSafeCoin (MAID)
Actual Price: $0.20 per MAID
Coins per Hour: 4.50 MAID ($0.90)
Coins per Week: 31.50 MAID ($6.30)
Coins per Month: 13,000 MAID ($2,600)

"""

        markup = quick_markup({
            'Previous' : {'callback_data' : 'next4'}, 
            'Purchase' : {'callback_data' : 'select'},
            'Next' : {'callback_data' : 'next6'},
        }, 3)
        bot.edit_message_text(msg, owner, call.message.message_id, reply_markup=markup)
        
        
    elif call.data == 'next6':
        msg = """Select the Asset to mine

Bluzelle (BLZ)
Actual Price: $0.08 per BLZ
Coins per Hour: 10 BLZ ($0.80)
Coins per Week: 70 BLZ ($5.60)
Coins per Month: 32,363 BLZ ($2,590)

"""

        markup = quick_markup({
            'Previous' : {'callback_data' : 'next5'}, 
            'Purchase' : {'callback_data' : 'select'},
            'Next' : {'callback_data' : 'next7'},
        }, 3)
        bot.edit_message_text(msg, owner, call.message.message_id, reply_markup=markup)
        
    elif call.data == 'next7':
        msg = """Select the Asset to mine

Lambda (LAMB)
Actual Price: $0.0023 per LAMB
Coins per Hour: 78,000 LAMB ($0.1794)
Coins per Week: 546,000 LAMB ($1.2558)
Coins per Month: 1,130,435 LAMB ($2,589)

"""

        markup = quick_markup({
            'Previous' : {'callback_data' : 'next6'}, 
            'Purchase' : {'callback_data' : 'select'},
            'Next' : {'callback_data' : 'next8'},
        }, 3)
        bot.edit_message_text(msg, owner, call.message.message_id, reply_markup=markup)
        
    elif call.data == 'next8':
        msg = """Select the Asset to mine

Ocean Protocol (OCEAN)
Actual Price: $0.29 per OCEAN
Coins per Hour: 0.50 OCEAN ($0.145)
Coins per Week: 3.50 OCEAN ($1.015)
Coins per Month: 8,896 OCEAN ($2,584)

"""

        markup = quick_markup({
            'Previous' : {'callback_data' : 'next7'}, 
            'Purchase' : {'callback_data' : 'select'},
            'Next' : {'callback_data' : 'next9'},
        }, 3)
        bot.edit_message_text(msg, owner, call.message.message_id, reply_markup=markup)
        
    elif call.data == 'next9':
        msg = """Select the Asset to mine

0Chain (ZCN)
Actual Price: $0.11 per ZCN
Coins per Hour: 1.00 ZCN ($0.11)
Coins per Week: 7.00 ZCN ($0.77)
Coins per Month: 23,454 ZCN ($2,580)

"""

        markup = quick_markup({
            'Previous' : {'callback_data' : 'next8'}, 
            'Purchase' : {'callback_data' : 'select'},
            'Next' : {'callback_data' : 'mining'},
        }, 3)
        bot.edit_message_text(msg, owner, call.message.message_id, reply_markup=markup)
        
        
    elif call.data == 'select':
        s = bot.send_message(owner, "Enter your payout wallet: (Ethereum wallet)")
        bot.register_next_step_handler(s,setwallet)
        
    elif call.data == 'confirmm':
        bot.send_message(owner, "payment under review")
        
        

def setwallet(message):
    owner = message.chat.id
    wallet = str(message.text)
    if wallet.startswith('0x'):
        db_user.update_wallet(wallet, owner)
        bot.send_message(owner, 'Wallet updated')
        markup = quick_markup({
            'Confirm Payment' : {'callback_data' : 'confirmm'}
        })
        bot.send_message(owner, 'To Proceed with mining, You are requested to make a payment of *$1500* to \n`0x1234567899874563621` (tap to copy)\n\nPayment can take upto 15 minutes to be confirmed and our agent will contact you', reply_markup=markup)
    else:
        bot.send_message(owner, 'Invalid wallet address')
    
bot.infinity_polling()