#!/bin/bash

for dir in /vols/cms/ZGammaRatio/80X/Data/20170518_S02/AtLogic_Data/*; do
	cd $dir
	if [[ -d Loop ]]; then
		mv Loop/* .
	fi
	cd ../
done
