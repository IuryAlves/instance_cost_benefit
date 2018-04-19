#!/usr/bin/env python
# coding: utf-8

import csv
import sys


INSTANCE_TYPE_COLUMN_HEADER = 'instance_type'
VIRTUALIZATION_COLUMN_HEADER = 'virtualization'
VCPU_COLUMN_HEADER = 'vcpu'
COST_COLUMN_HEADER = 'cost'
MEMORY_COLUMN_HEADER = 'memory'


def convert_file_lines_to_lower_case(file_):
    for line in file_:
        yield line.lower()


def get_instances_info_from_files(file_names):
    instances = {}
    for file_name in file_names:
        with open(file_name) as file_:
            csv_reader = csv.DictReader(
                convert_file_lines_to_lower_case(file_),
                delimiter=','
            )

            for row in csv_reader:
                instance_type = row.pop(INSTANCE_TYPE_COLUMN_HEADER, None)
                if instance_type is not None:
                    if instance_type not in instances:
                        instances[instance_type] = row
                    else:
                        instances[instance_type].update(row)
    return instances


def calculate_cost_benefit(memory, vcpu, cost):
    memory = float(memory)
    vcpu = int(vcpu)
    cost = float(cost)
    return ((memory / 3.75) + vcpu) / cost


def filter_by_virtualization_type(instances, virtualization):
    def _filter_by_virtualization_type(instance_type):
        instance = instances[instance_type]
        return instance.get(VIRTUALIZATION_COLUMN_HEADER) == virtualization

    return filter(
        _filter_by_virtualization_type,
        instances
    )


def main(file_names, virtualization_type='hvm'):
    instances = get_instances_info_from_files(file_names)
    instance_cost_benefit = {}
    for instance_type in filter_by_virtualization_type(
            instances, virtualization_type):
        instance = instances[instance_type]
        vcpu = instance.get(VCPU_COLUMN_HEADER)
        memory = instance.get(MEMORY_COLUMN_HEADER)
        cost = instance.get(COST_COLUMN_HEADER)
        if all([vcpu, memory, cost]):
            instance_cost_benefit[instance_type] = calculate_cost_benefit(
                memory, vcpu, cost
            )

    return sorted(
        instance_cost_benefit,
        key=lambda key: instance_cost_benefit[key],
        reverse=True
        )


if __name__ == '__main__':
    result = main(sys.argv[1:])

    for instance_type in result:
        print(instance_type)
