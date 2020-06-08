cp -r Galaxies ./Accretion
cd Accretion
./run.sh
echo accretion finished
rm -r Galaxies
cd ../
cp -r Galaxies ./Stellar
cd Stellar
./run.sh
echo stellar finished
rm -r Galaxies
cd ../
