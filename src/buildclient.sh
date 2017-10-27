#!/bin/bash

sed -i -e "s/http:\/\/localhost:8000//g" client/actions/types.js

npm run build:client

sed -i -e "s/'';/'http:\/\/localhost:8000';/g" client/actions/types.js
rm client/actions/types.js-e
