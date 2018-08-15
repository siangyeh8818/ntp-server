#!/bin/bash

#ansible all -i hosts -m ping
ansible all -i hosts-list -m "command" -a "date"
