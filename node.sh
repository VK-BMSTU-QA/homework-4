#!/usr/bin/env bash

java -Dwebdriver.chrome.driver="./chromedriver" \
    -Dwebdriver.gecko.driver="./geckodriver" \
    -jar selenium-server-4.1.3.jar \
    node \
    --hub http://127.0.0.1:4444/grid/register
    -browser browserName=chrome,maxInstances=8 \
    -browser browserName=firefox,maxInstances=8
