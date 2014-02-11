#!/bin/bash
ps aux|grep "./standalone.py \-p 8998"|awk '{print $2}'|xargs kill -9
