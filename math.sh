#!/bin/bash

#initial value of counter is set to 
car=3

while [ $car -le 21 ]
do
   echo $car

    ((counter = $car +3))
done
echo "All done"
