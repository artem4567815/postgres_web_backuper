sudo pip3 install -r requirements.txt
sudo cp backuper.conf /etc/supervisor/conf.d/
sudo cp backuper_nginx.conf /etc/nginx/sites-enabled/
sudo supervisorctl update
sudo systemctl restart nginx
sudo certbot --nginx -d backuper.medsenger.ru
cp config.py.example config.py