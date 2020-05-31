class Player:
    def __init__(self, name, num, team, category):
        self.name = name
        self.num = num
        self.team = team
        self.category = category

    # region getters(player)
    def get_name(self):
        return self.name

    def get_num(self):
        return self.num

    def get_team(self):
        return self.team

    def get_category(self):
        return self.category

    # endregion

    # region setters(player)
    def set_name(self, name):
        self.name = name

    def set_num(self, num):
        self.num = num

    def set_team(self, team):
        self.team = team

    def set_category(self, category):
        self.category = category
    # endregion


class Batsman(Player):
    def __init__(self, name, num, team, category):
        super().__init__(name, num, team, category)
        self.fours = None
        self.sixs = None
        self.catch = None
        self.runs = None
        self.run_out = None
        self.balls_faced = None
        self.strike_rate = None

    # region getters(batsmen)
    def get_fours(self):
        return self.fours

    def get_sixs(self):
        return self.sixs

    def get_catch(self):
        return self.catch

    def get_runs(self):
        return self.runs

    def get_run_out(self):
        return self.run_out

    def get_balls_faced(self):
        return self.balls_faced

    def get_strike_rate(self):
        self.strike_rate = self.runs / self.balls_faced * 100
        return self.strike_rate
    # endregion

    # region setters(batsmen)
    def set_fours(self, fours):
        self.fours = fours

    def set_sixs(self, sixs):
        self.sixs = sixs

    def set_catch(self, catch):
        self.catch = catch

    def set_runs(self, runs):
        self.runs = runs

    def set_run_out(self, run_out):
        self.run_out = run_out

    def set_balls_faced(self, balls_faced):
        self.balls_faced = balls_faced

    # def set_strike_rate(self, strike_rate):
    #     self.strike_rate = strike_rate
    # endregion


class Bowler(Player):
    def __init__(self, name, num, team, category):
        super().__init__(name, num, team, category)
        self.over = None
        self.wicket = None
        self.maiden = None
        self.economy = None
        self.fours_given = None
        self.sixs_given = None
        self.catch = None
        self.runs_given = None
        self.run_out = None

    # region getters(bowler)
    def get_over(self):
        return self.over

    def get_wicket(self):
        return self.wicket

    def get_maiden(self):
        return self.maiden

    def get_economy(self):
        self.economy = self.runs_given / self.over
        return self.economy

    def get_fours_given(self):
        return self.fours_given

    def get_sixs_given(self):
        return self.sixs_given

    def get_catch(self):
        return self.catch

    def get_runs_given(self):
        return self.runs_given

    def get_run_out(self):
        return self.run_out
    # endregion

    # region setters(bowler)
    def set_over(self, over):
        self.over = over

    def set_wicket(self, wicket):
        self.wicket = wicket

    def set_maiden(self, maiden):
        self.maiden = maiden

    # def set_economy(self, economy):
    #     self.economy = economy

    def set_fours_given(self, fours_given):
        self.fours_given = fours_given

    def set_sixs_given(self, sixs_given):
        self.sixs_given = sixs_given

    def set_catch(self, catch):
        self.catch = catch

    def set_runs_given(self, runs_given):
        self.runs_given = runs_given

    def set_run_out(self, run_out):
        self.run_out = run_out
    # endregion


class WicketKeeper(Batsman):
    def __init__(self, name, num, team, category):
        super().__init__(name, num, team, category)
        self.stumping = None

    def get_stumping(self):
        return self.stumping

    def set_stumping(self, stumping):
        self.stumping = stumping


class AllRounder(Batsman, Bowler):
    pass