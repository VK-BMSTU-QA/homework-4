SHELL := /bin/bash
MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
PROJECT_DIR := $(patsubst %/,%,$(dir $(MAKEFILE_PATH)))
DRIVER_PATH ?= ${PROJECT_DIR}/bin
PLATFORM ?= $(uname -a | grep -E -o 'Darwin|Linux')
ARCH ?= $(uname -a | grep -E -o 'x86_64|arm64')
CHROME_VERSION ?= 101

${DRIVER_PATH}/chromedriver:
	if ! [ -e ${PROJECT_DIR}/bin ]; then mkdir ${PROJECT_DIR}/bin && \
	chmod +x install.sh && cp install.sh ${PROJECT_DIR}/bin && \
	cd ${PROJECT_DIR}/bin && ./install.sh; fi

deps: ${DRIVER_PATH}/chromedriver
	python3 -m pip install --upgrade pip
	python3 -m pip install flake8
	if [ -f requirements.txt ]; then pip3 install -r requirements.txt; fi

test: deps
	python3 ${PROJECT_DIR}/run_tests.py
