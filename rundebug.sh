#!/bin/bash

export PYTHONPATH=$(dirname $(readlink -f "$0"))/src:$PYTHONPATH
python cherrybased
