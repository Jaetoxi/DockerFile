�޸����²���:
����docker ʵ��
1. docker exec -t "master" bash
   a) �޸�/etc/mysql/my.conf
      bind_ip = 0.0.0.0
      max_connection =500
    b)run: mysql
        CREATE USER 'user-dev'@'%' IDENTIFIED BY '12345678';
        GRANT ALL PRIVILEGES ON * . * TO 'user-dev'@'%';
        FLUSH PRIVILEGES;
     
     �鿴�û���Ϣ
        SELECT user, host FROM mysql.user;

2. ���澵��
apt-get install phpmyadmin
3. phpmyadmin 
     vim /etc/phpmyadmin/config.inc.php
    $cfg['Servers'][$i]['host'] = '127.0.0.1';
    $cfg['Servers'][$i]['controluser'] = 'dev-user';
    $cfg['Servers'][$i]['controlpass'] = '12345678';