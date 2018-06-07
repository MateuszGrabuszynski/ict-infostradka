guid_path='./guid.conf'

if [ -e $guid_path ]; then
echo 'guid.conf found'
GUID=$(cat ${guid_path})
else
echo 'generating guid'
GUID=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
echo $GUID > $guid_path
fi

if [ -z "$1" -o -z "$2" ]; then
echo "IP address and/or name not specified! Usage: $0 [device_name <string>] [server_ip <IP>]"
exit 0
fi

echo $1 #name
echo $2 #ip
echo $GUID

while true; do
scrot 'infostradka.jpg' -d 5 -q 15 -z
curl -X PUT -F "display_id='{$GUID}'" -F "display_name=$1" -F "screenshot=@./infostradka.jpg" http://$2:8080/v1/api/display/$GUID
done

