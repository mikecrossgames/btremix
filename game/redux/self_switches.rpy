default self_switches = {}

init python:
    def set_self_switch(called_from, event_id, switch_id, value):
        if not called_from in self_switches:
            self_switches[called_from] = {}
        if not event_id in self_switches[called_from]:
            self_switches[called_from][event_id] = {}
        self_switches[called_from][event_id][switch_id] = value

    def self_switch(called_from, event_id, switch_id):
        if not called_from in self_switches:
            return False
        if not event_id in self_switches[called_from]:
            return False
        if not switch_id in self_switches[called_from][event_id]:
            return False
        if self_switches[called_from][event_id][switch_id] == None:
            return False
        return self_switches[called_from][event_id][switch_id]