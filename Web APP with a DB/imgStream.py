import os
import time
import boto3
import picamera

### Send data to AWS
# Start boto3 client and set up variables
client = boto3.client('s3', region_name='us-west-1')
time_min = 0

while True:
    if (time_min % 10 == 0) :
        os.system(''' aws cloudfront create-invalidation --distribution-id E3MMQ1PO9VN3I1 --paths "/imgStream.png" ''')
        # Take picture
        with picamera.PiCamera() as camera:
            camera.resolution = (1280, 720)
            camera.capture('/home/pi/imgStream.png')
        client.upload_file('/home/pi/imgStream.png', 'pestnodestream', "imgStream.png")
        # print and make imgCount variable plus one
        print("imgStream.png" + " is uploaded to S3 successfully!\n")

    # Count time
    time.sleep(60)
    time_min += 1