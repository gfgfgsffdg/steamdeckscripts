sudo steamos-readonly disable
echo "keyserver hkps://keyserver.ubuntu.com" >> /etc/pacman.d/gnupg/gpg.conf
sudo pacman-key --init
sudo pacman-key --populate
sudo pacman-key --refresh-keys
