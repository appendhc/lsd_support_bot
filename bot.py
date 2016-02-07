#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import time
reload(sys)
sys.setdefaultencoding("utf-8")

print "[System] Bot has started."

user = [line.rstrip('\n') for line in open('user.txt','rt')]
chat = [line.rstrip('\n') for line in open('chat.txt','rt')]
admins = [line.rstrip('\n') for line in open('admins.txt','rt')]

import telebot
import random
import json
import time
from pprint import pprint

API_TOKEN = 'token'
bot = telebot.TeleBot(API_TOKEN)

with open('loggingids.json') as f:
    loggingIDs = json.load(f)

@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(m):
	cid = m.chat.id
	inviter = m.from_user.first_name
	if m.content_type == 'new_chat_participant':
		if m.new_chat_participant.id == bot.get_me().id:
			chatid = m.chat.id
			if str(cid) not in chat:
				user.append(str(cid))
				with open('chat.txt', 'a') as f:
					f.write(str(cid)+"\n")
			bot.send_message(cid, "Hi ty for invite me but now im not work in group í ½í¸‰\nIf you want to see all the cute guys behind the Bot type /credits í ½í¸‡")
			print "New group received."
			userwhogotadded = m.new_chat_participant.first_name
			username = m.new_chat_participant.username
			groupname = m.chat.title
			groupid = m.chat.id
			bot.send_message('-84875656', "# DEBUG # " + "Bot got invited to the group " + str(groupname) + "(" + str(groupid) + ")", parse_mode="HTML")




@bot.message_handler(commands=['credits'])
def credits(m):
	cid = m.chat.id
	bot.send_message(cid, "@digitalboys", parse_mode="Markdown")

@bot.message_handler(commands=['help'])
def help(m):
	cid = m.chat.id
	bot.send_message(cid, "use /ask <MSG> for ask your question", parse_mode="Markdown")
	
@bot.message_handler(commands=['ask'])
def ask(m):
    tmt = m.from_user.id
    idA, cid = m.chat.id, m.chat.id
    str = m.text
    txt = str.replace("/ask", "")
    bot.send_message(idA, "<b>Thank you very much! Details to your Question:\n Quetsion:</b> {} \n<b>Chat-Id :</b> {} \n<b>We will answer you as soon as possible</b>".format(txt,idA), parse_mode="HTML")
    bot.send_message('-84875656', "<b>#NEW MSG\n Chat-Id:</b> {} \n<b>Msg :</b> {}".format(idA,txt), parse_mode="HTML")
    bot.send_message(idA, "<b>This is a confirmation that we received your Question</b>", parse_mode="HTML")


@bot.message_handler(commands=['answer'])
def answer(m):
        datafile = [line.rstrip('\n') for line in open('admins.txt','rt')]
        tmt = m.from_user.id
        idA, cid = m.chat.id, m.chat.id
        for line in datafile:
            if str(tmt) not in datafile:
                bot.send_message(cid, "Just for admin", parse_mode="Markdown")
                return
        to_id = m.text.split()[1]
        txt = m.text.split()[2:]
        text = ' '.join(txt)
        from_id = m.from_user.first_name
        bot.send_message(to_id, "<b>Staff</b> <i>{}</i> <b>has answered your question:</b>\n <i>{}</i>".format(from_id,text), parse_mode="HTML")
     
     
@bot.message_handler(commands=['bb'])
def answer(m):
        datafile = [line.rstrip('\n') for line in open('admins.txt','rt')]
        my_id = m.from_user.id
        idA, cid = m.chat.id, m.chat.id
        for line in datafile:
            if str(my_id) not in datafile:
                bot.send_message(cid, "Just for admin", parse_mode="Markdown")
                return
        id = m.text.split()[1]

        with open('bb.txt', 'a') as f:
			f.write(str(id)+"\n")
		        print "New User blocked"
        bot.send_message(id, "<b>You are blocked from this bot</b>", parse_mode="HTML")
        bot.send_message(cid, "<b>User blocked</b>", parse_mode="HTML")
        
