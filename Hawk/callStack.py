__author__ = 'chenzhi'


class Record(object):
    def __init__(self, order_id, receive_time, host, event_name, operation_signature, clazz, timestamp):
        self._order_id = order_id
        self._receive_time = receive_time
        self._host = host
        self._event_name = event_name
        self._operation_signature = operation_signature
        self._clazz = clazz
        self._timestamp = timestamp
        self._depth = 1
        self._paired = False

    def __init__(self, para_list):
        assert len(para_list) == 7, ("incorrect parameters" + ",".join(para_list))
        self._order_id = para_list[0]
        self._receive_time = para_list[1]
        self._host = para_list[2]
        self._event_name = para_list[3]
        self._operation_signature = para_list[4]
        self._clazz = para_list[5]
        self._timestamp = para_list[6]
        self._depth = 1
        self._paired = False

    def __str__(self):
        return ",".join([str(self._order_id), str(self._receive_time), str(self._host), str(self._event_name),
                        str(self._operation_signature), str(self._clazz), str(self._timestamp)])

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._order_id == other.get_order_id()

    def __gt__(self, other):
        return self._order_id > other.get_order_id()

    def get_depth(self):
        return self._depth

    def set_depth(self, depth):
        self._depth = depth

    def get_order_id(self):
        return self._order_id

    def get_event_name(self):
        return self._event_name

    def get_operation_signature(self):
        return self._operation_signature

    def pair(self):
        self._paired = True

    def is_paired(self):
        return self._paired


class Trace(object):
    def __init__(self, trace_id):
        self._trace_id = trace_id
        self._records = []

    def __getitem__(self, item):
        return self._records[item]

    def __len__(self):
        return len(self._records)

    def __eq__(self, other):
        return self._trace_id == other.trace_id

    def __gt__(self, other):
        return self._trace_id > other.trace_id

    def add_record(self, record):
        self._records.append(record)

    def add_records(self, records):
        self._records.extend(records)

    def correct_order(self):
        self._records = sorted(self._records)

    def correct_depth(self):
        self.correct_order()
        for i in range(1, len(self._records)):
            if self._records[i].get_event_name().startswith("After"):
                for j in range(i-1, -1, -1):
                    if self._records[i].get_operation_signature() == self._records[j].get_operation_signature():
                        self._records[j].pair()
                        break
            if self._records[i].get_event_name().startswith("BeforeOperation"):
                for j in range(i-1, -1, -1):
                    if not self._records[i].is_paired():
                        self._records[i].set_depth(self._records[j].get_depth() + 1)
                        break

    def print_call_stack(self):
        for record in self._records:
            if record.get_event_name().startswith("BeforeOperation"):
                print "\t" * (record.get_depth() - 1), record.get_operation_signature()


if __name__ == "__main__":
    path = "G:\Temp\\traceData\AllData"
    traces = {}
    with open(path, "r") as f:
        lines = f.readlines()
    for line in lines:
        trace_id = line.split(";")[0]
        # print trace_id
        if trace_id not in traces:
            traces[trace_id] = Trace(trace_id)

        record = Record(line.split(";")[1:])
        # print record
        traces[trace_id].add_record(record)

    for trace_id in traces:
        traces[trace_id].correct_depth()
        # print trace_id, traces[trace_id][0]
    print traces["6201970502416728064"].print_call_stack()

