#!/bin/bash -e

function exit_usage() {
  echo "Usage: $0 robot_name"
  exit $1
}

robots=("dingo")
robot=$1

if [ -z $robot ]; then
  exit_usage -1
fi

shift
files=(${@})


if [ ${#files[@]} -gt 0 ]; then
  for file in ${files[@]}; do
    echo -e "Sending $file to ${robot}:D:\user\alan\fll\FLL-SuperPowered-Rockets$(dirname $file)"
    scp $file robot@${robot}.local:D:\\user\\alan\\fll\\FLL-SuperPowered-Rockets$(dirname $file)
  done
else
  echo -e "\nSending all files to ${robot}:"
  scp D:\\user\\alan\\fll\\FLL-SuperPowered-Rockets\\*.py robot@${robot}.local:~/FLL-SuperPowered
  [[ $? -eq 0 ]] || (echo "Error sending files to ${robot}"; exit -1)
  scp -r D:\\user\\alan\\fll\\FLL-SuperPowered-Rockets\\modules robot@${robot}.local:~/FLL-SuperPowered/
  [[ $? -eq 0 ]] || (echo "Error sending files to ${robot}"; exit -1)
fi

echo "done"
