import time
import states
import items


class BaseGameEntity:
    """Defines the class which game object's that are characters fall into. """
    id = 0

    def __init__(self):
        self.id = BaseGameEntity.id
        BaseGameEntity.id += 1


class Miner(BaseGameEntity):
    """The Miner game object."""
    def __init__(self, name, current_state, location, gold_carried, gold_bank, thirst, fatigue, build, pickax):
        """ This BaseGameEntitiy's __init__ the variables name, current state, current location,
            amount of gold carried, amount of gold in the bank, thirst, fatigue, max amount of gold that can be carried,
            whether or not miner is in jail, number of times miner has been to jail, whether ot not the miner has a pickaxe, and
            what type of build a miner has (which determines his hitpoints and strength)."""
        super(Miner, self).__init__()
        self.name = name
        self.current_state = current_state
        self.location = location
        self.gold_carried = gold_carried
        self.gold_bank = gold_bank
        self.thirst = thirst
        self.fatigue = fatigue
        self.status = 'free'
        self.counter_jail = 0
        self.max_nuggets = 7
        self.pickax = pickax
        if build == "lanky":
            self.health = 30
            self.strength = 3 + self.pickax.strength
        if build == "normal":
            self.health = 50
            self.strength = 5 + self.pickax.strength
        if build == "bulky":
            self.health = 70
            self.strength = 7 + self.pickax.strength

    def update(self):
        """This gives the miner +1 thirst and executes a state."""
        self.thirst += 1
        self.current_state.execute(self)

    def change_state(self, new_state):
        """This exits the current state, changes the current state, and then enters the new state."""
        self.current_state.exit(self)
        self.current_state = new_state
        self.current_state.enter(self)

    def pockets_full(self):
        """Checks if gold_carried is equal to max_nuggets. If this is true, then his pockets are full."""
        if self.gold_carried > self.max_nuggets:
            return True
        else:
            return False

    def thirsty(self):
        """The miner is thirsty if his thirst exceeds 10."""
        if self.thirst > 10:
            return True
        else:
            return False

    def is_tired(self):
        """The miner is tired if his fatigue exceeds 10."""
        if self.fatigue > 10:
            return True
        else:
            return False

class Wife(BaseGameEntity):
    """The Miner's Wife game object """
    def __init__(self, name, wife_state, location, fatigue, dishes_washed, shirts_ironed, cups_made):
        """This BaseGameEntity's __init__ includes the variables name, current state, current location, fatigue,
            whether or not the dishes have been washed, whether or not the shirts have been ironed, how many cups of
            coffee she has made, and the max amount of coffee she can make."""
        super(Wife, self).__init__()
        self.name=name
        self.wife_state=wife_state
        self.location=location
        self.fatigue=fatigue
        self.dishes_washed=dishes_washed
        self.shirts_ironed=shirts_ironed
        self.cups_made = cups_made
        self.max_cups = 2

    def update(self):
        """This gives the wife +1 fatigue and executes a state."""
        self.fatigue+=1
        self.wife_state.execute(self)

    def wife_change_state(self, new_state):
        """This exits the current state, changes the current state, and then enters the new state."""
        self.wife_state.exit(self)
        self.wife_state=new_state
        self.wife_state.enter(self)

    def tired(self):
        """The wife is tired if her fatigue exceeds 10."""
        if self.fatigue > 4:
            return True
        else:
            return False

    def coffee_made(self):
        """Checks if cups_made is equal to max_cups, and if this is true, the coffee has been made."""
        if self.cups_made == self.max_cups:
            return True
        else:
            return False

if __name__ == '__main__':
    real_miner = Miner('Bob',
                       states.enter_mine_and_dig_for_nugget,
                       'home',
                       0,
                       0,
                       0,
                       0,
                       "bulky",
                       items.small_pickax)
    other_miner = Miner('Sam',
                        states.enter_mine_and_dig_for_nugget,
                        'home',
                        1,
                        10,
                        0,
                        0,
                        "lanky",
                        items.small_pickax)

    miner_wife = Wife('Deloris',
                      states.wake_up_and_make_coffee,
                      'home',
                      0,
                      0,
                      0,
                      0)

    game_objects = [real_miner, other_miner, miner_wife]
    counter = 0
    while counter < 50:
        print("Game tick {}".format(counter))
        for obj in game_objects:
            obj.update()
        time.sleep(0.5)
        counter += 1
