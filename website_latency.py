import urllib.request
from time import time


def prRed(skk): print("\033[91m{}\033[00m".format(skk))


def prGreen(skk): print("\033[92m{}\033[00m".format(skk))


def prCyan(skk): print("\033[96m{}\033[00m".format(skk))


websites = ['https://www.android.com/',
            'https://www.google.co.in',
            'https://www.google.co.uk',
            'https://mail.google.com',
            'https://www.youtube.com',
            'https://www.facebook.com',
            'https://en.wikipedia.org',
            'https://outlook.live.com/owa/',
            'https://in.yahoo.com/?p=us',
            'https://msn.com',
            'https://dropbox.com',
            'https://ubuntu.com/',
            'https://store.steampowered.com/']
web_names = ['Android       ',
             'Google India  ',
             'Google UK     ',
             'Gmail         ',
             'Youtube       ',
             'Facebook      ',
             'Wikipedia     ',
             'Outlook Mail  ',
             'Yahoo India   ',
             'MSN India     ',
             'DropBox       ',
             'Ubuntu        ',
             'Steam         ']
print('                    --------------------------------------')
print('                    || WEBSITE_NAME   ||    LATENCY     ||')


def latency_check(url, urlname):
    stream = urllib.request.urlopen(url)
    start_time = time()
    data = stream.read()
    end_time = time()
    f_time = round(end_time - start_time, 3)
    str_ftime: str = str(f_time)
    if f_time < 0.5:
        print('                    --------------------------------------')
        prGreen("                    ||  " + urlname + "||" + "  " + str_ftime + " Seconds" + " ||")

    elif 0.5 < f_time < 1:
        print('                    --------------------------------------')
        prCyan("                    ||  " + urlname + "||" + "  " + str_ftime + " Seconds" + " ||")
    else:
        print('                    --------------------------------------')
        prRed("                    ||  " + urlname + "||" + "  " + str_ftime + " Seconds" + " ||")


a = 0
while a != len(websites):
    latency_check(websites[a], web_names[a])
    a = a + 1
print("                    Calculation Complete")
