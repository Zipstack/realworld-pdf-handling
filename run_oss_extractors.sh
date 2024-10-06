#!/bin/bash

session="osslibs"

tmux new -s $session -d

# start camelot
tmux rename-window -t $session:0 camelot1
tmux send-keys -t $session 'source venv/bin/activate' C-m
tmux send-keys -t $session 'python camelot_extract.py clean/Chase\ Freedom.pdf' C-m

tmux new-window -t $session
tmux rename-window -t $session camelot2
tmux send-keys -t $session 'source venv/bin/activate' C-m
tmux send-keys -t $session 'python camelot_extract.py clean/Apple_10-Q-Q2-2024.pdf' C-m

# start PDF Plumber
tmux new-window -t $session
tmux rename-window -t $session pplumber1
tmux send-keys -t $session 'source venv/bin/activate' C-m
tmux send-keys -t $session 'python pdf_plumber_extract.py clean/Chase\ Freedom.pdf' C-m

tmux new-window -t $session
tmux rename-window -t $session pplumber2
tmux send-keys -t $session 'source venv/bin/activate' C-m
tmux send-keys -t $session 'python pdf_plumber_extract.py clean/Apple_10-Q-Q2-2024.pdf' C-m

# start Tabula
tmux new-window -t $session
tmux rename-window -t $session tabula1
tmux send-keys -t $session 'source venv/bin/activate' C-m
tmux send-keys -t $session 'python tabula_extract.py clean/Chase\ Freedom.pdf' C-m

tmux new-window -t $session
tmux rename-window -t $session tabula2
tmux send-keys -t $session 'source venv/bin/activate' C-m
tmux send-keys -t $session 'python tabula_extract.py clean/Apple_10-Q-Q2-2024.pdf' C-m

# finally
tmux select-window -t $session:0
tmux attach -t $session


