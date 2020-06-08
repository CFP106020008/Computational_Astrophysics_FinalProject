cd ./Galaxies
filelist=$(ls ${dir})
cd ../
echo ${filelist}
for filename in ${filelist}
do
    cp ./Galaxies/${filename}/*star* ./star.txt
    cp ./Galaxies/${filename}/*gas* ./dust.txt
    echo ${filename}
    python Make_Files.py
    python set_skirt_scale.py
    skirt Dusty.ski
    rm DustSphere*
    mv ./*_xy_sed.dat ./Datas/Accretion_xy_${filename}.dat
    mv ./*_xz_sed.dat ./Datas/Accretion_xz_${filename}.dat
done
mv ./Datas/* ../Datas
