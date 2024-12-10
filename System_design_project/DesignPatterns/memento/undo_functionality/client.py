from configuration_caretake import ConfigurationCareTaker
from configuration_memento import ConfiguarionMemento
from configuration_originator import ConfigurationOriginator

if __name__ == "__main__":

    care_taker_object: ConfigurationCareTaker = ConfigurationCareTaker()

    # initial state of originator
    originator_object: ConfigurationOriginator = ConfigurationOriginator(height=5, width=10)

    # save it
    snapshot1: ConfiguarionMemento = originator_object.create_memento()

    # add it to history
    care_taker_object.add_memento(snapshot1)

    # originator changing to new state
    originator_object.set_height(7)
    originator_object.set_width(12)

    # save it
    snapshot2: ConfiguarionMemento = originator_object.create_memento()

    # add it to hsitory
    care_taker_object.add_memento(snapshot2)

    # originator changing to new state
    originator_object.set_height(9)
    originator_object.set_width(14)

    # Undo

    restore_state_memento_obj: ConfiguarionMemento = care_taker_object.undo()
    originator_object.restore_memento(restore_state_memento_obj)

    print(f"Height : {originator_object.height}, Width : {originator_object.width}")