import plotly.express as px
from die import Dice


die = Dice()

rolls_number = 1000
rolls_result = die.multiple_rolls(rolls_number)
frequencies = die.frequencies(rolls_result)

possible_results = die.possible_results()

title = f"Result of Rolling One D6 Die {rolls_number} Times"
labels = {
    'x': "Result",
    "y": "Frequency of Result"
}
fig = px.bar(
    x=possible_results,
    y=frequencies,
    title=title,
    labels=labels
)

fig.show()
