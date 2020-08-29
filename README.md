<h1 align="center">Youtube Status (README)</h1>
<p align="center">View your Channel.</p>

<p align="center">

<p align="center">

![Image of Sandro Cagara](https://i.ibb.co/JH8xJxk/README-Youtube-Status-v2.jpg)
<p align="center">
   <h3>Demo</h3>
   <img src="https://youtube-status.vercel.app/api/run-youtube-status" alt="Youtube Channel" width="500" />
<p align="center">

Google Developer
------
 * Create account here: https://console.developers.google.com
 * Go to **Credentials**
 * Click **+ Create Credentials** then choose Api Key
 * Get your API KEY (ex: AI*****************************)
 * After you get yout Api key you need to **Restrict** it.
 * Find **API restrictions** then select **Youtube Data API V3**.
   - **Note:** Make sure you enable [Youtube Data API V3](https://console.developers.google.com/apis/library)
 * Save

Configure Vercel Application
------
* Fork this [Youtube Status](https://github.com/sndrjhlncgr/README-Youtube-Status)

* Register on [Vercel](https://vercel.com/)

* Create project linked to your forked respository
  
  ![Vercel](https://i.ibb.co/sHhywHD/dasddas.jpg)

* Add Project Name and Environment Variables:
  - `YOUTUBE_API_KEY`
  - `YOUTUBE_CHANNEL_ID`
        
  ![Vercel](https://i.ibb.co/vv5z4yP/Untitled.png)
  
 * Deploy

Put this in your README.md
------
``` 
[<img src="https://{DOMAIN_OF_YOUR_VERCEL_APP}/api/run-youtube-status" alt="Your alt what" width="350" />](LINK_TO_YOUR_ACCOUNT)
```

Contribution
------
Feel Free to contribute, PR are the most welcome :)

License
------
Copyright (c) 2020 Sandro Cagara | Youtube Status