@bot.message_handler(commands=['ub'])
def answer(m):
        datafile = [line.rstrip('\n') for line in open('admins.txt','rt')]
        my_id = m.from_user.id
        idA, cid = m.chat.id, m.chat.id
        for line in datafile:
            if str(my_id) not in datafile:
                bot.send_message(cid, "Just for admin", parse_mode="Markdown")
                return
        add = m.text.split()[1]
        with open('bb.txt', 'a') as f:
			f.write(line.replace(str(add), '#unblocked'))
		        print "New User unblocked"
        bot.send_message(add, "<b>You are Unblocked from this bot</b>", parse_mode="HTML")
        bot.send_message(cid, "<b>User unblocked</b>", parse_mode="HTML")
        
@bot.message_handler(commands=['newadmin'])
def answer(m):
        datafile = [line.rstrip('\n') for line in open('admins.txt','rt')]
        my_id = m.from_user.id
        idA, cid = m.chat.id, m.chat.id
        for line in datafile:
            if str(my_id) not in datafile:
                bot.send_message(cid, "Just for admin", parse_mode="Markdown")
                return
        id = m.text.split()[1]
        tmt = m.from_user.first_name
        with open('admins.txt', 'a') as f:
			f.write(str(id)+"\n")
		        print "New admin selected."
        bot.send_message(id, "<b>You promoted by </b> <i>{}</i>".format(my_id), parse_mode="HTML")
        bot.send_message(cid, "<i>{}</i> <b>Promoted</b> ".format(id), parse_mode="HTML")
     
@bot.message_handler(commands=['start'])
def welcome(m):
        datafile = [line.rstrip('\n') for line in open('user.txt','rt')]
        id = m.from_user.id
        idA, cid = m.chat.id, m.chat.id
        if str(id) not in datafile:
				with open('user.txt', 'a') as f:
					f.write(str(id)+"\n")
		                print "New user received."
	                        bot.send_message(id, "use /ask <MSG> for ask your question", parse_mode="Markdown")
        return
@bot.message_handler(commands=['stats'])
def check(m):
        datafile =  [line.rstrip('\n') for line in open('admins.txt','rt')]
        id = m.from_user.id
        cid = m.chat.id
        print datafile
        for line in datafile:
            if str(id) not in datafile:
                bot.send_message(cid, "Just for admin", parse_mode="Markdown")
                return
        num_lines = sum(1 for line in open('user.txt'))
        num_lines2 = sum(1 for line in open('chat.txt'))
        bb = sum(1 for line in open('bb.txt'))
        us_stats = file("user.txt", "r").readlines()[-10:]
        us_stats = ' '.join(us_stats)
	bot.send_message(cid, "<b>Users :</b><i>{}</i>\n <b>Chats :</b><i>{}</i>\n<b>Total blocked user :</b><i>{}</i>\n <b>10 New user :</b>\n<i>{}</i>   ".format(num_lines,num_lines2,bb,us_stats), parse_mode="HTML")
   
def handle_messages(messages):
    for m in messages:
        prcs_msg(m)

def prcs_msg(m):
    cid = m.chat.id
    if str(cid) in loggingIDs:
        try:
            bot.forward_message(int(loggingIDs[str(cid)]), cid, m.message_id)
        except:
            pass

@bot.message_handler(commands=['id'])
def id(m):
    cid = m.chat.id
    uid = m.from_user.id
    if cid > 0:
        bot.send_message( cid, "Hi %s , Your ID is %s.\n" %(m.from_user.first_name, cid))
        print "ID command received"
    else:
        bot.send_message( cid, "Hi %s , The group ID is %s.\n" %(m.from_user.first_name, cid))
        print "ID command received"

		
bot.set_update_listener(handle_messages)

bot.polling(none_stop=True, interval=0, timeout=3)
