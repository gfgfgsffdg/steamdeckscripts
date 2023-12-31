sudo pacman -S base-devel
sudo pacman -S openssl
rm -rf paru
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
cd ..
rm -rf paru
