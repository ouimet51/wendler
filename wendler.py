#This is a Wendler Calulator, a command line tool to give me printed work outs


file = open('wendler.txt','w') #Open a file to write the work out too

#Algo for rounding to nearest 0 or 5
def myround(x, base=5):
    return int(base * round(float(x)/base))

class Exercise():

    def __init__(self, one_rep_max):

        self.one_rep_max = int(one_rep_max)

    def calculate(self):
        '''will calculate all of the needed set weights'''

        self.first_a = myround(self.one_rep_max * .65)
        self.second_a = myround(self.one_rep_max * .75)
        self.third_a = myround(self.one_rep_max * .85)


        self.first_b = myround(self.one_rep_max * .70)
        self.second_b = myround(self.one_rep_max * .80)
        self.third_b = myround(self.one_rep_max * .90)


        self.first_c = myround(self.one_rep_max * .75)
        self.second_c = myround(self.one_rep_max * .85)
        self.third_c = myround(self.one_rep_max * .95)


#Promt the user to get their one rep max for the main lifts
over_head_press = Exercise(input("Over Head Press ORM?... "))
squat = Exercise(input("Squat ORM?... "))
bench_press = Exercise(input("Bench Press ORM?... "))
deadlift =  Exercise(input("Dead Lift ORM?... "))

over_head_press.calculate()
squat.calculate()
bench_press.calculate()
deadlift.calculate()

text = ["531 Workout\n\n",

        f"Over Head Press -  1RM {over_head_press.one_rep_max}",
        "\n",
        "Wave A\n",
        f"{over_head_press.first_a} X 5 - 65%\n",
        f"{over_head_press.second_a} X 5 - 75%\n",
        f"{over_head_press.third_a} X 5 - 85%\n",
        "\n",
        "Wave B\n",
        f"{over_head_press.first_b} X 3 - 70%\n",
        f"{over_head_press.second_b} X 3 - 80%\n",
        f"{over_head_press.third_b} X 3 - 90%\n",
        "\n",
        "Wave C\n",
        f"{over_head_press.first_c} X 5 - 75%\n",
        f"{over_head_press.second_c} X 3 - 85%\n",
        f"{over_head_press.third_c} X 1 - 95%\n",
        "\n\n",

        f"Squat -  1RM {squat.one_rep_max}",
        "\n",
        "Wave A\n",
        f"{squat.first_a} X 5 - 65%\n",
        f"{squat.second_a} X 5 - 75%\n",
        f"{squat.third_a} X 5 - 85%\n",
        "\n",
        "Wave B\n",
        f"{squat.first_b} X 3 - 70%\n",
        f"{squat.second_b} X 3 - 80%\n",
        f"{squat.third_b} X 3 - 90%\n",
        "\n",
        "Wave C\n",
        f"{squat.first_c} X 5 - 75%\n",
        f"{squat.second_c} X 3 - 85%\n",
        f"{squat.third_c} X 1 - 95%\n",
        "\n\n"

        f"Bench Press -  1RM {bench_press.one_rep_max}",
        "\n",
        "Wave A\n",
        f"{bench_press.first_a} X 5 - 65%\n",
        f"{bench_press.second_a} X 5 - 75%\n",
        f"{bench_press.third_a} X 5 - 85%\n",
        "\n",
        "Wave B\n",
        f"{bench_press.first_b} X 3 - 70%\n",
        f"{bench_press.second_b} X 3 - 80%\n",
        f"{bench_press.third_b} X 3 - 90%\n",
        "\n",
        "Wave C\n",
        f"{bench_press.first_c} X 5 - 75%\n",
        f"{bench_press.second_c} X 3 - 85%\n",
        f"{bench_press.third_c} X 1 - 95%\n",
        "\n\n",

        f"Dead Lift -  1RM {deadlift.one_rep_max}",
        "\n",
        "Wave A\n",
        f"{deadlift.first_a} X 5 - 65%\n",
        f"{deadlift.second_a} X 5 - 75%\n",
        f"{deadlift.third_a} X 5 - 85%\n",
        "\n",
        "Wave B\n",
        f"{deadlift.first_b} X 3 - 70%\n",
        f"{deadlift.second_b} X 3 - 80%\n",
        f"{deadlift.third_b} X 3 - 90%\n",
        "\n",
        "Wave C\n",
        f"{deadlift.first_c} X 5 - 75%\n",
        f"{deadlift.second_c} X 3 - 85%\n",
        f"{deadlift.third_c} X 1 - 95%\n",
        ]

file.writelines(text)
file.close()
print('Your file is ready... ')
