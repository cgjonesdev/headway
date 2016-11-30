read -p "Assembler path: " assembler_path # /Users/cary/Downloads/XMLIngester_KC20161013_4.4.1α_1234_32ec115_WithMacIngester/Assembler_Mac/Assembler.app/Contents/MacOS
currdir=`pwd`
cd "$assembler_path"
read -p "Path to xml files: " xml_dir # /Users/cary/Desktop/xml
rm $xml_dir/.DS_Store 2> /dev/null
# rm -r testlogs 2> /dev/null
timestamp=`date "+%m-%d-%yT%H-%M-%S"`
mkdir testlogs_`$timestamp`
for f in `find $xml_dir | grep .xml`; do
    if [ -f $f ]; then
        echo "Dropping $f onto Assembler"
        ./Assembler $f
        cat ~/Library/Logs/com.rorohiko.merck.AssemblerLog.txt > testlogs_`$timestamp`/$(basename $f)_`date "+%m-%d-%yT%H-%M-%S"`.log;
        rm $currdir/ASSEMBLER*.zip
    fi;
done
cd $currdir
