pushd $hdwyDnld &> /dev/null
function getAssembler {
    IFS=$''
    if [ -d $HOME/Dropbox\ \(Headway\ Services\)/Tunnel_HeadwayServices_Rorohiko/ ]; then
        tunnel=$HOME/Dropbox\ \(Headway\ Services\)/Tunnel_HeadwayServices_Rorohiko/
        zipFile=`ls -laht ${tunnel} | grep XMLIngester | head -n 1 | awk '{print $NF}'`
        rm -r $hdwyDnld/archive &> /dev/null
        if [ ! -d $hdwyDnld/archive ]; then
            mkdir $hdwyDnld/archive
            chmod 700 $hdwyDnld/archive
        fi
        cp $tunnel/$zipFile $hdwyDnld/archive
        chmod 700 $hdwyDnld/archive/$zipFile
        yes | unzip $hdwyDnld/archive/$zipFile &> /dev/null
        mv -f $hdwyDnld/XMLIngester* $hdwyDnld/archive
        rm $hdwyDnld/archive/XMLIngester*.zip
        pushd $hdwyDnld/archive/XMLIngester*  &> /dev/null
        yes | unzip Assembler_Mac.zip  &> /dev/null
        popd  &> /dev/null
    fi
    IFS=$'\n'
}
getAssembler
