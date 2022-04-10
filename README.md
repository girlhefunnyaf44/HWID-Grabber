## HWID-Grabber

 This is a easy to use HWID grabber that copys and pastes ur HWID to ur clipboard. 

## Info

It grabs ur HWID from here by default but edit it to whatever suits ur needs

subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
