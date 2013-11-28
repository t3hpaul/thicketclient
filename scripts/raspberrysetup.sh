rm -r Desktop/
rm ocr_pi.png 
rm -r python_games/
echo "Getting update"
apt-get install update
echo "Installing git"
apt-get install git
echo "Installing dependencies for phidgets!"
apt-get install libusb-1.0-0-dev
echo "Installing the phidgets!"
wget http://www.phidgets.com/downloads/libraries/libphidget.tar.gz
tar -xzvf libphidget.tar.gz 
rm libphidget.tar.gz
cd libphidget-2.1.8.20121218/
./configure
make
make install
cd ..
rm -r libphidget-2.1.8.20121218
wget http://www.phidgets.com/downloads/libraries/PhidgetsPython.zip
unzip PhidgetsPython.zip
cd PhidgetsPython
python setup.py install
echo "Installing requests framework"
cd ..
rm -r PhidgetsPython
git clone git://github.com/kennethreitz/requests.git
cd requests
python setup.py install
cd ..
rm -r requests
echo "cloning everything to its correct positions"
git clone https://github.com/t3hpaul/thicketclient.git /etc/thicketclient
cp /etc/thicketclient/scripts/initscript.sh /etc/init.d/thicketclient
echo "Setting up the startup scripts"
cat /etc/thicketclient/scripts/initscript.sh > /etc/init.d/thicketclient
chmod 777 /etc/init.d/thicketclient
echo "Now testing the installation."
python /etc/thicketclient/client/client_main_event.py
mkdir /var/logs/thicketclient 


