class State:
    def enter(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError

    def exit(self):
        raise NotImplementedError


class EnterMineAndDigForNugget(State):
    def enter(self, miner):
        if miner.location != 'goldmine':
            print("Miner {}: Walkin' to the gold mine".format(miner.name))
            miner.location = 'goldmine'

    def execute(self, miner):
        miner.gold_carried += 1
        miner.fatigue += 1
        print("Miner {}: Picking up a nugget!".format(miner.name))
        #reversed order of if statements
        if miner.thirsty():
            miner.change_state(quench_thirst)
        if miner.pockets_full():
            miner.change_state(visit_bank_and_deposit_gold)

    def exit(self, miner):
        print("Miner {}: Ah'm leavin' the gold mine with mah pockets full o'sweet gold".format(miner.name))


class VisitBankAndDepositGold(State):
    def enter(self, miner):
        if miner.location != 'bank':
            print("Miner {}: Goin' to the bank. Yes siree".format(miner.name))
            miner.location = 'bank'

    def execute(self, miner):
        miner.gold_bank += miner.gold_carried
        miner.gold_carried = 0
        print("Miner {}: Depostin' gold. Total savings now: {}".format(miner.name,
                                                                       miner.gold_bank))
        if miner.gold_bank > 4:
            print("Miner {}: Woohoo! Rich enough for now. Back home to mah li'l lady".format(miner.name))
            miner.change_state(go_home_and_sleep_till_rested)
        else:
            miner.change_state(enter_mine_and_dig_for_nugget)

    def exit(self, miner):
        print("Miner {}: Leavin' the bank".format(miner.name))


class GoHomeAndSleepTillRested(State):
    def enter(self, miner):
        if miner.location != 'home':
            print("Miner{}: Going Home to see my lil' lady".format(miner.name))
            miner.location = 'home'

    def execute(self, miner):
        miner.fatigue -= 1 #changed from miner.fatigue = 0 to miner.fatigue -= 1
        miner.thirst += 1
        #print("Miner {}: Good Mornin'!!".format(miner.name))
        # new 'if' statement that makes the accumulation of fatigue no longer arbitrary
        if miner.is_tired():
            miner.change_state(go_home_and_sleep_till_rested)
            print("Miner {}: Just 5 more minutes...".format(miner.name)) #new dialogue
        if miner.thirsty():
            miner.change_state(quench_thirst) #changed from 'go_home_and_sleep_till_rested' to 'quench_thirst'.
        else:
            miner.change_state(enter_mine_and_dig_for_nugget)

    def exit(self, miner):
        print("Miner {}: Good mornin'! Another day, another nugget!".format(miner.name)) #updated miner exit dialogue
        

class QuenchThirst(State):
    def enter(self, miner):
        if miner.location != 'saloon':
            print("Miner {}: So thirsty! Ima go get me cold one".format(miner.name))
            miner.location = 'saloon'

    def execute(self, miner):
        miner.fatigue += 1
        miner.thirst -= 3 #changed miner.thirst = 0 to miner.thirst -= 3
        #print("Miner {}: Whew! That really wet my wistle".format(miner.name))
        print("Miner {}: That's some fine sippin' liquor.".format(miner.name))  # new dialogue
        #new if statement to make the accumulation of thirst no longer arbitrary
        if miner.thirsty():
            miner.change_state(quench_thirst)
        #new if statement checking if pockets_full() = True
        if miner.pockets_full():
            miner.change_state(visit_bank_and_deposit_gold)
        if miner.is_tired():
            miner.change_state(go_home_and_sleep_till_rested)
        else:
            #changed location of miner execute dialogue
            print("Miner {}: Whew! That really wet my wistle".format(miner.name))
            miner.change_state(enter_mine_and_dig_for_nugget) #changed visit_bank_and_deposit_gold to enter_mine_and_dig_for_nugget

    def exit(self, miner):
        print("Miner {}: Gotta Get back to it!".format(miner.name))
        

enter_mine_and_dig_for_nugget = EnterMineAndDigForNugget()
visit_bank_and_deposit_gold = VisitBankAndDepositGold()
go_home_and_sleep_till_rested = GoHomeAndSleepTillRested()
quench_thirst = QuenchThirst()
