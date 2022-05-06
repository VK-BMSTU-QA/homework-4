#!/bin/bash
echo "chrome version ${CHROME_VERSION}"
echo "arch ${ARCH}"
echo "platform ${PLATFORM}"

ARCH=$(uname -a | grep -E -o 'x86_64|arm64')

if ! [ -e chromedriver ]; then
  if [ "${ARCH}" = "x86_64" ]; then
    if [ ${CHROME_VERSION} -eq 102 ]; then
      echo '1 x86_64' && curl -O https://chromedriver.storage.googleapis.com/102.0.5005.27/chromedriver_mac64.zip
    elif [ ${CHROME_VERSION} -eq 101 ]; then
      echo '2 x86_64' && curl -O https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_mac64.zip
    elif [ ${CHROME_VERSION} -eq 100 ]; then
      echo '3 x86_64' && curl -O https://chromedriver.storage.googleapis.com/100.0.4896.60/chromedriver_mac64.zip
    else
      echo '4 x86_64' && curl -O https://chromedriver.storage.googleapis.com/99.0.4844.51/chromedriver_mac64.zip
    fi
    unzip chromedriver_mac64.zip
  else
    if [ ${CHROME_VERSION} -eq 102 ]; then
      echo '1 arm' && curl -O https://chromedriver.storage.googleapis.com/102.0.5005.27/chromedriver_mac64_m1.zip
    elif [ ${CHROME_VERSION} -eq 101 ]; then
      echo '2 arm' && curl -O https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_mac64_m1.zip
    elif [ ${CHROME_VERSION} -eq 100 ]; then
      echo '3 arm' && curl -O https://chromedriver.storage.googleapis.com/100.0.4896.60/chromedriver_mac64_m1.zip
    else
      echo '4 arm' && curl -O https://chromedriver.storage.googleapis.com/99.0.4844.51/chromedriver_mac64_m1.zip
    fi
    unzip chromedriver_mac64_m1.zip
  fi
fi
