read -p "Ingestor path: " ingestor_path # /Users/cary/Downloads/XMLIngester_KC20161012_4.4.1α_1232_e8d3220/Mac\ OS\ X\ \(Intel\)/XMLIngester/
currdir=`pwd`
cd "$ingestor_path"
read -p "Path to xml files: " xml_dir # /Users/cary/Desktop/headway/xml
rm $xml_dir/.DS_Store 2> /dev/null
# rm -r testlogs 2> /dev/null
timestamp=`date "+%m-%d-%yT%H-%M-%S"`
mkdir testlogs_$timestamp
for f in `find $xml_dir | grep .xml`; do
    if [ -f $f ]; then
        echo "Ingesting $f"
        rm /tmp/test.zip 2> /dev/null
        ./XMLIngester -verbosity 2 -blocking -noapps -xml $f -output /tmp/test.zip 2> testlogs_$timestamp/$(basename $f)_`date "+%m-%d-%yT%H-%M-%S"`.log;
    fi
done
zip testlogs_$timestamp.zip testlogs_$timestamp/*
cd $currdir
