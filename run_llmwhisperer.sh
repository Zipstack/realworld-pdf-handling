#!/bin/bash

session="llmwhisperer"

tmux new -s $session -d

# Clean PDFs
tmux rename-window -t $session:0 llmw-clean-1
tmux send-keys -t $session 'source venv/bin/activate' C-m
tmux send-keys -t $session 'python llmwhisperer_extract.py clean/Chase\ Freedom.pdf' C-m

tmux new-window -t $session
tmux rename-window -t $session llmw-clean-2
tmux send-keys -t $session 'source venv/bin/activate' C-m
tmux send-keys -t $session 'python llmwhisperer_extract.py clean/Apple_10-Q-Q2-2024.pdf' C-m

# Electronically filled PDF
tmux new-window -t $session
tmux rename-window -t $session llmw-pdf-form
tmux send-keys -t $session 'source venv/bin/activate' C-m
tmux send-keys -t $session 'python llmwhisperer_extract.py forms/1003-sample.pdf' C-m

# Handwritten form
tmux new-window -t $session
tmux rename-window -t $session llmw-handwritten
tmux send-keys -t $session 'source venv/bin/activate' C-m
tmux send-keys -t $session 'python llmwhisperer_extract.py handwritten/Scanned\ Loan\ Application.pdf' C-m

# Smartphone-captured
tmux new-window -t $session
tmux rename-window -t $session llmw-smartphone
tmux send-keys -t $session 'source venv/bin/activate' C-m
tmux send-keys -t $session 'python llmwhisperer_extract.py smartphone_cam/food_receipt_phone.pdf' C-m

# finally
tmux select-window -t $session:0
tmux attach -t $session

