#! /bin/sh

tmux new -d -s "telegram"
tmux send-keys -t telegram "./run_segmentation_bot.sh" ENTER

tmux new-window -t telegram -n srvision_api
tmux send-keys -t telegram:srvision_api "./run_srVisionAPI_bot.sh" ENTER

tmux new-window -t telegram -n srvision_dev
tmux send-keys -t telegram:srvision_dev "./run_srVisionDev_bot.sh" ENTER

tmux new-window -t telegram -n wiki 
tmux send-keys -t telegram:wiki "./run_wiki_bot.sh" ENTER
