# telegit
GitHub web hooks for your Telegram groups


## 모든 텔레그램 봇 동시에 재시작하기

하나의 스크립트로 재시작을 자동화시켜두었다. `sr2`에서만 작동한다.

``` $ ./run_all.sh ```

## 텔레그램봇 재시작하기

1. sr2 계정으로 sr2 (sr2.snu.ac.kr) 접속
2. tmux 실행 `$ tmux new -s telegram`
3. conda environment 활성화 `$ conda activate telegram`
4. bot 시작 스크립트 실행 `$ cd telegram-bot` 후 `$ ./run_segmentation_bot.sh`
5. 다른bot도 추가로 시작하고 싶을 경우 `<ctrl>+c` 로 새 스크린 생성 후 3번부터 반복.

## Prerequisite 

1. Create a new conda environment `conda create -n telegram`
2. Activate environment `conda activate telegram`
3. Install required packages 
    * `conda install -c conda-forge nodejs`
    * `npm install githubhook ellipsize node-telegram-bot-api yargs`


## Initial Setup
1. `git clone https://github.com/SNURobotics/telegram-bot`
2. `cd telegram-bot`
3. `mkdir ~/.telegit && cp config.example.js ~/.telegit/config.js`
4. Set up your GitHub web hooks. Do this from your repository settings ->
   Webhooks & services.
   1. Payload URL should point to your machine, port 3420, default callback
      path is `/github/callback`. For example:
      http://example.com:3420/github/callback
   2. Content type should be left as `application/json`
   3. Set up a secret so others can't send fake events to your bot. Note
      the secret down, you'll need it soon.
   4. Remember to pick `Send me everything` or `Let me select individual events`
      to choose which events you want to see on Telegram.
5. Set up a Telegram bot with [BotFather](https://telegram.me/botfather),
   store the API token somewhere safe, you'll need it soon
6. Use BotFather's `/setcommands` command on your newly created bot. Paste the
   contents of the [commands.txt](/commands.txt) file to BotFather.
7. Edit the default config: `$EDITOR ~/.telegit/config.js`
8. `npm start`
9. Now invite your bot to a group and greet it with `/gitstart@botname`

You can stop the bot from sending messages with `/gitstop@botname`.



