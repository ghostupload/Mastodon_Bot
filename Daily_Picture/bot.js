require('dotenv').config();
const Mastodon = require('mastodon-api');
const util = require('util');
const fs = require('fs');
const exec = util.promisify(require('child_process').exec);
const cronJob = require("cron").CronJob;

console.log('Mastodon Bot Running...')

const M = new Mastodon({
    client_key: process.env.CLIENT_KEY,
    client_secret: process.env.CLIENT_SECRET,
    access_token: process.env.ACCESS_TOKEN,
    timeout_ms: 60*1000, 
        //optional HTTP request timeout to apply to all requests.
    api_url: 'https://botsin.space/api/v1/',
})

const pick_a_pic = 'python `pwd`/pick_a_pic.py';

new cronJob(
    "0 0 0,6,22 * * *",	//每天0点、6点、22点整发图。
    function tooting() {
        toot()
       .then(response => console.log(response))
       .catch(error => console.error(error));
    },
    null,
    true,
    "Asia/Shanghai"
  );

async function toot() {
    // Step 1 Random Pick
    const pyResponse = await exec(pick_a_pic);
    const alt = pyResponse.stdout;    //获取python输出的图片描述

    // Step 2 Upload
    const mediaContent = {
        file: fs.createReadStream('img.jpg'),
        description: alt,
    }
    const mediaResponse = await M.post('media', mediaContent);

    // Step 3 Toot!
    const tootContent = {
        media_ids: [mediaResponse.data.id],
    }
    const tootResponse = await M.post('statuses', tootContent)
    const result = alt + tootResponse.data.url + '\n' + tootResponse.data.created_at + '\n'
    return result;
    }
