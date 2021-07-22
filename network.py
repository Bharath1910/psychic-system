import speedtest
from plyer import notification

def speedtest():
    notification.notify(
        title = "Starting Speedtest..",
        message = "Please Standby..",
        app_icon = "/home/bharath/Downloads/Speed.png"

    )

    s = speedtest.Speedtest()

    Download_speed = s.download()
    Upload_speed = s.upload()

    notification.notify(
        title = "Network Speed",
        message = f"Download Speed {round(Download_speed/1000000, 2)} Mbps, Upload Speed {round(Upload_speed/1000000, 2)} Mbps",
        app_icon = "/home/bharath/Downloads/Speed.png"
)

speedtest()