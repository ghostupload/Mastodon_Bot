## Daily Picture

<br/>

### 运行
```
pm2 start pm2_daily_pic.json
```

<br/><br/>

### 简介
每天在自定义时间发图片的Mastodon Bot.

原图文件夹（默认为screenshots）中应有jpg文件和对应的文件名列表list.txt，图片将按list.txt的顺序发布。  
pm2保护运行，配置文件为pm2_daily_pic.json

#### pick_a_pic.py
选择一张图片，选择记录单独保存在imgpicked.log中。

#### bot.js
定时发布图片。

#### .env
填写账号信息，可在Mastodon的Preferences-Development（设置-开发）中设置。无需添加引号。