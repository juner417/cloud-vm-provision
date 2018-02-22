#!/usr/bin/python
#-*- coding: utf-8 -*-

import boto.ec2

ec2_connection = boto.ec2.connect_to_region('ap-northeast-2')

reservations = ec2_connection.get_all_reservations()
#reservations = ec2_connection.get_all_reservations(
#    filters={'instance-state-name': 'runnig'})

print(reservations)

for reservation in reservations:
    for instance in reservation.instances:
        #print(instance.instance_id, instance.instance_type)
        print(instance)
